# GomX-3

from __future__ import annotations
from typing import List, Union, Optional

class VariableInfo(object):
	__slots__ = ("name", "component", "type", "minValue", "maxValue")
	
	def __init__(self, name: str, component: Optional[int], type: str, minValue = None, maxValue = None):
		self.name = name
		self.component = component
		self.type = type
		self.minValue = minValue
		self.maxValue = maxValue

# States
class State(object):
	__slots__ = ("clk", "job_clk", "load", "SoC", "last_a_time", "current_a_time", "L_3F2_i", "L_3F3_i", "Sun_i", "UHF_i", "X_Kourou_i", "X_Toulouse_i", "is_aligned", "L_X_counter", "Battery_job_location", "PV_job_location", "UHF_job_location", "L_X_Scheduler_location", "sched_clk")
	
	def get_variable_value(self, variable: int):
		if variable == 0:
			return self.clk
		elif variable == 1:
			return self.job_clk
		elif variable == 2:
			return self.load
		elif variable == 3:
			return self.SoC
		elif variable == 4:
			return self.last_a_time
		elif variable == 5:
			return self.current_a_time
		elif variable == 6:
			return self.L_3F2_i
		elif variable == 7:
			return self.L_3F3_i
		elif variable == 8:
			return self.Sun_i
		elif variable == 9:
			return self.UHF_i
		elif variable == 10:
			return self.X_Kourou_i
		elif variable == 11:
			return self.X_Toulouse_i
		elif variable == 12:
			return self.is_aligned
		elif variable == 13:
			return self.L_X_counter
		elif variable == 14:
			return self.Battery_job_location
		elif variable == 15:
			return self.PV_job_location
		elif variable == 16:
			return self.UHF_job_location
		elif variable == 17:
			return self.L_X_Scheduler_location
		elif variable == 18:
			return self.sched_clk
	
	def copy_to(self, other: State):
		other.clk = self.clk
		other.job_clk = self.job_clk
		other.load = self.load
		other.SoC = self.SoC
		other.last_a_time = self.last_a_time
		other.current_a_time = self.current_a_time
		other.L_3F2_i = self.L_3F2_i
		other.L_3F3_i = self.L_3F3_i
		other.Sun_i = self.Sun_i
		other.UHF_i = self.UHF_i
		other.X_Kourou_i = self.X_Kourou_i
		other.X_Toulouse_i = self.X_Toulouse_i
		other.is_aligned = self.is_aligned
		other.L_X_counter = list(self.L_X_counter)
		other.Battery_job_location = self.Battery_job_location
		other.PV_job_location = self.PV_job_location
		other.UHF_job_location = self.UHF_job_location
		other.L_X_Scheduler_location = self.L_X_Scheduler_location
		other.sched_clk = self.sched_clk
	
	def __eq__(self, other):
		return isinstance(other, self.__class__) and self.clk == other.clk and self.job_clk == other.job_clk and self.load == other.load and self.SoC == other.SoC and self.last_a_time == other.last_a_time and self.current_a_time == other.current_a_time and self.L_3F2_i == other.L_3F2_i and self.L_3F3_i == other.L_3F3_i and self.Sun_i == other.Sun_i and self.UHF_i == other.UHF_i and self.X_Kourou_i == other.X_Kourou_i and self.X_Toulouse_i == other.X_Toulouse_i and self.is_aligned == other.is_aligned and self.L_X_counter == other.L_X_counter and self.Battery_job_location == other.Battery_job_location and self.PV_job_location == other.PV_job_location and self.UHF_job_location == other.UHF_job_location and self.L_X_Scheduler_location == other.L_X_Scheduler_location and self.sched_clk == other.sched_clk
	
	def __ne__(self, other):
		return not self.__eq__(other)
	
	def __hash__(self):
		result = 75619
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.clk)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.job_clk)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.load)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.SoC)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.last_a_time)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.current_a_time)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.L_3F2_i)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.L_3F3_i)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.Sun_i)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.UHF_i)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.X_Kourou_i)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.X_Toulouse_i)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.is_aligned)) & 0xFFFFFFFF
		for x in self.L_X_counter:
			result = (((101 * result) & 0xFFFFFFFF) + hash(x)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.Battery_job_location)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.PV_job_location)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.UHF_job_location)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.L_X_Scheduler_location)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.sched_clk)) & 0xFFFFFFFF
		return result
	
	def __str__(self):
		result = "("
		result += "clk = " + str(self.clk)
		result += ", job_clk = " + str(self.job_clk)
		result += ", load = " + str(self.load)
		result += ", SoC = " + str(self.SoC)
		result += ", last_a_time = " + str(self.last_a_time)
		result += ", current_a_time = " + str(self.current_a_time)
		result += ", L_3F2_i = " + str(self.L_3F2_i)
		result += ", L_3F3_i = " + str(self.L_3F3_i)
		result += ", Sun_i = " + str(self.Sun_i)
		result += ", UHF_i = " + str(self.UHF_i)
		result += ", X_Kourou_i = " + str(self.X_Kourou_i)
		result += ", X_Toulouse_i = " + str(self.X_Toulouse_i)
		result += ", is_aligned = " + str(self.is_aligned)
		result += ", L_X_counter = " + str(self.L_X_counter)
		result += ", Battery_job_location = " + str(self.Battery_job_location)
		result += ", PV_job_location = " + str(self.PV_job_location)
		result += ", UHF_job_location = " + str(self.UHF_job_location)
		result += ", L_X_Scheduler_location = " + str(self.L_X_Scheduler_location)
		result += ", sched_clk = " + str(self.sched_clk)
		result += ")"
		return result

# Transients
class Transient(object):
	__slots__ = ("Generated_Schedule_until_clk__edge_reward", "L_Band_Inmarsat_3F2_data", "L_Band_Inmarsat_3F3_data", "Sun_data", "UHF_data", "X_Band_Kourou_data", "X_Band_Toulouse_data", "cost")
	
	def copy_to(self, other: Transient):
		other.Generated_Schedule_until_clk__edge_reward = self.Generated_Schedule_until_clk__edge_reward
		other.L_Band_Inmarsat_3F2_data = list(self.L_Band_Inmarsat_3F2_data)
		other.L_Band_Inmarsat_3F3_data = list(self.L_Band_Inmarsat_3F3_data)
		other.Sun_data = list(self.Sun_data)
		other.UHF_data = list(self.UHF_data)
		other.X_Band_Kourou_data = list(self.X_Band_Kourou_data)
		other.X_Band_Toulouse_data = list(self.X_Band_Toulouse_data)
		other.cost = self.cost
	
	def __eq__(self, other):
		return isinstance(other, self.__class__) and self.Generated_Schedule_until_clk__edge_reward == other.Generated_Schedule_until_clk__edge_reward and self.L_Band_Inmarsat_3F2_data == other.L_Band_Inmarsat_3F2_data and self.L_Band_Inmarsat_3F3_data == other.L_Band_Inmarsat_3F3_data and self.Sun_data == other.Sun_data and self.UHF_data == other.UHF_data and self.X_Band_Kourou_data == other.X_Band_Kourou_data and self.X_Band_Toulouse_data == other.X_Band_Toulouse_data and self.cost == other.cost
	
	def __ne__(self, other):
		return not self.__eq__(other)
	
	def __hash__(self):
		result = 75619
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.Generated_Schedule_until_clk__edge_reward)) & 0xFFFFFFFF
		for x in self.L_Band_Inmarsat_3F2_data:
			result = (((101 * result) & 0xFFFFFFFF) + hash(x)) & 0xFFFFFFFF
		for x in self.L_Band_Inmarsat_3F3_data:
			result = (((101 * result) & 0xFFFFFFFF) + hash(x)) & 0xFFFFFFFF
		for x in self.Sun_data:
			result = (((101 * result) & 0xFFFFFFFF) + hash(x)) & 0xFFFFFFFF
		for x in self.UHF_data:
			result = (((101 * result) & 0xFFFFFFFF) + hash(x)) & 0xFFFFFFFF
		for x in self.X_Band_Kourou_data:
			result = (((101 * result) & 0xFFFFFFFF) + hash(x)) & 0xFFFFFFFF
		for x in self.X_Band_Toulouse_data:
			result = (((101 * result) & 0xFFFFFFFF) + hash(x)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.cost)) & 0xFFFFFFFF
		return result
	
	def __str__(self):
		result = "("
		result += "Generated_Schedule_until_clk__edge_reward = " + str(self.Generated_Schedule_until_clk__edge_reward)
		result += ", L_Band_Inmarsat_3F2_data = " + str(self.L_Band_Inmarsat_3F2_data)
		result += ", L_Band_Inmarsat_3F3_data = " + str(self.L_Band_Inmarsat_3F3_data)
		result += ", Sun_data = " + str(self.Sun_data)
		result += ", UHF_data = " + str(self.UHF_data)
		result += ", X_Band_Kourou_data = " + str(self.X_Band_Kourou_data)
		result += ", X_Band_Toulouse_data = " + str(self.X_Band_Toulouse_data)
		result += ", cost = " + str(self.cost)
		result += ")"
		return result

