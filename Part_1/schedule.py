# Class which can be used to create a schedule in various ways.
import os, csv
from datetime import datetime
import plotly.express as px
import pandas as pd

class Schedule:

	time = 1458450000 # 03/20/2016 @ 5:00am (UTC)
	job_types = ['3F2', '3F3', 'UHF', 'Kourou', 'Toulouse']

	def __init__(self, clock_name, load_name):
		self.clock = clock_name
		self.load = load_name

	def create_simulink_schedule_from_trace(self, trace):
		# Every moment that the load changes has to be recorded.
		# The "moment" that this happens is defined by the variable which is in self.clock.

		schedule = []
		prev_clock = None
		prev_load = None 

		for action in trace:
			try:
				# Multiply the accumulating value (of the clock) by 60 to get the correct time base in seconds again.
				clock_value = int(int(action.split(self.clock + ' = ', 1)[1].split(',')[0]) * 60)
				load_value = int(int(action.split(self.load + ' = ', 1)[1].split(',')[0]) / 60)

				if not schedule:
					# List is empty.
					schedule.append((0, load_value))

				if prev_clock == clock_value and prev_load != load_value:
						# A new load is detected at this clock moment.
						# Close the left hand limit and open one on the right.
						schedule.append((clock_value, prev_load))
						schedule.append((clock_value, load_value))			
				prev_clock = clock_value
				prev_load = load_value

			except:
				print('Trace cannot be properly parsed. Check the variable names!')
				return False
		
		# Append the closing clock and load to make the schedule continuous.
		schedule.append((int(trace[-1].split(self.clock + ' = ', 1)[1].split(',')[0]) * 60, prev_load))

		# Schedule is now available as tuples in the list.
		# Write the list of tuples to a csv file.
		self.write_list_to_csv('simulink_schedule', schedule)
		return True


	def create_human_readable_schedule_from_trace(self, trace):
		
		# Create a dictionary of lists for each job type.
		job_actions = {}

		# Create a dataframe for the Gantt chart
		df = pd.DataFrame([])

		for job_type in self.job_types:
			# Add an empty list for each job.
			job_actions = []
			job_actions.append(['"Job"', '"Start Time (UTC)"', '"Stop Time (UTC)"', '"Duration (sec)"'])

		job_start_time = 0

		try:
			for action in trace:

				for job in self.job_types:
					jobdict = {}

					# Get the time.
					clock_value = int(action.split(self.clock + ' = ', 1)[1].split(',')[0]) * 60

					# What kind of action is this?
					if 'Skip_' + job in action:
						# Job is skipped.
						skip_time = datetime.utcfromtimestamp(self.time + clock_value).strftime('%d %b %Y %H:%M:%S')
						job_actions.append([job, skip_time, skip_time , str(0)])

					if job + '_start-->' in action:
						# Job has started.
						job_start_time = clock_value

					if job + '_end-->' in action:
						# Job has ended.
						start_time = datetime.utcfromtimestamp(self.time + job_start_time).strftime('%d %b %Y %H:%M:%S')
						end_time = datetime.utcfromtimestamp(self.time + clock_value).strftime('%d %b %Y %H:%M:%S')
						duration = clock_value - job_start_time
						job_actions.append([job, start_time, end_time, str(duration)])
						
						jobdict['Job'] = job
						jobdict['Start'] = datetime.fromtimestamp(self.time + job_start_time)
						jobdict['End'] = datetime.fromtimestamp(self.time + clock_value)
						if job == '3F2' or job == '3F3':
							jobdict['Job type:'] = "L-Band"
						elif job == 'Kourou' or job == 'Toulouse':
							jobdict['Job type:'] = "X-Band"
						elif job == 'UHF':
							jobdict['Job type:'] = "UHF"
						else:
							jobdict['Job type:'] = "NAN"
						
						df = df.append(jobdict, ignore_index=True)
			
		except:
			print('Trace cannot be properly parsed. Check the variable names!')
			return False
		
		# Get the lists from the dictionary one by one.
		self.write_list_to_csv('schedule', job_actions)

		fig = px.timeline(df, x_start="Start", x_end="End", y="Job", color="Job type:")
		fig.update_yaxes(autorange="reversed") # otherwise tasks are listed from the bottom up
		fig.show()

		return True


	def create_schedules_from_trace(self, trace):
		# Try to create a simulink schedule.
		if self.create_simulink_schedule_from_trace(trace):
			# Schedule successfully created!
			# Now try to create the human readable schedule.
			if self.create_human_readable_schedule_from_trace(trace):
				print("Schedules successfully created.\n")
			else:
				print("Failed to create human readable schedule.\n")
		else:
			print("Failed to create simulink schedule.\n")


	def create_schedules_from_txt_file(self, file_path):
		trace = []
		try:
			with open(file_path, "r") as f:
				for item in f:
					trace.append(item)
		except:
			print("Failed parsing file to trace!")
		
		self.create_schedules_from_trace(trace)

	def write_list_to_csv(self, name, list_to_write):
		if not os.path.exists('output'):
			os.makedirs('output')

		try:
			with open('output/' + name + '.csv','w', newline='') as out:
				csv_out = csv.writer(out, delimiter=',', escapechar=' ', quoting=csv.QUOTE_NONE)
				csv_out.writerows(list_to_write)
		except:
			print("Attempting to write schedule to file failed.")	