import sys, argparse
from importlib import util
from timeit import default_timer as timer
import queue

# Import algorithms
from Part_1.algorithms.dfs import dfs
from Part_1.algorithms.bfs import bfs
from Part_1.algorithms.dijkstra import dijkstra
from Part_1.algorithms.best_first_search import best_first_search

# Import schedule generator
from Part_1.schedule import Schedule

class Model:

	# The network of the model.
	network = None

	# The exist properties to check.
	exists_list = []

	# The Xmin properties to check.
	xmin_list = []

	def __init__(self):
		self.import_model()

		# Schedule class which checks the variables "clk" and "load" to construct a schedule.
		self.schedule = Schedule('clk', 'load')

	
	def get_parameters(self):
		return self.network, self.exists_list, self.xmin_list, self.debug_mode, self.print_trace

	def import_model(self):
		parser = argparse.ArgumentParser(description='Modest model checker')
		parser.add_argument('--d', help='d(ebug): Enter runtime debug mode', action='store_true')
		parser.add_argument('--t', help='t(race): Print the property trace', action='store_true')
		parser.add_argument('--s', help='s(chedule): Create human-readable CSV schedules and KiBam baseload CSV', action='store_true')
		parser.add_argument('--bfs', help='bfs: Use the Breadth First Search algorithm for the exist properties, default is DFS', action='store_true')
		parser.add_argument('--dijkstra', help='dijkstra: Use Dijkstra algorithm for the Xmin properties, default is Best First Search', action='store_true')
		parser.add_argument('model', help='specify .py model exported from Modest')

		args = parser.parse_args()

		# Load the model
		try:
			if not args.model:
				print("Error: No model specified.")
				quit()

			# Get the arguments.
			self.debug_mode = args.d
			self.print_trace = args.t
			self.create_schedule = args.s
			self.use_bfs = args.bfs
			self.use_dijkstra = args.dijkstra


			print("Loading model from \"{0}\"...".format(args.model), end = "", flush = True)
			spec = util.spec_from_file_location("model", args.model)
			model = util.module_from_spec(spec)
			spec.loader.exec_module(model)
			network = model.Network() # create network instance
			print(" done.") 
		except:
			print("Failed to load the model. Check the provided arguments.")
			quit()


		# Print some information about the model and the initial state
		print("\nThe model has", str(len(network.properties)), "properties.")

		reachability_list = []
		cost_optimal_list = []

		for prop in range(len(network.properties)):
			#print("* Property", prop, "is:", str(network.properties[prop]))
			is_reach = network.properties[prop].exp is not None and network.properties[prop].exp.op == "exists" and network.properties[prop].exp.args[0].op == "eventually" and network.properties[prop].exp.args[0].args[0].op == "ap"
			
			
			#print("* Property ", prop, " is:", "" if is_reach else " not", " a reachability property.", sep = "")
			is_reward = network.properties[prop].exp is not None and network.properties[prop].exp.op == "xmin" and network.properties[prop].exp.args[1].op == "ap"
			if is_reward:
				cost_optimal_list.append(str(network.properties[prop]))
				#print("* The following proposition must hold for the property:", network.properties[prop].exp.args[1].args[0])
			if is_reach:
				reachability_list.append(str(network.properties[prop]))
				#print("* The following proposition must hold for the property:", network.properties[prop].exp.args[0].args[0].args[0])
			#print("* Property ", prop, " is:", "" if is_reward else " not", " a cost-optimal reachability property.", sep = "")
			if network.properties[prop].exp is not None and network.properties[prop].exp.op == "exists" and network.properties[prop].exp.args[0].op == "eventually" and network.properties[prop].exp.args[0].args[0].op == "ap":
				self.exists_list.append((prop, str(network.properties[prop])))
			if network.properties[prop].exp is not None and network.properties[prop].exp.op == "xmin" and network.properties[prop].exp.args[1].op == "ap":
				self.xmin_list.append((prop, str(network.properties[prop])))

		self.network = network

		if reachability_list:
			print("The following reachabiliy properties will be checked: ")
			for prop in reachability_list:
				print(prop)

		if cost_optimal_list:
			print("The following cost-optimal reachability properties will be checked: ")
			for prop in cost_optimal_list:
				print(prop)


	def check_property_exists(self):
		
		# Check if there are "exist" properties to check.
		if len(self.exists_list) == 0:
			# Return if there is nothing to check.
			return

		# Iterate over all elements of the reachability list.
		for exist, name in self.exists_list:	
			# Record start time.
			start_time = timer()

			result = None

			# Perform the requested check (DFS as default).
			if self.use_bfs:
				print('\nChecking "' + name + '" with BFS.')
				result = bfs(self.network, self.network.properties[exist].exp.args[0].args[0].args[0])
			else:
				print('\nChecking "' + name + '" with DFS.')
				result = dfs(self.network, self.network.properties[exist].exp.args[0].args[0].args[0])

			# Get the results from the result tuple.
			found, number_of_states, trace = result

			if found:
				if self.print_trace:
					print("Diagnostic trace to target denoted by '---transition-->state':")
					for state in trace:
						print(state)
				print("The property", str(self.network.properties[exist]), "holds") #If goal holds in current state, the property holds
			else:
				if self.print_trace:
					print("Diagnostic trace to target denoted by '---transition-->state':")
					for state in trace:
						print(state)
				print("The property", str(self.network.properties[exist]), "does not hold") #If goal holds in current state, the property holds
			print('Checked in {0:.2f} seconds.'.format(timer() - start_time) + "\n")


	def check_property_xmin(self):

		# Check if there are "xmin" properties to check.
		if len(self.xmin_list) == 0:
			# Return if there is nothing to check.
			return

		# Iterate over all elements of the xmin reachability list.
		for xmin, name in self.xmin_list:
			# Record start time.
			start_time = timer()

			result = None 

			# Perform the requested check (BFS as default).
			if self.use_dijkstra:
				print('\nChecking "' + name + '" with Dijkstra.')
				result = dijkstra(self.network, self.network.properties[xmin].exp.args[1].args[0], xmin, self.debug_mode)
			else:
				print('\nChecking "' + name + '" with Best First Search.')
				result = best_first_search(self.network, self.network.properties[xmin].exp.args[1].args[0], xmin, self.debug_mode)

			# Get the results from the result tuple.
			found, number_of_steps, trace = result
			
			#found, numberofstates = eval(function)(self.network, self.network.properties[xmin].exp.args[1].args[0], trace, xmin, self.debug_mode)
			if found:

				# If debug mode is specified the full trace is printed.
				if self.print_trace:
					print("Diagnostic minimum cost trace to target denoted by '---transition-->\tcost\tstate':")
					for state in trace:
						print(state)
				
				print("The property " + str(self.network.properties[xmin]) + " holds with a total cost of: " + str(number_of_steps)) #If goal holds in current state, the property holds

				if self.create_schedule:
					self.schedule.create_schedules_from_trace(trace)

			else:
				if self.print_trace:
					print("Stack trace of taken transitions:")
					for state in trace:
						print(state)
				print("The property", str(self.network.properties[xmin]), "does not hold.") #If goal holds in current state, the property holds
			
			print('Checked in {0:.2f} seconds.'.format(timer() - start_time) + "\n")