# Automaton: Battery_job
class Battery_jobAutomaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [19, 1, 19]
		self.transition_labels = [[1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 40], [40], [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 40]]
		self.branch_counts = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
	
	def set_initial_values(self, state: State) -> None:
		state.Battery_job_location = 0
	
	def set_initial_transient_values(self, transient: Transient) -> None:
		pass
	
	def get_transient_value(self, state: State, transient_variable: str):
		location = state.Battery_job_location
		return None
	
	def get_transition_count(self, state: State) -> int:
		return self.transition_counts[state.Battery_job_location]
	
	def get_transition_label(self, state: State, transition: int) -> int:
		return self.transition_labels[state.Battery_job_location][transition]
	
	def get_guard_value(self, state: State, transition: int) -> bool:
		location = state.Battery_job_location
		if location == 1:
			return True
		elif location == 0:
			if transition >= 0 and transition < 6:
				return ((state.SoC - (state.load * (state.current_a_time - state.last_a_time))) >= 149760000)
			elif transition >= 6 and transition < 12:
				return (((state.SoC - (state.load * (state.current_a_time - state.last_a_time))) > 59904000) and ((state.SoC - (state.load * (state.current_a_time - state.last_a_time))) < 149760000))
			elif transition >= 12 and transition < 18:
				return ((state.SoC - (state.load * (state.current_a_time - state.last_a_time))) <= 59904000)
			elif transition == 18:
				return True
		elif location == 2:
			if transition >= 0 and transition < 6:
				return ((state.SoC - (state.load * (state.current_a_time - state.last_a_time))) >= 149760000)
			elif transition >= 6 and transition < 12:
				return (((state.SoC - (state.load * (state.current_a_time - state.last_a_time))) > 59904000) and ((state.SoC - (state.load * (state.current_a_time - state.last_a_time))) < 149760000))
			elif transition >= 12 and transition < 18:
				return ((state.SoC - (state.load * (state.current_a_time - state.last_a_time))) <= 59904000)
			elif transition == 18:
				return True
	
	def get_branch_count(self, state: State, transition: int) -> int:
		return self.branch_counts[state.Battery_job_location][transition]
	
	def get_probability_value(self, state: State, transition: int, branch: int) -> float:
		location = state.Battery_job_location
		if location == 0:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			elif transition == 3:
				return 1
			elif transition == 4:
				return 1
			elif transition == 5:
				return 1
			elif transition == 6:
				return 1
			elif transition == 7:
				return 1
			elif transition == 8:
				return 1
			elif transition == 9:
				return 1
			elif transition == 10:
				return 1
			elif transition == 11:
				return 1
			elif transition == 12:
				return 1
			elif transition == 13:
				return 1
			elif transition == 14:
				return 1
			elif transition == 15:
				return 1
			elif transition == 16:
				return 1
			elif transition == 17:
				return 1
			elif transition == 18:
				return 1
		elif location == 1:
			if transition == 0:
				return 1
		elif location == 2:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			elif transition == 3:
				return 1
			elif transition == 4:
				return 1
			elif transition == 5:
				return 1
			elif transition == 6:
				return 1
			elif transition == 7:
				return 1
			elif transition == 8:
				return 1
			elif transition == 9:
				return 1
			elif transition == 10:
				return 1
			elif transition == 11:
				return 1
			elif transition == 12:
				return 1
			elif transition == 13:
				return 1
			elif transition == 14:
				return 1
			elif transition == 15:
				return 1
			elif transition == 16:
				return 1
			elif transition == 17:
				return 1
			elif transition == 18:
				return 1
	
	def jump(self, state: State, transient: Transient, transition: int, branch: int, assignment_index: int, target_state: State, target_transient: Transient) -> None:
		if assignment_index == 0:
			location = state.Battery_job_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.SoC = 149760000
				elif transition == 1:
					if branch == 0:
						target_state.SoC = 149760000
				elif transition == 2:
					if branch == 0:
						target_state.SoC = 149760000
				elif transition == 3:
					if branch == 0:
						target_state.SoC = 149760000
				elif transition == 4:
					if branch == 0:
						target_state.SoC = 149760000
				elif transition == 5:
					if branch == 0:
						target_state.SoC = 149760000
				elif transition == 6:
					if branch == 0:
						target_state.SoC = (state.SoC - (state.load * (state.current_a_time - state.last_a_time)))
						if target_state.SoC < 0:
							raise OverflowError("Assigned value of " + str(target_state.SoC) + " is less than the lower bound of 0 for variable \"SoC\".")
				elif transition == 7:
					if branch == 0:
						target_state.SoC = (state.SoC - (state.load * (state.current_a_time - state.last_a_time)))
						if target_state.SoC < 0:
							raise OverflowError("Assigned value of " + str(target_state.SoC) + " is less than the lower bound of 0 for variable \"SoC\".")
				elif transition == 8:
					if branch == 0:
						target_state.SoC = (state.SoC - (state.load * (state.current_a_time - state.last_a_time)))
						if target_state.SoC < 0:
							raise OverflowError("Assigned value of " + str(target_state.SoC) + " is less than the lower bound of 0 for variable \"SoC\".")
				elif transition == 9:
					if branch == 0:
						target_state.SoC = (state.SoC - (state.load * (state.current_a_time - state.last_a_time)))
						if target_state.SoC < 0:
							raise OverflowError("Assigned value of " + str(target_state.SoC) + " is less than the lower bound of 0 for variable \"SoC\".")
				elif transition == 10:
					if branch == 0:
						target_state.SoC = (state.SoC - (state.load * (state.current_a_time - state.last_a_time)))
						if target_state.SoC < 0:
							raise OverflowError("Assigned value of " + str(target_state.SoC) + " is less than the lower bound of 0 for variable \"SoC\".")
				elif transition == 11:
					if branch == 0:
						target_state.SoC = (state.SoC - (state.load * (state.current_a_time - state.last_a_time)))
						if target_state.SoC < 0:
							raise OverflowError("Assigned value of " + str(target_state.SoC) + " is less than the lower bound of 0 for variable \"SoC\".")
				elif transition == 12:
					if branch == 0:
						target_transient.cost = 1000
				elif transition == 13:
					if branch == 0:
						target_transient.cost = 1000
				elif transition == 14:
					if branch == 0:
						target_transient.cost = 1000
				elif transition == 15:
					if branch == 0:
						target_transient.cost = 1000
				elif transition == 16:
					if branch == 0:
						target_transient.cost = 1000
				elif transition == 17:
					if branch == 0:
						target_transient.cost = 1000
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.SoC = 149760000
				elif transition == 1:
					if branch == 0:
						target_state.SoC = 149760000
				elif transition == 2:
					if branch == 0:
						target_state.SoC = 149760000
				elif transition == 3:
					if branch == 0:
						target_state.SoC = 149760000
				elif transition == 4:
					if branch == 0:
						target_state.SoC = 149760000
				elif transition == 5:
					if branch == 0:
						target_state.SoC = 149760000
				elif transition == 6:
					if branch == 0:
						target_state.SoC = (state.SoC - (state.load * (state.current_a_time - state.last_a_time)))
						if target_state.SoC < 0:
							raise OverflowError("Assigned value of " + str(target_state.SoC) + " is less than the lower bound of 0 for variable \"SoC\".")
				elif transition == 7:
					if branch == 0:
						target_state.SoC = (state.SoC - (state.load * (state.current_a_time - state.last_a_time)))
						if target_state.SoC < 0:
							raise OverflowError("Assigned value of " + str(target_state.SoC) + " is less than the lower bound of 0 for variable \"SoC\".")
				elif transition == 8:
					if branch == 0:
						target_state.SoC = (state.SoC - (state.load * (state.current_a_time - state.last_a_time)))
						if target_state.SoC < 0:
							raise OverflowError("Assigned value of " + str(target_state.SoC) + " is less than the lower bound of 0 for variable \"SoC\".")
				elif transition == 9:
					if branch == 0:
						target_state.SoC = (state.SoC - (state.load * (state.current_a_time - state.last_a_time)))
						if target_state.SoC < 0:
							raise OverflowError("Assigned value of " + str(target_state.SoC) + " is less than the lower bound of 0 for variable \"SoC\".")
				elif transition == 10:
					if branch == 0:
						target_state.SoC = (state.SoC - (state.load * (state.current_a_time - state.last_a_time)))
						if target_state.SoC < 0:
							raise OverflowError("Assigned value of " + str(target_state.SoC) + " is less than the lower bound of 0 for variable \"SoC\".")
				elif transition == 11:
					if branch == 0:
						target_state.SoC = (state.SoC - (state.load * (state.current_a_time - state.last_a_time)))
						if target_state.SoC < 0:
							raise OverflowError("Assigned value of " + str(target_state.SoC) + " is less than the lower bound of 0 for variable \"SoC\".")
				elif transition == 12:
					if branch == 0:
						target_transient.cost = 1000
				elif transition == 13:
					if branch == 0:
						target_transient.cost = 1000
				elif transition == 14:
					if branch == 0:
						target_transient.cost = 1000
				elif transition == 15:
					if branch == 0:
						target_transient.cost = 1000
				elif transition == 16:
					if branch == 0:
						target_transient.cost = 1000
				elif transition == 17:
					if branch == 0:
						target_transient.cost = 1000
		elif assignment_index == 2:
			location = state.Battery_job_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.Battery_job_location = 2
				elif transition == 1:
					if branch == 0:
						target_state.Battery_job_location = 2
				elif transition == 2:
					if branch == 0:
						target_state.Battery_job_location = 2
				elif transition == 3:
					if branch == 0:
						target_state.Battery_job_location = 2
				elif transition == 4:
					if branch == 0:
						target_state.Battery_job_location = 2
				elif transition == 5:
					if branch == 0:
						target_state.Battery_job_location = 2
				elif transition == 6:
					if branch == 0:
						target_state.Battery_job_location = 2
				elif transition == 7:
					if branch == 0:
						target_state.Battery_job_location = 2
				elif transition == 8:
					if branch == 0:
						target_state.Battery_job_location = 2
				elif transition == 9:
					if branch == 0:
						target_state.Battery_job_location = 2
				elif transition == 10:
					if branch == 0:
						target_state.Battery_job_location = 2
				elif transition == 11:
					if branch == 0:
						target_state.Battery_job_location = 2
				elif transition == 12:
					if branch == 0:
						target_state.Battery_job_location = 1
				elif transition == 13:
					if branch == 0:
						target_state.Battery_job_location = 1
				elif transition == 14:
					if branch == 0:
						target_state.Battery_job_location = 1
				elif transition == 15:
					if branch == 0:
						target_state.Battery_job_location = 1
				elif transition == 16:
					if branch == 0:
						target_state.Battery_job_location = 1
				elif transition == 17:
					if branch == 0:
						target_state.Battery_job_location = 1
				elif transition == 18:
					if branch == 0:
						target_state.Battery_job_location = 0
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.Battery_job_location = 1
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.Battery_job_location = 2
				elif transition == 1:
					if branch == 0:
						target_state.Battery_job_location = 2
				elif transition == 2:
					if branch == 0:
						target_state.Battery_job_location = 2
				elif transition == 3:
					if branch == 0:
						target_state.Battery_job_location = 2
				elif transition == 4:
					if branch == 0:
						target_state.Battery_job_location = 2
				elif transition == 5:
					if branch == 0:
						target_state.Battery_job_location = 2
				elif transition == 6:
					if branch == 0:
						target_state.Battery_job_location = 2
				elif transition == 7:
					if branch == 0:
						target_state.Battery_job_location = 2
				elif transition == 8:
					if branch == 0:
						target_state.Battery_job_location = 2
				elif transition == 9:
					if branch == 0:
						target_state.Battery_job_location = 2
				elif transition == 10:
					if branch == 0:
						target_state.Battery_job_location = 2
				elif transition == 11:
					if branch == 0:
						target_state.Battery_job_location = 2
				elif transition == 12:
					if branch == 0:
						target_state.Battery_job_location = 1
				elif transition == 13:
					if branch == 0:
						target_state.Battery_job_location = 1
				elif transition == 14:
					if branch == 0:
						target_state.Battery_job_location = 1
				elif transition == 15:
					if branch == 0:
						target_state.Battery_job_location = 1
				elif transition == 16:
					if branch == 0:
						target_state.Battery_job_location = 1
				elif transition == 17:
					if branch == 0:
						target_state.Battery_job_location = 1
				elif transition == 18:
					if branch == 0:
						target_state.Battery_job_location = 2

# Automaton: PV_job
class PV_jobAutomaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [4, 1, 1, 2, 1, 4, 1, 2, 1]
		self.transition_labels = [[7, 8, 41, 40], [40], [1], [9, 40], [1], [7, 8, 41, 40], [1], [10, 40], [1]]
		self.branch_counts = [[1, 1, 1, 1], [1], [1], [1, 1], [1], [1, 1, 1, 1], [1], [1, 1], [1]]
	
	def set_initial_values(self, state: State) -> None:
		state.PV_job_location = 0
	
	def set_initial_transient_values(self, transient: Transient) -> None:
		pass
	
	def get_transient_value(self, state: State, transient_variable: str):
		location = state.PV_job_location
		return None
	
	def get_transition_count(self, state: State) -> int:
		return self.transition_counts[state.PV_job_location]
	
	def get_transition_label(self, state: State, transition: int) -> int:
		return self.transition_labels[state.PV_job_location][transition]
	
	def get_guard_value(self, state: State, transition: int) -> bool:
		location = state.PV_job_location
		if location == 1 or location == 2 or location == 4 or location == 6 or location == 8:
			return True
		elif location == 0:
			if transition == 0:
				return (((state.clk >= (self.network._get_transient_value(state, "Sun_data"))[state.Sun_i]) and (state.Sun_i <= 85)) and state.is_aligned)
			elif transition == 1:
				return (((state.clk >= (self.network._get_transient_value(state, "Sun_data"))[state.Sun_i]) and (state.Sun_i <= 85)) and (not state.is_aligned))
			elif transition == 2:
				return (state.Sun_i > 85)
			elif transition == 3:
				return (state.clk < (self.network._get_transient_value(state, "Sun_data"))[state.Sun_i])
		elif location == 3:
			if transition == 0:
				return (state.clk >= (self.network._get_transient_value(state, "Sun_data"))[state.Sun_i])
			elif transition == 1:
				return (state.clk < (self.network._get_transient_value(state, "Sun_data"))[state.Sun_i])
		elif location == 5:
			if transition == 0:
				return (((state.clk >= (self.network._get_transient_value(state, "Sun_data"))[state.Sun_i]) and (state.Sun_i <= 85)) and state.is_aligned)
			elif transition == 1:
				return (((state.clk >= (self.network._get_transient_value(state, "Sun_data"))[state.Sun_i]) and (state.Sun_i <= 85)) and (not state.is_aligned))
			elif transition == 2:
				return (state.Sun_i > 85)
			elif transition == 3:
				return (state.clk < (self.network._get_transient_value(state, "Sun_data"))[state.Sun_i])
		elif location == 7:
			if transition == 0:
				return (state.clk >= (self.network._get_transient_value(state, "Sun_data"))[state.Sun_i])
			elif transition == 1:
				return (state.clk < (self.network._get_transient_value(state, "Sun_data"))[state.Sun_i])
	
	def get_branch_count(self, state: State, transition: int) -> int:
		return self.branch_counts[state.PV_job_location][transition]
	
	def get_probability_value(self, state: State, transition: int, branch: int) -> float:
		location = state.PV_job_location
		if location == 0:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			elif transition == 3:
				return 1
		elif location == 1:
			if transition == 0:
				return 1
		elif location == 2:
			if transition == 0:
				return 1
		elif location == 3:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
		elif location == 4:
			if transition == 0:
				return 1
		elif location == 5:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			elif transition == 3:
				return 1
		elif location == 6:
			if transition == 0:
				return 1
		elif location == 7:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
		elif location == 8:
			if transition == 0:
				return 1
	
	def jump(self, state: State, transient: Transient, transition: int, branch: int, assignment_index: int, target_state: State, target_transient: Transient) -> None:
		if assignment_index == 0:
			location = state.PV_job_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.Sun_i = (state.Sun_i + 1)
						if target_state.Sun_i > 86:
							raise OverflowError("Assigned value of " + str(target_state.Sun_i) + " is greater than the upper bound of 86 for variable \"Sun_i\".")
						target_state.last_a_time = state.current_a_time
						target_state.current_a_time = (transient.Sun_data)[state.Sun_i]
				elif transition == 1:
					if branch == 0:
						target_state.Sun_i = (state.Sun_i + 1)
						if target_state.Sun_i > 86:
							raise OverflowError("Assigned value of " + str(target_state.Sun_i) + " is greater than the upper bound of 86 for variable \"Sun_i\".")
						target_state.last_a_time = state.current_a_time
						target_state.current_a_time = (transient.Sun_data)[state.Sun_i]
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.load = (state.load - 342000)
						if target_state.load < -1200000:
							raise OverflowError("Assigned value of " + str(target_state.load) + " is less than the lower bound of -1200000 for variable \"load\".")
			elif location == 3:
				if transition == 0:
					if branch == 0:
						target_state.Sun_i = (state.Sun_i + 1)
						if target_state.Sun_i > 86:
							raise OverflowError("Assigned value of " + str(target_state.Sun_i) + " is greater than the upper bound of 86 for variable \"Sun_i\".")
						target_state.last_a_time = state.current_a_time
						target_state.current_a_time = (transient.Sun_data)[state.Sun_i]
			elif location == 4:
				if transition == 0:
					if branch == 0:
						target_state.load = (state.load + 342000)
						if target_state.load > 1200000:
							raise OverflowError("Assigned value of " + str(target_state.load) + " is greater than the upper bound of 1200000 for variable \"load\".")
			elif location == 5:
				if transition == 0:
					if branch == 0:
						target_state.Sun_i = (state.Sun_i + 1)
						if target_state.Sun_i > 86:
							raise OverflowError("Assigned value of " + str(target_state.Sun_i) + " is greater than the upper bound of 86 for variable \"Sun_i\".")
						target_state.last_a_time = state.current_a_time
						target_state.current_a_time = (transient.Sun_data)[state.Sun_i]
				elif transition == 1:
					if branch == 0:
						target_state.Sun_i = (state.Sun_i + 1)
						if target_state.Sun_i > 86:
							raise OverflowError("Assigned value of " + str(target_state.Sun_i) + " is greater than the upper bound of 86 for variable \"Sun_i\".")
						target_state.last_a_time = state.current_a_time
						target_state.current_a_time = (transient.Sun_data)[state.Sun_i]
			elif location == 6:
				if transition == 0:
					if branch == 0:
						target_state.load = (state.load - 366000)
						if target_state.load < -1200000:
							raise OverflowError("Assigned value of " + str(target_state.load) + " is less than the lower bound of -1200000 for variable \"load\".")
			elif location == 7:
				if transition == 0:
					if branch == 0:
						target_state.Sun_i = (state.Sun_i + 1)
						if target_state.Sun_i > 86:
							raise OverflowError("Assigned value of " + str(target_state.Sun_i) + " is greater than the upper bound of 86 for variable \"Sun_i\".")
						target_state.last_a_time = state.current_a_time
						target_state.current_a_time = (transient.Sun_data)[state.Sun_i]
			elif location == 8:
				if transition == 0:
					if branch == 0:
						target_state.load = (state.load + 366000)
						if target_state.load > 1200000:
							raise OverflowError("Assigned value of " + str(target_state.load) + " is greater than the upper bound of 1200000 for variable \"load\".")
		elif assignment_index == 2:
			location = state.PV_job_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.PV_job_location = 6
				elif transition == 1:
					if branch == 0:
						target_state.PV_job_location = 2
				elif transition == 2:
					if branch == 0:
						target_state.PV_job_location = 1
				elif transition == 3:
					if branch == 0:
						target_state.PV_job_location = 0
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.PV_job_location = 1
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.PV_job_location = 3
			elif location == 3:
				if transition == 0:
					if branch == 0:
						target_state.PV_job_location = 4
				elif transition == 1:
					if branch == 0:
						target_state.PV_job_location = 3
			elif location == 4:
				if transition == 0:
					if branch == 0:
						target_state.PV_job_location = 5
			elif location == 5:
				if transition == 0:
					if branch == 0:
						target_state.PV_job_location = 6
				elif transition == 1:
					if branch == 0:
						target_state.PV_job_location = 2
				elif transition == 2:
					if branch == 0:
						target_state.PV_job_location = 1
				elif transition == 3:
					if branch == 0:
						target_state.PV_job_location = 5
			elif location == 6:
				if transition == 0:
					if branch == 0:
						target_state.PV_job_location = 7
			elif location == 7:
				if transition == 0:
					if branch == 0:
						target_state.PV_job_location = 8
				elif transition == 1:
					if branch == 0:
						target_state.PV_job_location = 7
			elif location == 8:
				if transition == 0:
					if branch == 0:
						target_state.PV_job_location = 5

# Automaton: UHF_job
class UHF_jobAutomaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [4, 1, 4, 1, 2, 1]
		self.transition_labels = [[11, 12, 41, 40], [40], [11, 12, 41, 40], [2], [13, 40], [2]]
		self.branch_counts = [[1, 1, 1, 1], [1], [1, 1, 1, 1], [1], [1, 1], [1]]
	
	def set_initial_values(self, state: State) -> None:
		state.UHF_job_location = 0
	
	def set_initial_transient_values(self, transient: Transient) -> None:
		pass
	
	def get_transient_value(self, state: State, transient_variable: str):
		location = state.UHF_job_location
		return None
	
	def get_transition_count(self, state: State) -> int:
		return self.transition_counts[state.UHF_job_location]
	
	def get_transition_label(self, state: State, transition: int) -> int:
		return self.transition_labels[state.UHF_job_location][transition]
	
	def get_guard_value(self, state: State, transition: int) -> bool:
		location = state.UHF_job_location
		if location == 1 or location == 3 or location == 5:
			return True
		elif location == 0:
			if transition >= 0 and transition < 2:
				return ((state.clk >= (self.network._get_transient_value(state, "UHF_data"))[state.UHF_i]) and (state.UHF_i <= 21))
			elif transition == 2:
				return (state.UHF_i > 21)
			elif transition == 3:
				return (state.clk < (self.network._get_transient_value(state, "UHF_data"))[state.UHF_i])
		elif location == 2:
			if transition >= 0 and transition < 2:
				return ((state.clk >= (self.network._get_transient_value(state, "UHF_data"))[state.UHF_i]) and (state.UHF_i <= 21))
			elif transition == 2:
				return (state.UHF_i > 21)
			elif transition == 3:
				return (state.clk < (self.network._get_transient_value(state, "UHF_data"))[state.UHF_i])
		elif location == 4:
			if transition == 0:
				return (state.clk >= (self.network._get_transient_value(state, "UHF_data"))[state.UHF_i])
			elif transition == 1:
				return (state.clk < (self.network._get_transient_value(state, "UHF_data"))[state.UHF_i])
	
	def get_branch_count(self, state: State, transition: int) -> int:
		return self.branch_counts[state.UHF_job_location][transition]
	
	def get_probability_value(self, state: State, transition: int, branch: int) -> float:
		location = state.UHF_job_location
		if location == 0:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			elif transition == 3:
				return 1
		elif location == 1:
			if transition == 0:
				return 1
		elif location == 2:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			elif transition == 3:
				return 1
		elif location == 3:
			if transition == 0:
				return 1
		elif location == 4:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
		elif location == 5:
			if transition == 0:
				return 1
	
	def jump(self, state: State, transient: Transient, transition: int, branch: int, assignment_index: int, target_state: State, target_transient: Transient) -> None:
		if assignment_index == 0:
			location = state.UHF_job_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.UHF_i = (state.UHF_i + 1)
						if target_state.UHF_i > 22:
							raise OverflowError("Assigned value of " + str(target_state.UHF_i) + " is greater than the upper bound of 22 for variable \"UHF_i\".")
						target_state.last_a_time = state.current_a_time
						target_state.current_a_time = (transient.UHF_data)[state.UHF_i]
				elif transition == 1:
					if branch == 0:
						target_state.UHF_i = (state.UHF_i + 2)
						if target_state.UHF_i > 22:
							raise OverflowError("Assigned value of " + str(target_state.UHF_i) + " is greater than the upper bound of 22 for variable \"UHF_i\".")
						target_transient.cost = 1000
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.UHF_i = (state.UHF_i + 1)
						if target_state.UHF_i > 22:
							raise OverflowError("Assigned value of " + str(target_state.UHF_i) + " is greater than the upper bound of 22 for variable \"UHF_i\".")
						target_state.last_a_time = state.current_a_time
						target_state.current_a_time = (transient.UHF_data)[state.UHF_i]
				elif transition == 1:
					if branch == 0:
						target_state.UHF_i = (state.UHF_i + 2)
						if target_state.UHF_i > 22:
							raise OverflowError("Assigned value of " + str(target_state.UHF_i) + " is greater than the upper bound of 22 for variable \"UHF_i\".")
						target_transient.cost = 1000
			elif location == 3:
				if transition == 0:
					if branch == 0:
						target_state.load = (state.load + 157800)
						if target_state.load > 1200000:
							raise OverflowError("Assigned value of " + str(target_state.load) + " is greater than the upper bound of 1200000 for variable \"load\".")
			elif location == 4:
				if transition == 0:
					if branch == 0:
						target_state.UHF_i = (state.UHF_i + 1)
						if target_state.UHF_i > 22:
							raise OverflowError("Assigned value of " + str(target_state.UHF_i) + " is greater than the upper bound of 22 for variable \"UHF_i\".")
						target_state.last_a_time = state.current_a_time
						target_state.current_a_time = (transient.UHF_data)[state.UHF_i]
			elif location == 5:
				if transition == 0:
					if branch == 0:
						target_state.load = (state.load - 157800)
						if target_state.load < -1200000:
							raise OverflowError("Assigned value of " + str(target_state.load) + " is less than the lower bound of -1200000 for variable \"load\".")
		elif assignment_index == 2:
			location = state.UHF_job_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.UHF_job_location = 3
				elif transition == 1:
					if branch == 0:
						target_state.UHF_job_location = 2
				elif transition == 2:
					if branch == 0:
						target_state.UHF_job_location = 1
				elif transition == 3:
					if branch == 0:
						target_state.UHF_job_location = 0
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.UHF_job_location = 1
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.UHF_job_location = 3
				elif transition == 1:
					if branch == 0:
						target_state.UHF_job_location = 2
				elif transition == 2:
					if branch == 0:
						target_state.UHF_job_location = 1
				elif transition == 3:
					if branch == 0:
						target_state.UHF_job_location = 2
			elif location == 3:
				if transition == 0:
					if branch == 0:
						target_state.UHF_job_location = 4
			elif location == 4:
				if transition == 0:
					if branch == 0:
						target_state.UHF_job_location = 5
				elif transition == 1:
					if branch == 0:
						target_state.UHF_job_location = 4
			elif location == 5:
				if transition == 0:
					if branch == 0:
						target_state.UHF_job_location = 2

# Automaton: L_X_Scheduler
class L_X_SchedulerAutomaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [11, 2, 11, 3, 1, 1, 2, 1, 2, 1, 2, 1, 2, 2, 2, 2, 2, 3, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1]
		self.transition_labels = [[14, 14, 15, 15, 16, 16, 16, 17, 17, 17, 18], [19, 40], [14, 14, 15, 15, 16, 16, 16, 17, 17, 17, 18], [20, 41, 40], [40], [4], [21, 40], [4], [22, 40], [4], [23, 40], [4], [24, 41], [25, 41], [26, 41], [27, 41], [24, 41], [28, 41, 40], [3], [29, 40], [3], [30, 40], [3], [31, 40], [3], [32, 41, 40], [6], [33, 40], [6], [34, 40], [6], [35, 40], [6], [36, 41, 40], [5], [37, 40], [5], [38, 40], [5], [39, 40], [5]]
		self.branch_counts = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1], [1], [1], [1, 1], [1], [1, 1], [1], [1, 1], [1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1, 1], [1], [1, 1], [1], [1, 1], [1], [1, 1], [1], [1, 1, 1], [1], [1, 1], [1], [1, 1], [1], [1, 1], [1], [1, 1, 1], [1], [1, 1], [1], [1, 1], [1], [1, 1], [1]]
	
	def set_initial_values(self, state: State) -> None:
		state.L_X_Scheduler_location = 0
		state.sched_clk = 0
	
	def set_initial_transient_values(self, transient: Transient) -> None:
		pass
	
	def get_transient_value(self, state: State, transient_variable: str):
		location = state.L_X_Scheduler_location
		return None
	
	def get_transition_count(self, state: State) -> int:
		return self.transition_counts[state.L_X_Scheduler_location]
	
	def get_transition_label(self, state: State, transition: int) -> int:
		return self.transition_labels[state.L_X_Scheduler_location][transition]
	
	def get_guard_value(self, state: State, transition: int) -> bool:
		location = state.L_X_Scheduler_location
		if location == 4 or location == 5 or location == 7 or location == 9 or location == 11 or location == 18 or location == 20 or location == 22 or location == 24 or location == 26 or location == 28 or location == 30 or location == 32 or location == 34 or location == 36 or location == 38 or location == 40:
			return True
		elif location == 0:
			if transition == 0:
				return ((((state.clk >= (((self.network._get_transient_value(state, "L_Band_Inmarsat_3F2_data"))[state.L_3F2_i] - 40) - 600)) and (state.L_3F2_i <= 75)) and ((state.L_X_counter)[5] >= 2)) and ((state.L_X_counter)[4] < 1))
			elif transition == 1:
				return ((((state.clk >= (((self.network._get_transient_value(state, "L_Band_Inmarsat_3F2_data"))[state.L_3F2_i] - 40) - 600)) and (state.L_3F2_i <= 75)) and ((state.L_X_counter)[5] < 2)) and ((state.L_X_counter)[4] < 1))
			elif transition == 2:
				return ((((state.clk >= (((self.network._get_transient_value(state, "L_Band_Inmarsat_3F3_data"))[state.L_3F3_i] - 40) - 600)) and (state.L_3F3_i <= 77)) and ((state.L_X_counter)[5] >= 2)) and ((state.L_X_counter)[4] < 1))
			elif transition == 3:
				return ((((state.clk >= (((self.network._get_transient_value(state, "L_Band_Inmarsat_3F3_data"))[state.L_3F3_i] - 40) - 600)) and (state.L_3F3_i <= 77)) and ((state.L_X_counter)[5] < 2)) and ((state.L_X_counter)[4] < 1))
			elif transition == 4:
				return ((((state.clk >= (((self.network._get_transient_value(state, "X_Band_Kourou_data"))[state.X_Kourou_i] - 20) - 600)) and (state.X_Kourou_i <= 19)) and ((state.L_X_counter)[5] < 1)) and ((state.L_X_counter)[4] > 0))
			elif transition == 5:
				return ((((state.clk >= (((self.network._get_transient_value(state, "X_Band_Kourou_data"))[state.X_Kourou_i] - 20) - 600)) and (state.X_Kourou_i <= 19)) and ((state.L_X_counter)[5] >= 1)) and ((state.L_X_counter)[4] > 0))
			elif transition == 6:
				return ((((state.clk >= (((self.network._get_transient_value(state, "X_Band_Kourou_data"))[state.X_Kourou_i] - 20) - 600)) and (state.X_Kourou_i <= 19)) and ((state.L_X_counter)[5] >= 2)) and ((state.L_X_counter)[4] > 0))
			elif transition == 7:
				return ((((state.clk >= (((self.network._get_transient_value(state, "X_Band_Toulouse_data"))[state.X_Toulouse_i] - 20) - 600)) and (state.X_Toulouse_i <= 27)) and ((state.L_X_counter)[5] < 1)) and ((state.L_X_counter)[4] > 0))
			elif transition == 8:
				return ((((state.clk >= (((self.network._get_transient_value(state, "X_Band_Toulouse_data"))[state.X_Toulouse_i] - 20) - 600)) and (state.X_Toulouse_i <= 27)) and ((state.L_X_counter)[5] >= 1)) and ((state.L_X_counter)[4] > 0))
			elif transition == 9:
				return ((((state.clk >= (((self.network._get_transient_value(state, "X_Band_Toulouse_data"))[state.X_Toulouse_i] - 20) - 600)) and (state.X_Toulouse_i <= 27)) and ((state.L_X_counter)[5] >= 2)) and ((state.L_X_counter)[4] > 0))
			elif transition == 10:
				return ((((state.L_3F2_i <= 75) or (state.L_3F3_i <= 77)) or (state.X_Kourou_i <= 19)) or (state.X_Toulouse_i <= 27))
		elif location == 1:
			if transition == 0:
				return (state.sched_clk >= 600)
			elif transition == 1:
				return (state.sched_clk < 600)
		elif location == 2:
			if transition == 0:
				return ((((state.clk >= (((self.network._get_transient_value(state, "L_Band_Inmarsat_3F2_data"))[state.L_3F2_i] - 40) - 600)) and (state.L_3F2_i <= 75)) and ((state.L_X_counter)[5] >= 2)) and ((state.L_X_counter)[4] < 1))
			elif transition == 1:
				return ((((state.clk >= (((self.network._get_transient_value(state, "L_Band_Inmarsat_3F2_data"))[state.L_3F2_i] - 40) - 600)) and (state.L_3F2_i <= 75)) and ((state.L_X_counter)[5] < 2)) and ((state.L_X_counter)[4] < 1))
			elif transition == 2:
				return ((((state.clk >= (((self.network._get_transient_value(state, "L_Band_Inmarsat_3F3_data"))[state.L_3F3_i] - 40) - 600)) and (state.L_3F3_i <= 77)) and ((state.L_X_counter)[5] >= 2)) and ((state.L_X_counter)[4] < 1))
			elif transition == 3:
				return ((((state.clk >= (((self.network._get_transient_value(state, "L_Band_Inmarsat_3F3_data"))[state.L_3F3_i] - 40) - 600)) and (state.L_3F3_i <= 77)) and ((state.L_X_counter)[5] < 2)) and ((state.L_X_counter)[4] < 1))
			elif transition == 4:
				return ((((state.clk >= (((self.network._get_transient_value(state, "X_Band_Kourou_data"))[state.X_Kourou_i] - 20) - 600)) and (state.X_Kourou_i <= 19)) and ((state.L_X_counter)[5] < 1)) and ((state.L_X_counter)[4] > 0))
			elif transition == 5:
				return ((((state.clk >= (((self.network._get_transient_value(state, "X_Band_Kourou_data"))[state.X_Kourou_i] - 20) - 600)) and (state.X_Kourou_i <= 19)) and ((state.L_X_counter)[5] >= 1)) and ((state.L_X_counter)[4] > 0))
			elif transition == 6:
				return ((((state.clk >= (((self.network._get_transient_value(state, "X_Band_Kourou_data"))[state.X_Kourou_i] - 20) - 600)) and (state.X_Kourou_i <= 19)) and ((state.L_X_counter)[5] >= 2)) and ((state.L_X_counter)[4] > 0))
			elif transition == 7:
				return ((((state.clk >= (((self.network._get_transient_value(state, "X_Band_Toulouse_data"))[state.X_Toulouse_i] - 20) - 600)) and (state.X_Toulouse_i <= 27)) and ((state.L_X_counter)[5] < 1)) and ((state.L_X_counter)[4] > 0))
			elif transition == 8:
				return ((((state.clk >= (((self.network._get_transient_value(state, "X_Band_Toulouse_data"))[state.X_Toulouse_i] - 20) - 600)) and (state.X_Toulouse_i <= 27)) and ((state.L_X_counter)[5] >= 1)) and ((state.L_X_counter)[4] > 0))
			elif transition == 9:
				return ((((state.clk >= (((self.network._get_transient_value(state, "X_Band_Toulouse_data"))[state.X_Toulouse_i] - 20) - 600)) and (state.X_Toulouse_i <= 27)) and ((state.L_X_counter)[5] >= 2)) and ((state.L_X_counter)[4] > 0))
			elif transition == 10:
				return ((((state.L_3F2_i <= 75) or (state.L_3F3_i <= 77)) or (state.X_Kourou_i <= 19)) or (state.X_Toulouse_i <= 27))
		elif location == 3:
			if transition == 0:
				return ((state.clk >= ((self.network._get_transient_value(state, "X_Band_Toulouse_data"))[state.X_Toulouse_i] - 20)) and (state.X_Toulouse_i <= 27))
			elif transition == 1:
				return (state.X_Toulouse_i > 27)
			elif transition == 2:
				return (state.clk < ((self.network._get_transient_value(state, "X_Band_Toulouse_data"))[state.X_Toulouse_i] - 20))
		elif location == 6:
			if transition == 0:
				return (state.job_clk >= 20)
			elif transition == 1:
				return (state.job_clk < 20)
		elif location == 8:
			if transition == 0:
				return (state.clk >= (self.network._get_transient_value(state, "X_Band_Toulouse_data"))[state.X_Toulouse_i])
			elif transition == 1:
				return (state.clk < (self.network._get_transient_value(state, "X_Band_Toulouse_data"))[state.X_Toulouse_i])
		elif location == 10:
			if transition == 0:
				return (state.job_clk >= 10)
			elif transition == 1:
				return (state.job_clk < 10)
		elif location == 12:
			if transition == 0:
				return ((state.clk >= ((self.network._get_transient_value(state, "L_Band_Inmarsat_3F2_data"))[state.L_3F2_i] - 40)) and (state.L_3F2_i <= 75))
			elif transition == 1:
				return ((state.clk <= ((self.network._get_transient_value(state, "L_Band_Inmarsat_3F2_data"))[state.L_3F2_i] - 40)) and (state.L_3F2_i <= 75))
		elif location == 13:
			if transition == 0:
				return ((state.clk >= ((self.network._get_transient_value(state, "L_Band_Inmarsat_3F3_data"))[state.L_3F3_i] - 40)) and (state.L_3F3_i <= 77))
			elif transition == 1:
				return ((state.clk <= ((self.network._get_transient_value(state, "L_Band_Inmarsat_3F3_data"))[state.L_3F3_i] - 40)) and (state.L_3F3_i <= 77))
		elif location == 14:
			if transition == 0:
				return ((state.clk >= ((self.network._get_transient_value(state, "X_Band_Kourou_data"))[state.X_Kourou_i] - 20)) and (state.X_Kourou_i <= 19))
			elif transition == 1:
				return ((state.clk <= ((self.network._get_transient_value(state, "X_Band_Kourou_data"))[state.X_Kourou_i] - 20)) and (state.X_Kourou_i <= 19))
		elif location == 15:
			if transition == 0:
				return ((state.clk >= ((self.network._get_transient_value(state, "X_Band_Toulouse_data"))[state.X_Toulouse_i] - 20)) and (state.X_Toulouse_i <= 27))
			elif transition == 1:
				return ((state.clk <= ((self.network._get_transient_value(state, "X_Band_Toulouse_data"))[state.X_Toulouse_i] - 20)) and (state.X_Toulouse_i <= 27))
		elif location == 16:
			if transition == 0:
				return ((state.clk >= ((self.network._get_transient_value(state, "L_Band_Inmarsat_3F2_data"))[state.L_3F2_i] - 40)) and (state.L_3F2_i <= 75))
			elif transition == 1:
				return ((state.clk <= ((self.network._get_transient_value(state, "L_Band_Inmarsat_3F2_data"))[state.L_3F2_i] - 40)) and (state.L_3F2_i <= 75))
		elif location == 17:
			if transition == 0:
				return ((state.clk >= ((self.network._get_transient_value(state, "X_Band_Kourou_data"))[state.X_Kourou_i] - 20)) and (state.X_Kourou_i <= 19))
			elif transition == 1:
				return (state.X_Kourou_i > 19)
			elif transition == 2:
				return (state.clk < ((self.network._get_transient_value(state, "X_Band_Kourou_data"))[state.X_Kourou_i] - 20))
		elif location == 19:
			if transition == 0:
				return (state.job_clk >= 20)
			elif transition == 1:
				return (state.job_clk < 20)
		elif location == 21:
			if transition == 0:
				return (state.clk >= (self.network._get_transient_value(state, "X_Band_Kourou_data"))[state.X_Kourou_i])
			elif transition == 1:
				return (state.clk < (self.network._get_transient_value(state, "X_Band_Kourou_data"))[state.X_Kourou_i])
		elif location == 23:
			if transition == 0:
				return (state.job_clk >= 10)
			elif transition == 1:
				return (state.job_clk < 10)
		elif location == 25:
			if transition == 0:
				return ((state.clk >= ((self.network._get_transient_value(state, "L_Band_Inmarsat_3F3_data"))[state.L_3F3_i] - 40)) and (state.L_3F3_i <= 77))
			elif transition == 1:
				return (state.L_3F3_i > 77)
			elif transition == 2:
				return (state.clk < ((self.network._get_transient_value(state, "L_Band_Inmarsat_3F3_data"))[state.L_3F3_i] - 40))
		elif location == 27:
			if transition == 0:
				return (state.job_clk >= 40)
			elif transition == 1:
				return (state.job_clk < 40)
		elif location == 29:
			if transition == 0:
				return (state.clk >= (self.network._get_transient_value(state, "L_Band_Inmarsat_3F3_data"))[state.L_3F3_i])
			elif transition == 1:
				return (state.clk < (self.network._get_transient_value(state, "L_Band_Inmarsat_3F3_data"))[state.L_3F3_i])
		elif location == 31:
			if transition == 0:
				return (state.job_clk >= 10)
			elif transition == 1:
				return (state.job_clk < 10)
		elif location == 33:
			if transition == 0:
				return ((state.clk >= ((self.network._get_transient_value(state, "L_Band_Inmarsat_3F2_data"))[state.L_3F2_i] - 40)) and (state.L_3F2_i <= 75))
			elif transition == 1:
				return (state.L_3F2_i > 75)
			elif transition == 2:
				return (state.clk < ((self.network._get_transient_value(state, "L_Band_Inmarsat_3F2_data"))[state.L_3F2_i] - 40))
		elif location == 35:
			if transition == 0:
				return (state.job_clk >= 40)
			elif transition == 1:
				return (state.job_clk < 40)
		elif location == 37:
			if transition == 0:
				return (state.clk >= (self.network._get_transient_value(state, "L_Band_Inmarsat_3F2_data"))[state.L_3F2_i])
			elif transition == 1:
				return (state.clk < (self.network._get_transient_value(state, "L_Band_Inmarsat_3F2_data"))[state.L_3F2_i])
		elif location == 39:
			if transition == 0:
				return (state.job_clk >= 10)
			elif transition == 1:
				return (state.job_clk < 10)
	
	def get_branch_count(self, state: State, transition: int) -> int:
		return self.branch_counts[state.L_X_Scheduler_location][transition]
	
	def get_probability_value(self, state: State, transition: int, branch: int) -> float:
		location = state.L_X_Scheduler_location
		if location == 0:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			elif transition == 3:
				return 1
			elif transition == 4:
				return 1
			elif transition == 5:
				return 1
			elif transition == 6:
				return 1
			elif transition == 7:
				return 1
			elif transition == 8:
				return 1
			elif transition == 9:
				return 1
			elif transition == 10:
				return 1
		elif location == 1:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
		elif location == 2:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
			elif transition == 3:
				return 1
			elif transition == 4:
				return 1
			elif transition == 5:
				return 1
			elif transition == 6:
				return 1
			elif transition == 7:
				return 1
			elif transition == 8:
				return 1
			elif transition == 9:
				return 1
			elif transition == 10:
				return 1
		elif location == 3:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
		elif location == 4:
			if transition == 0:
				return 1
		elif location == 5:
			if transition == 0:
				return 1
		elif location == 6:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
		elif location == 7:
			if transition == 0:
				return 1
		elif location == 8:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
		elif location == 9:
			if transition == 0:
				return 1
		elif location == 10:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
		elif location == 11:
			if transition == 0:
				return 1
		elif location == 12:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
		elif location == 13:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
		elif location == 14:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
		elif location == 15:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
		elif location == 16:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
		elif location == 17:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
		elif location == 18:
			if transition == 0:
				return 1
		elif location == 19:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
		elif location == 20:
			if transition == 0:
				return 1
		elif location == 21:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
		elif location == 22:
			if transition == 0:
				return 1
		elif location == 23:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
		elif location == 24:
			if transition == 0:
				return 1
		elif location == 25:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
		elif location == 26:
			if transition == 0:
				return 1
		elif location == 27:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
		elif location == 28:
			if transition == 0:
				return 1
		elif location == 29:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
		elif location == 30:
			if transition == 0:
				return 1
		elif location == 31:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
		elif location == 32:
			if transition == 0:
				return 1
		elif location == 33:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
		elif location == 34:
			if transition == 0:
				return 1
		elif location == 35:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
		elif location == 36:
			if transition == 0:
				return 1
		elif location == 37:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
		elif location == 38:
			if transition == 0:
				return 1
		elif location == 39:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
		elif location == 40:
			if transition == 0:
				return 1
	
	def jump(self, state: State, transient: Transient, transition: int, branch: int, assignment_index: int, target_state: State, target_transient: Transient) -> None:
		if assignment_index == 0:
			location = state.L_X_Scheduler_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.L_X_counter[5] = 0
						target_state.L_X_counter[4] = ((state.L_X_counter)[4] + 1)
						target_state.L_X_counter[0] = ((state.L_X_counter)[0] + 1)
						target_transient.cost = (state.L_X_counter)[0]
				elif transition == 1:
					if branch == 0:
						target_state.L_X_counter[5] = 0
						target_state.L_X_counter[4] = ((state.L_X_counter)[4] + 1)
						target_state.L_X_counter[0] = ((state.L_X_counter)[0] + 1)
						target_transient.cost = (1000 + (state.L_X_counter)[0])
				elif transition == 2:
					if branch == 0:
						target_state.L_X_counter[5] = 0
						target_state.L_X_counter[4] = ((state.L_X_counter)[4] + 1)
						target_state.L_X_counter[1] = ((state.L_X_counter)[1] + 1)
						target_transient.cost = (state.L_X_counter)[1]
				elif transition == 3:
					if branch == 0:
						target_state.L_X_counter[5] = 0
						target_state.L_X_counter[4] = ((state.L_X_counter)[4] + 1)
						target_state.L_X_counter[1] = ((state.L_X_counter)[1] + 1)
						target_transient.cost = (1000 + (state.L_X_counter)[1])
				elif transition == 4:
					if branch == 0:
						target_state.L_X_counter[5] = ((state.L_X_counter)[5] + 1)
						target_state.L_X_counter[2] = ((state.L_X_counter)[2] + 1)
						target_transient.cost = (state.L_X_counter)[2]
				elif transition == 5:
					if branch == 0:
						target_state.L_X_counter[5] = ((state.L_X_counter)[5] + 1)
						target_state.L_X_counter[4] = 0
						target_state.L_X_counter[2] = ((state.L_X_counter)[2] + 1)
						target_transient.cost = (state.L_X_counter)[2]
				elif transition == 6:
					if branch == 0:
						target_state.L_X_counter[5] = ((state.L_X_counter)[5] + 1)
						target_state.L_X_counter[4] = 0
						target_state.L_X_counter[2] = ((state.L_X_counter)[2] + 1)
						target_transient.cost = (1000 + (state.L_X_counter)[2])
				elif transition == 7:
					if branch == 0:
						target_state.L_X_counter[5] = ((state.L_X_counter)[5] + 1)
						target_state.L_X_counter[3] = ((state.L_X_counter)[3] + 1)
						target_transient.cost = (state.L_X_counter)[3]
				elif transition == 8:
					if branch == 0:
						target_state.L_X_counter[5] = ((state.L_X_counter)[5] + 1)
						target_state.L_X_counter[4] = 0
						target_state.L_X_counter[3] = ((state.L_X_counter)[3] + 1)
						target_transient.cost = (state.L_X_counter)[3]
				elif transition == 9:
					if branch == 0:
						target_state.L_X_counter[5] = ((state.L_X_counter)[5] + 1)
						target_state.L_X_counter[4] = 0
						target_state.L_X_counter[3] = ((state.L_X_counter)[3] + 1)
						target_transient.cost = (1000 + (state.L_X_counter)[3])
				elif transition == 10:
					if branch == 0:
						target_transient.cost = 1000
						target_state.sched_clk = 0
			elif location == 1:
				if transition == 1:
					if branch == 0:
						target_state.sched_clk = min((state.sched_clk + 1), 601)
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.L_X_counter[5] = 0
						target_state.L_X_counter[4] = ((state.L_X_counter)[4] + 1)
						target_state.L_X_counter[0] = ((state.L_X_counter)[0] + 1)
						target_transient.cost = (state.L_X_counter)[0]
				elif transition == 1:
					if branch == 0:
						target_state.L_X_counter[5] = 0
						target_state.L_X_counter[4] = ((state.L_X_counter)[4] + 1)
						target_state.L_X_counter[0] = ((state.L_X_counter)[0] + 1)
						target_transient.cost = (1000 + (state.L_X_counter)[0])
				elif transition == 2:
					if branch == 0:
						target_state.L_X_counter[5] = 0
						target_state.L_X_counter[4] = ((state.L_X_counter)[4] + 1)
						target_state.L_X_counter[1] = ((state.L_X_counter)[1] + 1)
						target_transient.cost = (state.L_X_counter)[1]
				elif transition == 3:
					if branch == 0:
						target_state.L_X_counter[5] = 0
						target_state.L_X_counter[4] = ((state.L_X_counter)[4] + 1)
						target_state.L_X_counter[1] = ((state.L_X_counter)[1] + 1)
						target_transient.cost = (1000 + (state.L_X_counter)[1])
				elif transition == 4:
					if branch == 0:
						target_state.L_X_counter[5] = ((state.L_X_counter)[5] + 1)
						target_state.L_X_counter[2] = ((state.L_X_counter)[2] + 1)
						target_transient.cost = (state.L_X_counter)[2]
				elif transition == 5:
					if branch == 0:
						target_state.L_X_counter[5] = ((state.L_X_counter)[5] + 1)
						target_state.L_X_counter[4] = 0
						target_state.L_X_counter[2] = ((state.L_X_counter)[2] + 1)
						target_transient.cost = (state.L_X_counter)[2]
				elif transition == 6:
					if branch == 0:
						target_state.L_X_counter[5] = ((state.L_X_counter)[5] + 1)
						target_state.L_X_counter[4] = 0
						target_state.L_X_counter[2] = ((state.L_X_counter)[2] + 1)
						target_transient.cost = (1000 + (state.L_X_counter)[2])
				elif transition == 7:
					if branch == 0:
						target_state.L_X_counter[5] = ((state.L_X_counter)[5] + 1)
						target_state.L_X_counter[3] = ((state.L_X_counter)[3] + 1)
						target_transient.cost = (state.L_X_counter)[3]
				elif transition == 8:
					if branch == 0:
						target_state.L_X_counter[5] = ((state.L_X_counter)[5] + 1)
						target_state.L_X_counter[4] = 0
						target_state.L_X_counter[3] = ((state.L_X_counter)[3] + 1)
						target_transient.cost = (state.L_X_counter)[3]
				elif transition == 9:
					if branch == 0:
						target_state.L_X_counter[5] = ((state.L_X_counter)[5] + 1)
						target_state.L_X_counter[4] = 0
						target_state.L_X_counter[3] = ((state.L_X_counter)[3] + 1)
						target_transient.cost = (1000 + (state.L_X_counter)[3])
				elif transition == 10:
					if branch == 0:
						target_transient.cost = 1000
						target_state.sched_clk = 0
			elif location == 3:
				if transition == 0:
					if branch == 0:
						target_state.last_a_time = state.current_a_time
						target_state.current_a_time = ((transient.X_Band_Toulouse_data)[state.X_Toulouse_i] - 20)
						if target_state.current_a_time < 0:
							raise OverflowError("Assigned value of " + str(target_state.current_a_time) + " is less than the lower bound of 0 for variable \"current_a_time\".")
						target_state.job_clk = 0
						target_state.X_Toulouse_i = (state.X_Toulouse_i + 1)
						if target_state.X_Toulouse_i > 28:
							raise OverflowError("Assigned value of " + str(target_state.X_Toulouse_i) + " is greater than the upper bound of 28 for variable \"X_Toulouse_i\".")
			elif location == 5:
				if transition == 0:
					if branch == 0:
						target_state.load = (state.load + 24840)
						if target_state.load > 1200000:
							raise OverflowError("Assigned value of " + str(target_state.load) + " is greater than the upper bound of 1200000 for variable \"load\".")
			elif location == 6:
				if transition == 0:
					if branch == 0:
						target_state.last_a_time = state.current_a_time
						target_state.current_a_time = (state.current_a_time + 20)
						if target_state.current_a_time > 4320:
							raise OverflowError("Assigned value of " + str(target_state.current_a_time) + " is greater than the upper bound of 4320 for variable \"current_a_time\".")
						target_state.job_clk = 0
			elif location == 7:
				if transition == 0:
					if branch == 0:
						target_state.load = (state.load + 691860)
						if target_state.load > 1200000:
							raise OverflowError("Assigned value of " + str(target_state.load) + " is greater than the upper bound of 1200000 for variable \"load\".")
			elif location == 8:
				if transition == 0:
					if branch == 0:
						target_state.last_a_time = state.current_a_time
						target_state.current_a_time = (transient.X_Band_Toulouse_data)[state.X_Toulouse_i]
						target_state.job_clk = 0
						target_state.X_Toulouse_i = (state.X_Toulouse_i + 1)
						if target_state.X_Toulouse_i > 28:
							raise OverflowError("Assigned value of " + str(target_state.X_Toulouse_i) + " is greater than the upper bound of 28 for variable \"X_Toulouse_i\".")
			elif location == 9:
				if transition == 0:
					if branch == 0:
						target_state.load = (state.load - 691860)
						if target_state.load < -1200000:
							raise OverflowError("Assigned value of " + str(target_state.load) + " is less than the lower bound of -1200000 for variable \"load\".")
			elif location == 10:
				if transition == 0:
					if branch == 0:
						target_state.last_a_time = state.current_a_time
						target_state.current_a_time = (state.current_a_time + 10)
						if target_state.current_a_time > 4320:
							raise OverflowError("Assigned value of " + str(target_state.current_a_time) + " is greater than the upper bound of 4320 for variable \"current_a_time\".")
			elif location == 11:
				if transition == 0:
					if branch == 0:
						target_state.load = (state.load - 24840)
						if target_state.load < -1200000:
							raise OverflowError("Assigned value of " + str(target_state.load) + " is less than the lower bound of -1200000 for variable \"load\".")
			elif location == 12:
				if transition == 0:
					if branch == 0:
						target_state.L_3F2_i = (state.L_3F2_i + 2)
						if target_state.L_3F2_i > 76:
							raise OverflowError("Assigned value of " + str(target_state.L_3F2_i) + " is greater than the upper bound of 76 for variable \"L_3F2_i\".")
			elif location == 13:
				if transition == 0:
					if branch == 0:
						target_state.L_3F3_i = (state.L_3F3_i + 2)
						if target_state.L_3F3_i > 78:
							raise OverflowError("Assigned value of " + str(target_state.L_3F3_i) + " is greater than the upper bound of 78 for variable \"L_3F3_i\".")
			elif location == 14:
				if transition == 0:
					if branch == 0:
						target_state.X_Kourou_i = (state.X_Kourou_i + 2)
						if target_state.X_Kourou_i > 20:
							raise OverflowError("Assigned value of " + str(target_state.X_Kourou_i) + " is greater than the upper bound of 20 for variable \"X_Kourou_i\".")
			elif location == 15:
				if transition == 0:
					if branch == 0:
						target_state.X_Toulouse_i = (state.X_Toulouse_i + 2)
						if target_state.X_Toulouse_i > 28:
							raise OverflowError("Assigned value of " + str(target_state.X_Toulouse_i) + " is greater than the upper bound of 28 for variable \"X_Toulouse_i\".")
			elif location == 16:
				if transition == 0:
					if branch == 0:
						target_state.L_3F2_i = (state.L_3F2_i + 2)
						if target_state.L_3F2_i > 76:
							raise OverflowError("Assigned value of " + str(target_state.L_3F2_i) + " is greater than the upper bound of 76 for variable \"L_3F2_i\".")
			elif location == 17:
				if transition == 0:
					if branch == 0:
						target_state.last_a_time = state.current_a_time
						target_state.current_a_time = ((transient.X_Band_Kourou_data)[state.X_Kourou_i] - 20)
						if target_state.current_a_time < 0:
							raise OverflowError("Assigned value of " + str(target_state.current_a_time) + " is less than the lower bound of 0 for variable \"current_a_time\".")
						target_state.job_clk = 0
						target_state.X_Kourou_i = (state.X_Kourou_i + 1)
						if target_state.X_Kourou_i > 20:
							raise OverflowError("Assigned value of " + str(target_state.X_Kourou_i) + " is greater than the upper bound of 20 for variable \"X_Kourou_i\".")
			elif location == 18:
				if transition == 0:
					if branch == 0:
						target_state.load = (state.load + 24840)
						if target_state.load > 1200000:
							raise OverflowError("Assigned value of " + str(target_state.load) + " is greater than the upper bound of 1200000 for variable \"load\".")
			elif location == 19:
				if transition == 0:
					if branch == 0:
						target_state.last_a_time = state.current_a_time
						target_state.current_a_time = (state.current_a_time + 20)
						if target_state.current_a_time > 4320:
							raise OverflowError("Assigned value of " + str(target_state.current_a_time) + " is greater than the upper bound of 4320 for variable \"current_a_time\".")
						target_state.job_clk = 0
			elif location == 20:
				if transition == 0:
					if branch == 0:
						target_state.load = (state.load + 691860)
						if target_state.load > 1200000:
							raise OverflowError("Assigned value of " + str(target_state.load) + " is greater than the upper bound of 1200000 for variable \"load\".")
			elif location == 21:
				if transition == 0:
					if branch == 0:
						target_state.last_a_time = state.current_a_time
						target_state.current_a_time = (transient.X_Band_Kourou_data)[state.X_Kourou_i]
						target_state.job_clk = 0
						target_state.X_Kourou_i = (state.X_Kourou_i + 1)
						if target_state.X_Kourou_i > 20:
							raise OverflowError("Assigned value of " + str(target_state.X_Kourou_i) + " is greater than the upper bound of 20 for variable \"X_Kourou_i\".")
			elif location == 22:
				if transition == 0:
					if branch == 0:
						target_state.load = (state.load - 691860)
						if target_state.load < -1200000:
							raise OverflowError("Assigned value of " + str(target_state.load) + " is less than the lower bound of -1200000 for variable \"load\".")
			elif location == 23:
				if transition == 0:
					if branch == 0:
						target_state.last_a_time = state.current_a_time
						target_state.current_a_time = (state.current_a_time + 10)
						if target_state.current_a_time > 4320:
							raise OverflowError("Assigned value of " + str(target_state.current_a_time) + " is greater than the upper bound of 4320 for variable \"current_a_time\".")
			elif location == 24:
				if transition == 0:
					if branch == 0:
						target_state.load = (state.load - 24840)
						if target_state.load < -1200000:
							raise OverflowError("Assigned value of " + str(target_state.load) + " is less than the lower bound of -1200000 for variable \"load\".")
			elif location == 25:
				if transition == 0:
					if branch == 0:
						target_state.last_a_time = state.current_a_time
						target_state.current_a_time = ((transient.L_Band_Inmarsat_3F3_data)[state.L_3F3_i] - 40)
						if target_state.current_a_time < 0:
							raise OverflowError("Assigned value of " + str(target_state.current_a_time) + " is less than the lower bound of 0 for variable \"current_a_time\".")
						target_state.job_clk = 0
						target_state.L_3F3_i = (state.L_3F3_i + 1)
						if target_state.L_3F3_i > 78:
							raise OverflowError("Assigned value of " + str(target_state.L_3F3_i) + " is greater than the upper bound of 78 for variable \"L_3F3_i\".")
			elif location == 26:
				if transition == 0:
					if branch == 0:
						target_state.load = (state.load + 24840)
						if target_state.load > 1200000:
							raise OverflowError("Assigned value of " + str(target_state.load) + " is greater than the upper bound of 1200000 for variable \"load\".")
			elif location == 27:
				if transition == 0:
					if branch == 0:
						target_state.last_a_time = state.current_a_time
						target_state.current_a_time = (state.current_a_time + 40)
						if target_state.current_a_time > 4320:
							raise OverflowError("Assigned value of " + str(target_state.current_a_time) + " is greater than the upper bound of 4320 for variable \"current_a_time\".")
						target_state.job_clk = 0
						target_state.is_aligned = True
			elif location == 28:
				if transition == 0:
					if branch == 0:
						target_state.load = (state.load + 206940)
						if target_state.load > 1200000:
							raise OverflowError("Assigned value of " + str(target_state.load) + " is greater than the upper bound of 1200000 for variable \"load\".")
			elif location == 29:
				if transition == 0:
					if branch == 0:
						target_state.last_a_time = state.current_a_time
						target_state.current_a_time = (transient.L_Band_Inmarsat_3F3_data)[state.L_3F3_i]
						target_state.job_clk = 0
						target_state.L_3F3_i = (state.L_3F3_i + 1)
						if target_state.L_3F3_i > 78:
							raise OverflowError("Assigned value of " + str(target_state.L_3F3_i) + " is greater than the upper bound of 78 for variable \"L_3F3_i\".")
			elif location == 30:
				if transition == 0:
					if branch == 0:
						target_state.load = (state.load - 206940)
						if target_state.load < -1200000:
							raise OverflowError("Assigned value of " + str(target_state.load) + " is less than the lower bound of -1200000 for variable \"load\".")
			elif location == 31:
				if transition == 0:
					if branch == 0:
						target_state.last_a_time = state.current_a_time
						target_state.current_a_time = (state.current_a_time + 10)
						if target_state.current_a_time > 4320:
							raise OverflowError("Assigned value of " + str(target_state.current_a_time) + " is greater than the upper bound of 4320 for variable \"current_a_time\".")
						target_state.is_aligned = False
			elif location == 32:
				if transition == 0:
					if branch == 0:
						target_state.load = (state.load - 24840)
						if target_state.load < -1200000:
							raise OverflowError("Assigned value of " + str(target_state.load) + " is less than the lower bound of -1200000 for variable \"load\".")
			elif location == 33:
				if transition == 0:
					if branch == 0:
						target_state.last_a_time = state.current_a_time
						target_state.current_a_time = ((transient.L_Band_Inmarsat_3F2_data)[state.L_3F2_i] - 40)
						if target_state.current_a_time < 0:
							raise OverflowError("Assigned value of " + str(target_state.current_a_time) + " is less than the lower bound of 0 for variable \"current_a_time\".")
						target_state.job_clk = 0
						target_state.L_3F2_i = (state.L_3F2_i + 1)
						if target_state.L_3F2_i > 76:
							raise OverflowError("Assigned value of " + str(target_state.L_3F2_i) + " is greater than the upper bound of 76 for variable \"L_3F2_i\".")
			elif location == 34:
				if transition == 0:
					if branch == 0:
						target_state.load = (state.load + 24840)
						if target_state.load > 1200000:
							raise OverflowError("Assigned value of " + str(target_state.load) + " is greater than the upper bound of 1200000 for variable \"load\".")
			elif location == 35:
				if transition == 0:
					if branch == 0:
						target_state.last_a_time = state.current_a_time
						target_state.current_a_time = (state.current_a_time + 40)
						if target_state.current_a_time > 4320:
							raise OverflowError("Assigned value of " + str(target_state.current_a_time) + " is greater than the upper bound of 4320 for variable \"current_a_time\".")
						target_state.job_clk = 0
						target_state.is_aligned = True
			elif location == 36:
				if transition == 0:
					if branch == 0:
						target_state.load = (state.load + 206940)
						if target_state.load > 1200000:
							raise OverflowError("Assigned value of " + str(target_state.load) + " is greater than the upper bound of 1200000 for variable \"load\".")
			elif location == 37:
				if transition == 0:
					if branch == 0:
						target_state.last_a_time = state.current_a_time
						target_state.current_a_time = (transient.L_Band_Inmarsat_3F2_data)[state.L_3F2_i]
						target_state.job_clk = 0
						target_state.L_3F2_i = (state.L_3F2_i + 1)
						if target_state.L_3F2_i > 76:
							raise OverflowError("Assigned value of " + str(target_state.L_3F2_i) + " is greater than the upper bound of 76 for variable \"L_3F2_i\".")
			elif location == 38:
				if transition == 0:
					if branch == 0:
						target_state.load = (state.load - 206940)
						if target_state.load < -1200000:
							raise OverflowError("Assigned value of " + str(target_state.load) + " is less than the lower bound of -1200000 for variable \"load\".")
			elif location == 39:
				if transition == 0:
					if branch == 0:
						target_state.last_a_time = state.current_a_time
						target_state.current_a_time = (state.current_a_time + 10)
						if target_state.current_a_time > 4320:
							raise OverflowError("Assigned value of " + str(target_state.current_a_time) + " is greater than the upper bound of 4320 for variable \"current_a_time\".")
						target_state.is_aligned = False
			elif location == 40:
				if transition == 0:
					if branch == 0:
						target_state.load = (state.load - 24840)
						if target_state.load < -1200000:
							raise OverflowError("Assigned value of " + str(target_state.load) + " is less than the lower bound of -1200000 for variable \"load\".")
		elif assignment_index == 2:
			location = state.L_X_Scheduler_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.L_X_Scheduler_location = 33
				elif transition == 1:
					if branch == 0:
						target_state.L_X_Scheduler_location = 33
				elif transition == 2:
					if branch == 0:
						target_state.L_X_Scheduler_location = 25
				elif transition == 3:
					if branch == 0:
						target_state.L_X_Scheduler_location = 25
				elif transition == 4:
					if branch == 0:
						target_state.L_X_Scheduler_location = 17
				elif transition == 5:
					if branch == 0:
						target_state.L_X_Scheduler_location = 17
				elif transition == 6:
					if branch == 0:
						target_state.L_X_Scheduler_location = 17
				elif transition == 7:
					if branch == 0:
						target_state.L_X_Scheduler_location = 3
				elif transition == 8:
					if branch == 0:
						target_state.L_X_Scheduler_location = 3
				elif transition == 9:
					if branch == 0:
						target_state.L_X_Scheduler_location = 3
				elif transition == 10:
					if branch == 0:
						target_state.L_X_Scheduler_location = 1
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.sched_clk = 0
						target_state.L_X_Scheduler_location = 2
				elif transition == 1:
					if branch == 0:
						target_state.L_X_Scheduler_location = 1
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.L_X_Scheduler_location = 33
				elif transition == 1:
					if branch == 0:
						target_state.L_X_Scheduler_location = 33
				elif transition == 2:
					if branch == 0:
						target_state.L_X_Scheduler_location = 25
				elif transition == 3:
					if branch == 0:
						target_state.L_X_Scheduler_location = 25
				elif transition == 4:
					if branch == 0:
						target_state.L_X_Scheduler_location = 17
				elif transition == 5:
					if branch == 0:
						target_state.L_X_Scheduler_location = 17
				elif transition == 6:
					if branch == 0:
						target_state.L_X_Scheduler_location = 17
				elif transition == 7:
					if branch == 0:
						target_state.L_X_Scheduler_location = 3
				elif transition == 8:
					if branch == 0:
						target_state.L_X_Scheduler_location = 3
				elif transition == 9:
					if branch == 0:
						target_state.L_X_Scheduler_location = 3
				elif transition == 10:
					if branch == 0:
						target_state.L_X_Scheduler_location = 1
			elif location == 3:
				if transition == 0:
					if branch == 0:
						target_state.L_X_Scheduler_location = 5
				elif transition == 1:
					if branch == 0:
						target_state.L_X_Scheduler_location = 4
				elif transition == 2:
					if branch == 0:
						target_state.L_X_Scheduler_location = 3
			elif location == 4:
				if transition == 0:
					if branch == 0:
						target_state.L_X_Scheduler_location = 4
			elif location == 5:
				if transition == 0:
					if branch == 0:
						target_state.L_X_Scheduler_location = 6
			elif location == 6:
				if transition == 0:
					if branch == 0:
						target_state.L_X_Scheduler_location = 7
				elif transition == 1:
					if branch == 0:
						target_state.L_X_Scheduler_location = 6
			elif location == 7:
				if transition == 0:
					if branch == 0:
						target_state.L_X_Scheduler_location = 8
			elif location == 8:
				if transition == 0:
					if branch == 0:
						target_state.L_X_Scheduler_location = 9
				elif transition == 1:
					if branch == 0:
						target_state.L_X_Scheduler_location = 8
			elif location == 9:
				if transition == 0:
					if branch == 0:
						target_state.L_X_Scheduler_location = 10
			elif location == 10:
				if transition == 0:
					if branch == 0:
						target_state.L_X_Scheduler_location = 11
				elif transition == 1:
					if branch == 0:
						target_state.L_X_Scheduler_location = 10
			elif location == 11:
				if transition == 0:
					if branch == 0:
						target_state.L_X_Scheduler_location = 12
			elif location == 12:
				if transition == 0:
					if branch == 0:
						target_state.L_X_Scheduler_location = 16
				elif transition == 1:
					if branch == 0:
						target_state.L_X_Scheduler_location = 13
			elif location == 13:
				if transition == 0:
					if branch == 0:
						target_state.L_X_Scheduler_location = 13
				elif transition == 1:
					if branch == 0:
						target_state.L_X_Scheduler_location = 14
			elif location == 14:
				if transition == 0:
					if branch == 0:
						target_state.L_X_Scheduler_location = 14
				elif transition == 1:
					if branch == 0:
						target_state.L_X_Scheduler_location = 15
			elif location == 15:
				if transition == 0:
					if branch == 0:
						target_state.L_X_Scheduler_location = 15
				elif transition == 1:
					if branch == 0:
						target_state.L_X_Scheduler_location = 2
			elif location == 16:
				if transition == 0:
					if branch == 0:
						target_state.L_X_Scheduler_location = 16
				elif transition == 1:
					if branch == 0:
						target_state.L_X_Scheduler_location = 13
			elif location == 17:
				if transition == 0:
					if branch == 0:
						target_state.L_X_Scheduler_location = 18
				elif transition == 1:
					if branch == 0:
						target_state.L_X_Scheduler_location = 4
				elif transition == 2:
					if branch == 0:
						target_state.L_X_Scheduler_location = 17
			elif location == 18:
				if transition == 0:
					if branch == 0:
						target_state.L_X_Scheduler_location = 19
			elif location == 19:
				if transition == 0:
					if branch == 0:
						target_state.L_X_Scheduler_location = 20
				elif transition == 1:
					if branch == 0:
						target_state.L_X_Scheduler_location = 19
			elif location == 20:
				if transition == 0:
					if branch == 0:
						target_state.L_X_Scheduler_location = 21
			elif location == 21:
				if transition == 0:
					if branch == 0:
						target_state.L_X_Scheduler_location = 22
				elif transition == 1:
					if branch == 0:
						target_state.L_X_Scheduler_location = 21
			elif location == 22:
				if transition == 0:
					if branch == 0:
						target_state.L_X_Scheduler_location = 23
			elif location == 23:
				if transition == 0:
					if branch == 0:
						target_state.L_X_Scheduler_location = 24
				elif transition == 1:
					if branch == 0:
						target_state.L_X_Scheduler_location = 23
			elif location == 24:
				if transition == 0:
					if branch == 0:
						target_state.L_X_Scheduler_location = 12
			elif location == 25:
				if transition == 0:
					if branch == 0:
						target_state.L_X_Scheduler_location = 26
				elif transition == 1:
					if branch == 0:
						target_state.L_X_Scheduler_location = 4
				elif transition == 2:
					if branch == 0:
						target_state.L_X_Scheduler_location = 25
			elif location == 26:
				if transition == 0:
					if branch == 0:
						target_state.L_X_Scheduler_location = 27
			elif location == 27:
				if transition == 0:
					if branch == 0:
						target_state.L_X_Scheduler_location = 28
				elif transition == 1:
					if branch == 0:
						target_state.L_X_Scheduler_location = 27
			elif location == 28:
				if transition == 0:
					if branch == 0:
						target_state.L_X_Scheduler_location = 29
			elif location == 29:
				if transition == 0:
					if branch == 0:
						target_state.L_X_Scheduler_location = 30
				elif transition == 1:
					if branch == 0:
						target_state.L_X_Scheduler_location = 29
			elif location == 30:
				if transition == 0:
					if branch == 0:
						target_state.L_X_Scheduler_location = 31
			elif location == 31:
				if transition == 0:
					if branch == 0:
						target_state.L_X_Scheduler_location = 32
				elif transition == 1:
					if branch == 0:
						target_state.L_X_Scheduler_location = 31
			elif location == 32:
				if transition == 0:
					if branch == 0:
						target_state.L_X_Scheduler_location = 12
			elif location == 33:
				if transition == 0:
					if branch == 0:
						target_state.L_X_Scheduler_location = 34
				elif transition == 1:
					if branch == 0:
						target_state.L_X_Scheduler_location = 4
				elif transition == 2:
					if branch == 0:
						target_state.L_X_Scheduler_location = 33
			elif location == 34:
				if transition == 0:
					if branch == 0:
						target_state.L_X_Scheduler_location = 35
			elif location == 35:
				if transition == 0:
					if branch == 0:
						target_state.L_X_Scheduler_location = 36
				elif transition == 1:
					if branch == 0:
						target_state.L_X_Scheduler_location = 35
			elif location == 36:
				if transition == 0:
					if branch == 0:
						target_state.L_X_Scheduler_location = 37
			elif location == 37:
				if transition == 0:
					if branch == 0:
						target_state.L_X_Scheduler_location = 38
				elif transition == 1:
					if branch == 0:
						target_state.L_X_Scheduler_location = 37
			elif location == 38:
				if transition == 0:
					if branch == 0:
						target_state.L_X_Scheduler_location = 39
			elif location == 39:
				if transition == 0:
					if branch == 0:
						target_state.L_X_Scheduler_location = 40
				elif transition == 1:
					if branch == 0:
						target_state.L_X_Scheduler_location = 39
			elif location == 40:
				if transition == 0:
					if branch == 0:
						target_state.L_X_Scheduler_location = 12

# Automaton: GlobalSync
class GlobalSyncAutomaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [2]
		self.transition_labels = [[40, 41]]
		self.branch_counts = [[1, 1]]
	
	def set_initial_values(self, state: State) -> None:
		pass
	
	def set_initial_transient_values(self, transient: Transient) -> None:
		pass
	
	def get_transient_value(self, state: State, transient_variable: str):
		location = 0
		return None
	
	def get_transition_count(self, state: State) -> int:
		return self.transition_counts[0]
	
	def get_transition_label(self, state: State, transition: int) -> int:
		return self.transition_labels[0][transition]
	
	def get_guard_value(self, state: State, transition: int) -> bool:
		location = 0
		if location == 0:
			if transition >= 0 and transition < 2:
				return True
	
	def get_branch_count(self, state: State, transition: int) -> int:
		return self.branch_counts[0][transition]
	
	def get_probability_value(self, state: State, transition: int, branch: int) -> float:
		location = 0
		if location == 0:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
	
	def jump(self, state: State, transient: Transient, transition: int, branch: int, assignment_index: int, target_state: State, target_transient: Transient) -> None:
		if assignment_index == 0:
			location = 0
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.clk = min((state.clk + 1), 4321)
						target_state.job_clk = min((state.job_clk + 1), 41)
		elif assignment_index == 2:
			location = 0
			if location == 0:
				if transition == 0:
					if branch == 0:
						pass
				elif transition == 1:
					if branch == 0:
						target_transient.Generated_Schedule_until_clk__edge_reward = transient.cost

class PropertyExpression(object):
	__slots__ = ("op", "args")
	
	def __init__(self, op: str, args: List[Union[int, PropertyExpression]]):
		self.op = op
		self.args = args
	
	def __str__(self):
		result = self.op + "("
		needComma = False
		for arg in self.args:
			if needComma:
				result += ", "
			else:
				needComma = True
			result += str(arg)
		return result + ")"

class Property(object):
	__slots__ = ("name", "exp")
	
	def __init__(self, name: str, exp: PropertyExpression):
		self.name = name
		self.exp = exp
	
	def __str__(self):
		return self.name + ": " + str(self.exp)

class Transition(object):
	__slots__ = ("sync_vector", "label", "transitions")
	
	def __init__(self, sync_vector: int, label: int = 0, transitions: List[int] = [-1, -1, -1, -1, -1]):
		self.sync_vector = sync_vector
		self.label = label
		self.transitions = transitions

class Branch(object):
	__slots__ = ("probability", "branches")
	
	def __init__(self, probability = 0.0, branches = [0, 0, 0, 0, 0]):
		self.probability = probability
		self.branches = branches

class Network(object):
	__slots__ = ("network", "components", "transition_labels", "sync_vectors", "properties", "variables", "_initial_transient", "_aut_Battery_job", "_aut_PV_job", "_aut_UHF_job", "_aut_L_X_Scheduler", "_aut_GlobalSync")
	
	def __init__(self):
		self.network = self
		self.transition_labels = { 0: "τ", 1: "update_PV", 2: "update_UHF", 3: "update_X_Band_Kourou", 4: "update_X_Band_Toulouse", 5: "update_L_Band_Inmarsat_3F2", 6: "update_L_Band_Inmarsat_3F3", 7: "PV_aligned_start", 8: "PV_notaligned_start", 9: "PV_notaligned_end", 10: "PV_aligned_end", 11: "UHF_start", 12: "UHF_skip", 13: "UHF_end", 14: "Sched_3F2", 15: "Sched_3F3", 16: "Sched_Kourou", 17: "Sched_Toulouse", 18: "Sched_Nothing", 19: "tick_sched", 20: "X_Toulouse_slew_preheat", 21: "X_Toulouse_start", 22: "X_Toulouse_slewback", 23: "X_Toulouse_end", 24: "Skip_3F2", 25: "Skip_3F3", 26: "Skip_Kourou", 27: "Skip_Toulouse", 28: "X_Kourou_slew_preheat", 29: "X_Kourou_start", 30: "X_Kourou_slewback", 31: "X_Kourou_end", 32: "L_3F3_slew_preheat", 33: "L_3F3_start", 34: "L_3F3_slewback", 35: "L_3F3_end", 36: "L_3F2_slew_preheat", 37: "L_3F2_start", 38: "L_3F2_slewback", 39: "L_3F2_end", 40: "tick", 41: "tau" }
		self.sync_vectors = [[0, -1, -1, -1, -1, 0], [-1, 0, -1, -1, -1, 0], [-1, -1, 0, -1, -1, 0], [-1, -1, -1, 0, -1, 0], [-1, -1, -1, -1, 0, 0], [-1, 7, -1, -1, 41, 7], [-1, 8, -1, -1, 41, 8], [-1, 9, -1, -1, 41, 9], [-1, 10, -1, -1, 41, 10], [1, 1, -1, -1, 41, 1], [-1, -1, 11, -1, 41, 11], [-1, -1, 12, -1, 41, 12], [-1, -1, 13, -1, 41, 13], [2, -1, 2, -1, 41, 2], [-1, -1, -1, 14, 41, 14], [-1, -1, -1, 15, 41, 15], [-1, -1, -1, 16, 41, 16], [-1, -1, -1, 17, 41, 17], [-1, -1, -1, 18, 41, 18], [-1, -1, -1, 19, 41, 19], [-1, -1, -1, 20, 41, 20], [-1, -1, -1, 21, 41, 21], [-1, -1, -1, 22, 41, 22], [-1, -1, -1, 23, 41, 23], [-1, -1, -1, 24, 41, 24], [-1, -1, -1, 25, 41, 25], [-1, -1, -1, 26, 41, 26], [-1, -1, -1, 27, 41, 27], [-1, -1, -1, 28, 41, 28], [-1, -1, -1, 29, 41, 29], [-1, -1, -1, 30, 41, 30], [-1, -1, -1, 31, 41, 31], [-1, -1, -1, 32, 41, 32], [-1, -1, -1, 33, 41, 33], [-1, -1, -1, 34, 41, 34], [-1, -1, -1, 35, 41, 35], [-1, -1, -1, 36, 41, 36], [-1, -1, -1, 37, 41, 37], [-1, -1, -1, 38, 41, 38], [-1, -1, -1, 39, 41, 39], [3, -1, -1, 3, 41, 3], [4, -1, -1, 4, 41, 4], [5, -1, -1, 5, 41, 5], [6, -1, -1, 6, 41, 6], [-1, 41, -1, -1, 41, 0], [-1, -1, 41, -1, 41, 0], [-1, -1, -1, 41, 41, 0], [40, 40, 40, 40, 40, 40]]
		self.properties = [Property("Generated Schedule until clk=", PropertyExpression("xmin", [0, PropertyExpression("ap", [1])]))]
		self.variables = [VariableInfo("clk", None, "int", 0, 4321), VariableInfo("job_clk", None, "int", 0, 41), VariableInfo("load", None, "int", -1200000, 1200000), VariableInfo("SoC", None, "int", 0, 149760000), VariableInfo("last_a_time", None, "int", 0, 4320), VariableInfo("current_a_time", None, "int", 0, 4320), VariableInfo("L_3F2_i", None, "int", 0, 76), VariableInfo("L_3F3_i", None, "int", 0, 78), VariableInfo("Sun_i", None, "int", 0, 86), VariableInfo("UHF_i", None, "int", 0, 22), VariableInfo("X_Kourou_i", None, "int", 0, 20), VariableInfo("X_Toulouse_i", None, "int", 0, 28), VariableInfo("is_aligned", None, "bool"), VariableInfo("L_X_counter", None, None), VariableInfo("Battery_job_location", 0, "int", 0, 2), VariableInfo("PV_job_location", 1, "int", 0, 8), VariableInfo("UHF_job_location", 2, "int", 0, 5), VariableInfo("L_X_Scheduler_location", 3, "int", 0, 40), VariableInfo("sched_clk", 3, "int", 0, 601)]
		self._aut_Battery_job = Battery_jobAutomaton(self)
		self._aut_PV_job = PV_jobAutomaton(self)
		self._aut_UHF_job = UHF_jobAutomaton(self)
		self._aut_L_X_Scheduler = L_X_SchedulerAutomaton(self)
		self._aut_GlobalSync = GlobalSyncAutomaton(self)
		self.components = [self._aut_Battery_job, self._aut_PV_job, self._aut_UHF_job, self._aut_L_X_Scheduler, self._aut_GlobalSync]
		self._initial_transient = self._get_initial_transient()
	
	def get_initial_state(self) -> State:
		state = State()
		state.clk = 0
		state.job_clk = 0
		state.load = 179340
		state.SoC = 119808000
		state.last_a_time = 0
		state.current_a_time = 0
		state.L_3F2_i = 0
		state.L_3F3_i = 0
		state.Sun_i = 0
		state.UHF_i = 0
		state.X_Kourou_i = 0
		state.X_Toulouse_i = 0
		state.is_aligned = False
		state.L_X_counter = [0, 0, 0, 0, 0, 2]
		self._aut_Battery_job.set_initial_values(state)
		self._aut_PV_job.set_initial_values(state)
		self._aut_UHF_job.set_initial_values(state)
		self._aut_L_X_Scheduler.set_initial_values(state)
		self._aut_GlobalSync.set_initial_values(state)
		return state
	
	def _get_initial_transient(self) -> Transient:
		transient = Transient()
		transient.Generated_Schedule_until_clk__edge_reward = 0
		transient.L_Band_Inmarsat_3F2_data = [89, 182, 187, 280, 283, 375, 378, 471, 474, 567, 572, 665, 673, 766, 774, 867, 871, 964, 967, 1060, 1063, 1156, 1159, 1251, 1256, 1349, 1356, 1449, 1458, 1550, 1556, 1649, 1652, 1745, 1748, 1841, 1843, 1936, 1940, 2033, 2040, 2133, 2141, 2234, 2241, 2333, 2337, 2430, 2433, 2526, 2528, 2621, 2625, 2717, 2723, 2816, 2825, 2918, 2925, 3018, 3022, 3115, 3118, 3211, 3213, 3306, 3309, 3402, 3407, 3500, 3508, 3601, 3609, 3702, 3707, 3800, 0]
		transient.L_Band_Inmarsat_3F3_data = [45, 138, 142, 235, 238, 331, 333, 426, 429, 522, 528, 621, 629, 722, 729, 822, 827, 920, 923, 1016, 1018, 1111, 1114, 1207, 1212, 1305, 1313, 1406, 1414, 1506, 1512, 1604, 1608, 1701, 1703, 1796, 1799, 1892, 1896, 1989, 1996, 2089, 2098, 2190, 2196, 2289, 2293, 2385, 2388, 2481, 2484, 2577, 2580, 2673, 2680, 2773, 2781, 2874, 2881, 2973, 2977, 3070, 3073, 3166, 3168, 3261, 3265, 3358, 3363, 3456, 3465, 3558, 3565, 3658, 3662, 3755, 3758, 3851, 0]
		transient.Sun_data = [19, 77, 111, 169, 203, 261, 294, 352, 386, 444, 478, 536, 570, 628, 661, 719, 753, 811, 845, 903, 937, 995, 1028, 1087, 1120, 1178, 1212, 1270, 1303, 1362, 1395, 1454, 1487, 1545, 1579, 1637, 1670, 1729, 1762, 1821, 1854, 1913, 1946, 2004, 2037, 2096, 2129, 2188, 2221, 2280, 2313, 2372, 2404, 2463, 2496, 2555, 2588, 2647, 2680, 2739, 2771, 2831, 2863, 2922, 2955, 3014, 3047, 3106, 3138, 3198, 3230, 3289, 3322, 3381, 3413, 3473, 3505, 3565, 3597, 3657, 3689, 3748, 3780, 3840, 3872, 3932, 0]
		transient.UHF_data = [1015, 1019, 1107, 1116, 1201, 1211, 1296, 1306, 1392, 1400, 1489, 1492, 2481, 2489, 2575, 2584, 2670, 2680, 2765, 2774, 2861, 2868, 0]
		transient.X_Band_Kourou_data = [399, 408, 496, 502, 1089, 1096, 1183, 1192, 1773, 1781, 1867, 1877, 2556, 2566, 2653, 2659, 3240, 3250, 3339, 3343, 0]
		transient.X_Band_Toulouse_data = [114, 123, 1010, 1017, 1103, 1113, 1199, 1209, 1296, 1305, 1391, 1401, 1487, 1497, 1584, 1589, 2477, 2486, 2572, 2582, 2668, 2678, 2765, 2774, 2860, 2870, 2956, 2964, 0]
		transient.cost = 0
		self._aut_Battery_job.set_initial_transient_values(transient)
		self._aut_PV_job.set_initial_transient_values(transient)
		self._aut_UHF_job.set_initial_transient_values(transient)
		self._aut_L_X_Scheduler.set_initial_transient_values(transient)
		self._aut_GlobalSync.set_initial_transient_values(transient)
		return transient
	
	def get_expression_value(self, state: State, expression: int):
		if expression == 0:
			return self.network._get_transient_value(state, "Generated_Schedule_until_clk__edge_reward")
		elif expression == 1:
			return (state.clk >= 2160)
		else:
			raise IndexError
	
	def _get_jump_expression_value(self, state: State, transient: Transient, expression: int):
		if expression == 0:
			return transient.Generated_Schedule_until_clk__edge_reward
		elif expression == 1:
			return (state.clk >= 2160)
		else:
			raise IndexError
	
	def _get_transient_value(self, state: State, transient_variable: str):
		# Query the automata for the current value of the transient variable
		result = self._aut_Battery_job.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		result = self._aut_PV_job.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		result = self._aut_UHF_job.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		result = self._aut_L_X_Scheduler.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		result = self._aut_GlobalSync.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		# No automaton has a value: return the transient variable's (cached) initial value
		return getattr(self._initial_transient, transient_variable)
	
	def get_transitions(self, state: State) -> List[Transition]:
		# Collect all automaton transitions, gathered by label
		transitions = []
		trans_Battery_job = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
		transition_count = self._aut_Battery_job.get_transition_count(state)
		for i in range(transition_count):
			if self._aut_Battery_job.get_guard_value(state, i):
				trans_Battery_job[self._aut_Battery_job.get_transition_label(state, i)].append(i)
		trans_PV_job = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
		transition_count = self._aut_PV_job.get_transition_count(state)
		for i in range(transition_count):
			if self._aut_PV_job.get_guard_value(state, i):
				trans_PV_job[self._aut_PV_job.get_transition_label(state, i)].append(i)
		trans_UHF_job = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
		transition_count = self._aut_UHF_job.get_transition_count(state)
		for i in range(transition_count):
			if self._aut_UHF_job.get_guard_value(state, i):
				trans_UHF_job[self._aut_UHF_job.get_transition_label(state, i)].append(i)
		trans_L_X_Scheduler = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
		transition_count = self._aut_L_X_Scheduler.get_transition_count(state)
		for i in range(transition_count):
			if self._aut_L_X_Scheduler.get_guard_value(state, i):
				trans_L_X_Scheduler[self._aut_L_X_Scheduler.get_transition_label(state, i)].append(i)
		trans_GlobalSync = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
		transition_count = self._aut_GlobalSync.get_transition_count(state)
		for i in range(transition_count):
			if self._aut_GlobalSync.get_guard_value(state, i):
				trans_GlobalSync[self._aut_GlobalSync.get_transition_label(state, i)].append(i)
		# Match automaton transitions onto synchronisation vectors
		for svi in range(len(self.sync_vectors)):
			sv = self.sync_vectors[svi]
			synced = [[-1, -1, -1, -1, -1, -1]]
			# Battery_job
			if synced is not None:
				if sv[0] != -1:
					if len(trans_Battery_job[sv[0]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][0] = trans_Battery_job[sv[0]][0]
						for i in range(1, len(trans_Battery_job[sv[0]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][0] = trans_Battery_job[sv[0]][i]
			# PV_job
			if synced is not None:
				if sv[1] != -1:
					if len(trans_PV_job[sv[1]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][1] = trans_PV_job[sv[1]][0]
						for i in range(1, len(trans_PV_job[sv[1]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][1] = trans_PV_job[sv[1]][i]
			# UHF_job
			if synced is not None:
				if sv[2] != -1:
					if len(trans_UHF_job[sv[2]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][2] = trans_UHF_job[sv[2]][0]
						for i in range(1, len(trans_UHF_job[sv[2]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][2] = trans_UHF_job[sv[2]][i]
			# L_X_Scheduler
			if synced is not None:
				if sv[3] != -1:
					if len(trans_L_X_Scheduler[sv[3]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][3] = trans_L_X_Scheduler[sv[3]][0]
						for i in range(1, len(trans_L_X_Scheduler[sv[3]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][3] = trans_L_X_Scheduler[sv[3]][i]
			# GlobalSync
			if synced is not None:
				if sv[4] != -1:
					if len(trans_GlobalSync[sv[4]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][4] = trans_GlobalSync[sv[4]][0]
						for i in range(1, len(trans_GlobalSync[sv[4]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][4] = trans_GlobalSync[sv[4]][i]
			if synced is not None:
				for sync in synced:
					sync[-1] = sv[-1]
					sync.append(svi)
				transitions.extend(filter(lambda s: s[-2] != -1, synced))
		# Convert to Transition instances
		for i in range(len(transitions)):
			transitions[i] = Transition(transitions[i][-1], transitions[i][-2], transitions[i])
			del transitions[i].transitions[-1]
			del transitions[i].transitions[-1]
		# Done
		return transitions
	
	def get_branches(self, state: State, transition: Transition) -> List[Branch]:
		combs = [[-1, -1, -1, -1, -1]]
		probs = [1.0]
		if transition.transitions[0] != -1:
			existing = len(combs)
			branch_count = self._aut_Battery_job.get_branch_count(state, transition.transitions[0])
			for i in range(1, branch_count):
				probability = self._aut_Battery_job.get_probability_value(state, transition.transitions[0], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][0] = i
					probs.append(probs[j] * probability)
			probability = self._aut_Battery_job.get_probability_value(state, transition.transitions[0], 0)
			for i in range(existing):
				combs[i][0] = 0
				probs[i] *= probability
		if transition.transitions[1] != -1:
			existing = len(combs)
			branch_count = self._aut_PV_job.get_branch_count(state, transition.transitions[1])
			for i in range(1, branch_count):
				probability = self._aut_PV_job.get_probability_value(state, transition.transitions[1], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][1] = i
					probs.append(probs[j] * probability)
			probability = self._aut_PV_job.get_probability_value(state, transition.transitions[1], 0)
			for i in range(existing):
				combs[i][1] = 0
				probs[i] *= probability
		if transition.transitions[2] != -1:
			existing = len(combs)
			branch_count = self._aut_UHF_job.get_branch_count(state, transition.transitions[2])
			for i in range(1, branch_count):
				probability = self._aut_UHF_job.get_probability_value(state, transition.transitions[2], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][2] = i
					probs.append(probs[j] * probability)
			probability = self._aut_UHF_job.get_probability_value(state, transition.transitions[2], 0)
			for i in range(existing):
				combs[i][2] = 0
				probs[i] *= probability
		if transition.transitions[3] != -1:
			existing = len(combs)
			branch_count = self._aut_L_X_Scheduler.get_branch_count(state, transition.transitions[3])
			for i in range(1, branch_count):
				probability = self._aut_L_X_Scheduler.get_probability_value(state, transition.transitions[3], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][3] = i
					probs.append(probs[j] * probability)
			probability = self._aut_L_X_Scheduler.get_probability_value(state, transition.transitions[3], 0)
			for i in range(existing):
				combs[i][3] = 0
				probs[i] *= probability
		if transition.transitions[4] != -1:
			existing = len(combs)
			branch_count = self._aut_GlobalSync.get_branch_count(state, transition.transitions[4])
			for i in range(1, branch_count):
				probability = self._aut_GlobalSync.get_probability_value(state, transition.transitions[4], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][4] = i
					probs.append(probs[j] * probability)
			probability = self._aut_GlobalSync.get_probability_value(state, transition.transitions[4], 0)
			for i in range(existing):
				combs[i][4] = 0
				probs[i] *= probability
		# Convert to Branch instances
		for i in range(len(combs)):
			combs[i] = Branch(probs[i], combs[i])
		# Done
		return list(filter(lambda b: b.probability > 0.0, combs))
	
	def jump(self, state: State, transition: Transition, branch: Branch, expressions: List[int] = []) -> State:
		transient = self._get_initial_transient()
		for i in range(0, 3):
			target_state = State()
			state.copy_to(target_state)
			target_transient = Transient()
			transient.copy_to(target_transient)
			if transition.transitions[0] != -1:
				self._aut_Battery_job.jump(state, transient, transition.transitions[0], branch.branches[0], i, target_state, target_transient)
			if transition.transitions[1] != -1:
				self._aut_PV_job.jump(state, transient, transition.transitions[1], branch.branches[1], i, target_state, target_transient)
			if transition.transitions[2] != -1:
				self._aut_UHF_job.jump(state, transient, transition.transitions[2], branch.branches[2], i, target_state, target_transient)
			if transition.transitions[3] != -1:
				self._aut_L_X_Scheduler.jump(state, transient, transition.transitions[3], branch.branches[3], i, target_state, target_transient)
			if transition.transitions[4] != -1:
				self._aut_GlobalSync.jump(state, transient, transition.transitions[4], branch.branches[4], i, target_state, target_transient)
			state = target_state
			transient = target_transient
		for i in range(len(expressions)):
			expressions[i] = self._get_jump_expression_value(state, transient, expressions[i])
		return state
	
	def jump_np(self, state: State, transition: Transition, expressions: List[int] = []) -> State:
		return self.jump(state, transition, self.get_branches(state, transition)[0], expressions)
