# jobshop_workers

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
	__slots__ = ("jobs_in_progress", "jobs_done", "had_lunch", "machine_1_available", "machine_2_available", "time", "Worker_location", "x", "Worker_location_1", "x_1", "Factory_location", "Machine_location", "x_2", "Machine_location_1", "x_3")
	
	def get_variable_value(self, variable: int):
		if variable == 0:
			return self.jobs_in_progress
		elif variable == 1:
			return self.jobs_done
		elif variable == 2:
			return self.had_lunch
		elif variable == 3:
			return self.machine_1_available
		elif variable == 4:
			return self.machine_2_available
		elif variable == 5:
			return self.time
		elif variable == 6:
			return self.Worker_location
		elif variable == 7:
			return self.x
		elif variable == 8:
			return self.Worker_location_1
		elif variable == 9:
			return self.x_1
		elif variable == 10:
			return self.Factory_location
		elif variable == 11:
			return self.Machine_location
		elif variable == 12:
			return self.x_2
		elif variable == 13:
			return self.Machine_location_1
		elif variable == 14:
			return self.x_3
	
	def copy_to(self, other: State):
		other.jobs_in_progress = self.jobs_in_progress
		other.jobs_done = self.jobs_done
		other.had_lunch = list(self.had_lunch)
		other.machine_1_available = self.machine_1_available
		other.machine_2_available = self.machine_2_available
		other.time = self.time
		other.Worker_location = self.Worker_location
		other.x = self.x
		other.Worker_location_1 = self.Worker_location_1
		other.x_1 = self.x_1
		other.Factory_location = self.Factory_location
		other.Machine_location = self.Machine_location
		other.x_2 = self.x_2
		other.Machine_location_1 = self.Machine_location_1
		other.x_3 = self.x_3
	
	def __eq__(self, other):
		return isinstance(other, self.__class__) and self.jobs_in_progress == other.jobs_in_progress and self.jobs_done == other.jobs_done and self.had_lunch == other.had_lunch and self.machine_1_available == other.machine_1_available and self.machine_2_available == other.machine_2_available and self.time == other.time and self.Worker_location == other.Worker_location and self.x == other.x and self.Worker_location_1 == other.Worker_location_1 and self.x_1 == other.x_1 and self.Factory_location == other.Factory_location and self.Machine_location == other.Machine_location and self.x_2 == other.x_2 and self.Machine_location_1 == other.Machine_location_1 and self.x_3 == other.x_3
	
	def __ne__(self, other):
		return not self.__eq__(other)
	
	def __hash__(self):
		result = 75619
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.jobs_in_progress)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.jobs_done)) & 0xFFFFFFFF
		for x in self.had_lunch:
			result = (((101 * result) & 0xFFFFFFFF) + hash(x)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.machine_1_available)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.machine_2_available)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.time)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.Worker_location)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.x)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.Worker_location_1)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.x_1)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.Factory_location)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.Machine_location)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.x_2)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.Machine_location_1)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.x_3)) & 0xFFFFFFFF
		return result
	
	def __str__(self):
		result = "("
		result += "jobs_in_progress = " + str(self.jobs_in_progress)
		result += ", jobs_done = " + str(self.jobs_done)
		result += ", had_lunch = " + str(self.had_lunch)
		result += ", machine_1_available = " + str(self.machine_1_available)
		result += ", machine_2_available = " + str(self.machine_2_available)
		result += ", time = " + str(self.time)
		result += ", Worker_location = " + str(self.Worker_location)
		result += ", x = " + str(self.x)
		result += ", Worker_location_1 = " + str(self.Worker_location_1)
		result += ", x_1 = " + str(self.x_1)
		result += ", Factory_location = " + str(self.Factory_location)
		result += ", Machine_location = " + str(self.Machine_location)
		result += ", x_2 = " + str(self.x_2)
		result += ", Machine_location_1 = " + str(self.Machine_location_1)
		result += ", x_3 = " + str(self.x_3)
		result += ")"
		return result

# Transients
class Transient(object):
	__slots__ = ()
	
	def copy_to(self, other: Transient):
		pass
	
	def __eq__(self, other):
		return isinstance(other, self.__class__)
	
	def __ne__(self, other):
		return not self.__eq__(other)
	
	def __hash__(self):
		result = 75619
		return result
	
	def __str__(self):
		result = "("
		result += ")"
		return result

# Automaton: Worker
class WorkerAutomaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [2, 2, 2, 1, 2, 2, 2]
		self.transition_labels = [[0, 1], [2, 3], [4, 23], [5], [0, 1], [0, 23], [6, 23]]
		self.branch_counts = [[1, 1], [1, 1], [1, 1], [1], [1, 1], [1, 1], [1, 1]]
	
	def set_initial_values(self, state: State) -> None:
		state.Worker_location = 0
		state.x = 0
	
	def set_initial_transient_values(self, transient: Transient) -> None:
		pass
	
	def get_transient_value(self, state: State, transient_variable: str):
		location = state.Worker_location
		return None
	
	def get_transition_count(self, state: State) -> int:
		return self.transition_counts[state.Worker_location]
	
	def get_transition_label(self, state: State, transition: int) -> int:
		return self.transition_labels[state.Worker_location][transition]
	
	def get_guard_value(self, state: State, transition: int) -> bool:
		location = state.Worker_location
		if location == 3:
			return True
		elif location == 0:
			if transition == 0:
				return (((not (state.had_lunch)[0]) and (state.time >= 180)) and (state.time <= 300))
			elif transition == 1:
				return True
		elif location == 1:
			if transition == 0:
				return state.machine_1_available
			elif transition == 1:
				return state.machine_2_available
		elif location == 2:
			if transition >= 0 and transition < 2:
				return True
		elif location == 4:
			if transition == 0:
				return (((not (state.had_lunch)[0]) and (state.time >= 180)) and (state.time <= 300))
			elif transition == 1:
				return True
		elif location == 5:
			if transition == 0:
				return (state.x >= 30)
			elif transition == 1:
				return (state.x < 30)
		elif location == 6:
			if transition >= 0 and transition < 2:
				return True
	
	def get_branch_count(self, state: State, transition: int) -> int:
		return self.branch_counts[state.Worker_location][transition]
	
	def get_probability_value(self, state: State, transition: int, branch: int) -> float:
		location = state.Worker_location
		if location == 0:
			if transition == 0:
				return 1
			elif transition == 1:
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
			elif transition == 1:
				return 1
		elif location == 6:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
	
	def jump(self, state: State, transient: Transient, transition: int, branch: int, assignment_index: int, target_state: State, target_transient: Transient) -> None:
		if assignment_index == 0:
			location = state.Worker_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.x = 0
						target_state.Worker_location = 5
				elif transition == 1:
					if branch == 0:
						target_state.Worker_location = 1
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.machine_1_available = False
						target_state.Worker_location = 6
				elif transition == 1:
					if branch == 0:
						target_state.machine_2_available = False
						target_state.Worker_location = 2
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.machine_2_available = True
						target_state.Worker_location = 3
				elif transition == 1:
					if branch == 0:
						target_state.Worker_location = 2
			elif location == 3:
				if transition == 0:
					if branch == 0:
						target_state.Worker_location = 4
			elif location == 4:
				if transition == 0:
					if branch == 0:
						target_state.x = 0
						target_state.Worker_location = 5
				elif transition == 1:
					if branch == 0:
						target_state.Worker_location = 1
			elif location == 5:
				if transition == 0:
					if branch == 0:
						target_state.had_lunch[0] = True
						target_state.x = 0
						target_state.Worker_location = 4
				elif transition == 1:
					if branch == 0:
						target_state.x = min((state.x + 1), 31)
						target_state.Worker_location = 5
			elif location == 6:
				if transition == 0:
					if branch == 0:
						target_state.machine_1_available = True
						target_state.Worker_location = 3
				elif transition == 1:
					if branch == 0:
						target_state.Worker_location = 6

# Automaton: Worker
class WorkerAutomaton_1(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [2, 2, 2, 1, 2, 2, 2]
		self.transition_labels = [[0, 1], [2, 3], [4, 23], [5], [0, 1], [0, 23], [6, 23]]
		self.branch_counts = [[1, 1], [1, 1], [1, 1], [1], [1, 1], [1, 1], [1, 1]]
	
	def set_initial_values(self, state: State) -> None:
		state.Worker_location_1 = 0
		state.x_1 = 0
	
	def set_initial_transient_values(self, transient: Transient) -> None:
		pass
	
	def get_transient_value(self, state: State, transient_variable: str):
		location = state.Worker_location_1
		return None
	
	def get_transition_count(self, state: State) -> int:
		return self.transition_counts[state.Worker_location_1]
	
	def get_transition_label(self, state: State, transition: int) -> int:
		return self.transition_labels[state.Worker_location_1][transition]
	
	def get_guard_value(self, state: State, transition: int) -> bool:
		location = state.Worker_location_1
		if location == 3:
			return True
		elif location == 0:
			if transition == 0:
				return (((not (state.had_lunch)[1]) and (state.time >= 180)) and (state.time <= 300))
			elif transition == 1:
				return True
		elif location == 1:
			if transition == 0:
				return state.machine_1_available
			elif transition == 1:
				return state.machine_2_available
		elif location == 2:
			if transition >= 0 and transition < 2:
				return True
		elif location == 4:
			if transition == 0:
				return (((not (state.had_lunch)[1]) and (state.time >= 180)) and (state.time <= 300))
			elif transition == 1:
				return True
		elif location == 5:
			if transition == 0:
				return (state.x_1 >= 30)
			elif transition == 1:
				return (state.x_1 < 30)
		elif location == 6:
			if transition >= 0 and transition < 2:
				return True
	
	def get_branch_count(self, state: State, transition: int) -> int:
		return self.branch_counts[state.Worker_location_1][transition]
	
	def get_probability_value(self, state: State, transition: int, branch: int) -> float:
		location = state.Worker_location_1
		if location == 0:
			if transition == 0:
				return 1
			elif transition == 1:
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
			elif transition == 1:
				return 1
		elif location == 6:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
	
	def jump(self, state: State, transient: Transient, transition: int, branch: int, assignment_index: int, target_state: State, target_transient: Transient) -> None:
		if assignment_index == 0:
			location = state.Worker_location_1
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.x_1 = 0
						target_state.Worker_location_1 = 5
				elif transition == 1:
					if branch == 0:
						target_state.Worker_location_1 = 1
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.machine_1_available = False
						target_state.Worker_location_1 = 6
				elif transition == 1:
					if branch == 0:
						target_state.machine_2_available = False
						target_state.Worker_location_1 = 2
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.machine_2_available = True
						target_state.Worker_location_1 = 3
				elif transition == 1:
					if branch == 0:
						target_state.Worker_location_1 = 2
			elif location == 3:
				if transition == 0:
					if branch == 0:
						target_state.Worker_location_1 = 4
			elif location == 4:
				if transition == 0:
					if branch == 0:
						target_state.x_1 = 0
						target_state.Worker_location_1 = 5
				elif transition == 1:
					if branch == 0:
						target_state.Worker_location_1 = 1
			elif location == 5:
				if transition == 0:
					if branch == 0:
						target_state.had_lunch[1] = True
						target_state.x_1 = 0
						target_state.Worker_location_1 = 4
				elif transition == 1:
					if branch == 0:
						target_state.x_1 = min((state.x_1 + 1), 31)
						target_state.Worker_location_1 = 5
			elif location == 6:
				if transition == 0:
					if branch == 0:
						target_state.machine_1_available = True
						target_state.Worker_location_1 = 3
				elif transition == 1:
					if branch == 0:
						target_state.Worker_location_1 = 6

# Automaton: Factory
class FactoryAutomaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [5, 3]
		self.transition_labels = [[7, 8, 9, 10, 23], [0, 0, 23]]
		self.branch_counts = [[1, 1, 1, 1, 1], [1, 1, 1]]
	
	def set_initial_values(self, state: State) -> None:
		state.Factory_location = 0
	
	def set_initial_transient_values(self, transient: Transient) -> None:
		pass
	
	def get_transient_value(self, state: State, transient_variable: str):
		location = state.Factory_location
		return None
	
	def get_transition_count(self, state: State) -> int:
		return self.transition_counts[state.Factory_location]
	
	def get_transition_label(self, state: State, transition: int) -> int:
		return self.transition_labels[state.Factory_location][transition]
	
	def get_guard_value(self, state: State, transition: int) -> bool:
		location = state.Factory_location
		if location == 0:
			if transition >= 0 and transition < 5:
				return True
		elif location == 1:
			if transition == 0:
				return (state.jobs_done == 160)
			elif transition == 1:
				return (state.jobs_done <= 159)
			elif transition == 2:
				return True
	
	def get_branch_count(self, state: State, transition: int) -> int:
		return self.branch_counts[state.Factory_location][transition]
	
	def get_probability_value(self, state: State, transition: int, branch: int) -> float:
		location = state.Factory_location
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
		elif location == 1:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
				return 1
	
	def jump(self, state: State, transient: Transient, transition: int, branch: int, assignment_index: int, target_state: State, target_transient: Transient) -> None:
		if assignment_index == 0:
			location = state.Factory_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.jobs_in_progress = (state.jobs_in_progress + 1)
						if target_state.jobs_in_progress > 2:
							raise OverflowError("Assigned value of " + str(target_state.jobs_in_progress) + " is greater than the upper bound of 2 for variable \"jobs_in_progress\".")
						target_state.Factory_location = 0
				elif transition == 1:
					if branch == 0:
						target_state.jobs_in_progress = (state.jobs_in_progress + 1)
						if target_state.jobs_in_progress > 2:
							raise OverflowError("Assigned value of " + str(target_state.jobs_in_progress) + " is greater than the upper bound of 2 for variable \"jobs_in_progress\".")
						target_state.Factory_location = 0
				elif transition == 2:
					if branch == 0:
						target_state.Factory_location = 1
				elif transition == 3:
					if branch == 0:
						target_state.Factory_location = 1
				elif transition == 4:
					if branch == 0:
						target_state.Factory_location = 0
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.jobs_in_progress = (state.jobs_in_progress - 1)
						if target_state.jobs_in_progress < 0:
							raise OverflowError("Assigned value of " + str(target_state.jobs_in_progress) + " is less than the lower bound of 0 for variable \"jobs_in_progress\".")
						target_state.Factory_location = 0
				elif transition == 1:
					if branch == 0:
						target_state.jobs_done = (state.jobs_done + 1)
						if target_state.jobs_done > 160:
							raise OverflowError("Assigned value of " + str(target_state.jobs_done) + " is greater than the upper bound of 160 for variable \"jobs_done\".")
						target_state.jobs_in_progress = (state.jobs_in_progress - 1)
						if target_state.jobs_in_progress < 0:
							raise OverflowError("Assigned value of " + str(target_state.jobs_in_progress) + " is less than the lower bound of 0 for variable \"jobs_in_progress\".")
						target_state.Factory_location = 0
				elif transition == 2:
					if branch == 0:
						target_state.Factory_location = 1

# Automaton: Machine
class MachineAutomaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [3, 2, 3, 2]
		self.transition_labels = [[11, 12, 23], [13, 23], [11, 12, 23], [14, 23]]
		self.branch_counts = [[1, 1, 1], [1, 1], [1, 1, 1], [1, 1]]
	
	def set_initial_values(self, state: State) -> None:
		state.Machine_location = 0
		state.x_2 = 0
	
	def set_initial_transient_values(self, transient: Transient) -> None:
		pass
	
	def get_transient_value(self, state: State, transient_variable: str):
		location = state.Machine_location
		return None
	
	def get_transition_count(self, state: State) -> int:
		return self.transition_counts[state.Machine_location]
	
	def get_transition_label(self, state: State, transition: int) -> int:
		return self.transition_labels[state.Machine_location][transition]
	
	def get_guard_value(self, state: State, transition: int) -> bool:
		location = state.Machine_location
		if location == 0:
			if transition >= 0 and transition < 3:
				return True
		elif location == 1:
			if transition == 0:
				return (state.x_2 >= 40)
			elif transition == 1:
				return (state.x_2 < 50)
		elif location == 2:
			if transition >= 0 and transition < 3:
				return True
		elif location == 3:
			if transition == 0:
				return (state.x_2 >= 40)
			elif transition == 1:
				return (state.x_2 < 50)
	
	def get_branch_count(self, state: State, transition: int) -> int:
		return self.branch_counts[state.Machine_location][transition]
	
	def get_probability_value(self, state: State, transition: int, branch: int) -> float:
		location = state.Machine_location
		if location == 0:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
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
		elif location == 3:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
	
	def jump(self, state: State, transient: Transient, transition: int, branch: int, assignment_index: int, target_state: State, target_transient: Transient) -> None:
		if assignment_index == 0:
			location = state.Machine_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.x_2 = 0
						target_state.Machine_location = 3
				elif transition == 1:
					if branch == 0:
						target_state.x_2 = 0
						target_state.Machine_location = 1
				elif transition == 2:
					if branch == 0:
						target_state.Machine_location = 0
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.x_2 = 0
						target_state.Machine_location = 2
				elif transition == 1:
					if branch == 0:
						target_state.x_2 = min((state.x_2 + 1), 51)
						target_state.Machine_location = 1
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.x_2 = 0
						target_state.Machine_location = 3
				elif transition == 1:
					if branch == 0:
						target_state.x_2 = 0
						target_state.Machine_location = 1
				elif transition == 2:
					if branch == 0:
						target_state.Machine_location = 2
			elif location == 3:
				if transition == 0:
					if branch == 0:
						target_state.x_2 = 0
						target_state.Machine_location = 2
				elif transition == 1:
					if branch == 0:
						target_state.x_2 = min((state.x_2 + 1), 51)
						target_state.Machine_location = 3

# Automaton: Machine
class MachineAutomaton_1(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [3, 2, 3, 2]
		self.transition_labels = [[11, 12, 23], [13, 23], [11, 12, 23], [14, 23]]
		self.branch_counts = [[1, 1, 1], [1, 1], [1, 1, 1], [1, 1]]
	
	def set_initial_values(self, state: State) -> None:
		state.Machine_location_1 = 0
		state.x_3 = 0
	
	def set_initial_transient_values(self, transient: Transient) -> None:
		pass
	
	def get_transient_value(self, state: State, transient_variable: str):
		location = state.Machine_location_1
		return None
	
	def get_transition_count(self, state: State) -> int:
		return self.transition_counts[state.Machine_location_1]
	
	def get_transition_label(self, state: State, transition: int) -> int:
		return self.transition_labels[state.Machine_location_1][transition]
	
	def get_guard_value(self, state: State, transition: int) -> bool:
		location = state.Machine_location_1
		if location == 0:
			if transition >= 0 and transition < 3:
				return True
		elif location == 1:
			if transition == 0:
				return (state.x_3 >= 70)
			elif transition == 1:
				return (state.x_3 < 100)
		elif location == 2:
			if transition >= 0 and transition < 3:
				return True
		elif location == 3:
			if transition == 0:
				return (state.x_3 >= 70)
			elif transition == 1:
				return (state.x_3 < 100)
	
	def get_branch_count(self, state: State, transition: int) -> int:
		return self.branch_counts[state.Machine_location_1][transition]
	
	def get_probability_value(self, state: State, transition: int, branch: int) -> float:
		location = state.Machine_location_1
		if location == 0:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
			elif transition == 2:
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
		elif location == 3:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
	
	def jump(self, state: State, transient: Transient, transition: int, branch: int, assignment_index: int, target_state: State, target_transient: Transient) -> None:
		if assignment_index == 0:
			location = state.Machine_location_1
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.x_3 = 0
						target_state.Machine_location_1 = 3
				elif transition == 1:
					if branch == 0:
						target_state.x_3 = 0
						target_state.Machine_location_1 = 1
				elif transition == 2:
					if branch == 0:
						target_state.Machine_location_1 = 0
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.x_3 = 0
						target_state.Machine_location_1 = 2
				elif transition == 1:
					if branch == 0:
						target_state.x_3 = min((state.x_3 + 1), 101)
						target_state.Machine_location_1 = 1
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.x_3 = 0
						target_state.Machine_location_1 = 3
				elif transition == 1:
					if branch == 0:
						target_state.x_3 = 0
						target_state.Machine_location_1 = 1
				elif transition == 2:
					if branch == 0:
						target_state.Machine_location_1 = 2
			elif location == 3:
				if transition == 0:
					if branch == 0:
						target_state.x_3 = 0
						target_state.Machine_location_1 = 2
				elif transition == 1:
					if branch == 0:
						target_state.x_3 = min((state.x_3 + 1), 101)
						target_state.Machine_location_1 = 3

# Automaton: GlobalSync
class GlobalSyncAutomaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [1]
		self.transition_labels = [[23]]
		self.branch_counts = [[1]]
	
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
			return True
	
	def get_branch_count(self, state: State, transition: int) -> int:
		return self.branch_counts[0][transition]
	
	def get_probability_value(self, state: State, transition: int, branch: int) -> float:
		location = 0
		if location == 0:
			if transition == 0:
				return 1
	
	def jump(self, state: State, transient: Transient, transition: int, branch: int, assignment_index: int, target_state: State, target_transient: Transient) -> None:
		if assignment_index == 0:
			location = 0
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.time = min((state.time + 1), 481)

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
	
	def __init__(self, sync_vector: int, label: int = 0, transitions: List[int] = [-1, -1, -1, -1, -1, -1]):
		self.sync_vector = sync_vector
		self.label = label
		self.transitions = transitions

class Branch(object):
	__slots__ = ("probability", "branches")
	
	def __init__(self, probability = 0.0, branches = [0, 0, 0, 0, 0, 0]):
		self.probability = probability
		self.branches = branches

class Network(object):
	__slots__ = ("network", "components", "transition_labels", "sync_vectors", "properties", "variables", "_initial_transient", "_aut_Worker", "_aut_Worker_1", "_aut_Factory", "_aut_Machine", "_aut_Machine_1", "_aut_GlobalSync")
	
	def __init__(self):
		self.network = self
		self.transition_labels = { 0: "τ", 1: "start_job", 2: "start_machine_1", 3: "start_machine_2", 4: "machine_2_done", 5: "job_done", 6: "machine_1_done", 7: "w1_start_job", 8: "w2_start_job", 9: "w1_job_done", 10: "w2_job_done", 11: "start_machine_by_w1", 12: "start_machine_by_w2", 13: "machine_done_by_w2", 14: "machine_done_by_w1", 15: "start_machine_1_by_w1", 16: "machine_1_done_by_w1", 17: "start_machine_2_by_w1", 18: "machine_2_done_by_w1", 19: "start_machine_1_by_w2", 20: "machine_1_done_by_w2", 21: "start_machine_2_by_w2", 22: "machine_2_done_by_w2", 23: "tick" }
		self.sync_vectors = [[0, -1, -1, -1, -1, -1, 0], [-1, 0, -1, -1, -1, -1, 0], [-1, -1, 0, -1, -1, -1, 0], [-1, -1, -1, 0, -1, -1, 0], [-1, -1, -1, -1, 0, -1, 0], [-1, -1, -1, -1, -1, 0, 0], [1, -1, 7, -1, -1, -1, 7], [5, -1, 9, -1, -1, -1, 9], [-1, 1, 8, -1, -1, -1, 8], [-1, 5, 10, -1, -1, -1, 10], [2, -1, -1, 11, -1, -1, 15], [6, -1, -1, 14, -1, -1, 16], [3, -1, -1, -1, 11, -1, 17], [4, -1, -1, -1, 14, -1, 18], [-1, 2, -1, 12, -1, -1, 19], [-1, 6, -1, 13, -1, -1, 20], [-1, 3, -1, -1, 12, -1, 21], [-1, 4, -1, -1, 13, -1, 22], [23, 23, 23, 23, 23, 23, 23]]
		self.properties = [Property("E_time", PropertyExpression("exists", [PropertyExpression("eventually", [PropertyExpression("ap", [0])])]))]
		self.variables = [VariableInfo("jobs_in_progress", None, "int", 0, 2), VariableInfo("jobs_done", None, "int", 0, 160), VariableInfo("had_lunch", None, None), VariableInfo("machine_1_available", None, "bool"), VariableInfo("machine_2_available", None, "bool"), VariableInfo("time", None, "int", 0, 481), VariableInfo("Worker_location", 0, "int", 0, 6), VariableInfo("x", 0, "int", 0, 31), VariableInfo("Worker_location", 1, "int", 0, 6), VariableInfo("x", 1, "int", 0, 31), VariableInfo("Factory_location", 2, "int", 0, 1), VariableInfo("Machine_location", 3, "int", 0, 3), VariableInfo("x", 3, "int", 0, 51), VariableInfo("Machine_location", 4, "int", 0, 3), VariableInfo("x", 4, "int", 0, 101)]
		self._aut_Worker = WorkerAutomaton(self)
		self._aut_Worker_1 = WorkerAutomaton_1(self)
		self._aut_Factory = FactoryAutomaton(self)
		self._aut_Machine = MachineAutomaton(self)
		self._aut_Machine_1 = MachineAutomaton_1(self)
		self._aut_GlobalSync = GlobalSyncAutomaton(self)
		self.components = [self._aut_Worker, self._aut_Worker_1, self._aut_Factory, self._aut_Machine, self._aut_Machine_1, self._aut_GlobalSync]
		self._initial_transient = self._get_initial_transient()
	
	def get_initial_state(self) -> State:
		state = State()
		state.jobs_in_progress = 0
		state.jobs_done = 0
		state.had_lunch = [False, False]
		state.machine_1_available = True
		state.machine_2_available = True
		state.time = 0
		self._aut_Worker.set_initial_values(state)
		self._aut_Worker_1.set_initial_values(state)
		self._aut_Factory.set_initial_values(state)
		self._aut_Machine.set_initial_values(state)
		self._aut_Machine_1.set_initial_values(state)
		self._aut_GlobalSync.set_initial_values(state)
		return state
	
	def _get_initial_transient(self) -> Transient:
		transient = Transient()
		self._aut_Worker.set_initial_transient_values(transient)
		self._aut_Worker_1.set_initial_transient_values(transient)
		self._aut_Factory.set_initial_transient_values(transient)
		self._aut_Machine.set_initial_transient_values(transient)
		self._aut_Machine_1.set_initial_transient_values(transient)
		self._aut_GlobalSync.set_initial_transient_values(transient)
		return transient
	
	def get_expression_value(self, state: State, expression: int):
		if expression == 0:
			return (((((state.time == 480) and (state.jobs_in_progress == 0)) and (state.jobs_done >= 12)) and (state.had_lunch)[0]) and (state.had_lunch)[1])
		else:
			raise IndexError
	
	def _get_jump_expression_value(self, state: State, transient: Transient, expression: int):
		if expression == 0:
			return (((((state.time == 480) and (state.jobs_in_progress == 0)) and (state.jobs_done >= 12)) and (state.had_lunch)[0]) and (state.had_lunch)[1])
		else:
			raise IndexError
	
	def _get_transient_value(self, state: State, transient_variable: str):
		# Query the automata for the current value of the transient variable
		result = self._aut_Worker.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		result = self._aut_Worker_1.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		result = self._aut_Factory.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		result = self._aut_Machine.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		result = self._aut_Machine_1.get_transient_value(state, transient_variable)
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
		trans_Worker = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
		transition_count = self._aut_Worker.get_transition_count(state)
		for i in range(transition_count):
			if self._aut_Worker.get_guard_value(state, i):
				trans_Worker[self._aut_Worker.get_transition_label(state, i)].append(i)
		trans_Worker_1 = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
		transition_count = self._aut_Worker_1.get_transition_count(state)
		for i in range(transition_count):
			if self._aut_Worker_1.get_guard_value(state, i):
				trans_Worker_1[self._aut_Worker_1.get_transition_label(state, i)].append(i)
		trans_Factory = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
		transition_count = self._aut_Factory.get_transition_count(state)
		for i in range(transition_count):
			if self._aut_Factory.get_guard_value(state, i):
				trans_Factory[self._aut_Factory.get_transition_label(state, i)].append(i)
		trans_Machine = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
		transition_count = self._aut_Machine.get_transition_count(state)
		for i in range(transition_count):
			if self._aut_Machine.get_guard_value(state, i):
				trans_Machine[self._aut_Machine.get_transition_label(state, i)].append(i)
		trans_Machine_1 = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
		transition_count = self._aut_Machine_1.get_transition_count(state)
		for i in range(transition_count):
			if self._aut_Machine_1.get_guard_value(state, i):
				trans_Machine_1[self._aut_Machine_1.get_transition_label(state, i)].append(i)
		trans_GlobalSync = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
		transition_count = self._aut_GlobalSync.get_transition_count(state)
		for i in range(transition_count):
			if self._aut_GlobalSync.get_guard_value(state, i):
				trans_GlobalSync[self._aut_GlobalSync.get_transition_label(state, i)].append(i)
		# Match automaton transitions onto synchronisation vectors
		for svi in range(len(self.sync_vectors)):
			sv = self.sync_vectors[svi]
			synced = [[-1, -1, -1, -1, -1, -1, -1]]
			# Worker
			if synced is not None:
				if sv[0] != -1:
					if len(trans_Worker[sv[0]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][0] = trans_Worker[sv[0]][0]
						for i in range(1, len(trans_Worker[sv[0]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][0] = trans_Worker[sv[0]][i]
			# Worker
			if synced is not None:
				if sv[1] != -1:
					if len(trans_Worker_1[sv[1]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][1] = trans_Worker_1[sv[1]][0]
						for i in range(1, len(trans_Worker_1[sv[1]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][1] = trans_Worker_1[sv[1]][i]
			# Factory
			if synced is not None:
				if sv[2] != -1:
					if len(trans_Factory[sv[2]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][2] = trans_Factory[sv[2]][0]
						for i in range(1, len(trans_Factory[sv[2]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][2] = trans_Factory[sv[2]][i]
			# Machine
			if synced is not None:
				if sv[3] != -1:
					if len(trans_Machine[sv[3]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][3] = trans_Machine[sv[3]][0]
						for i in range(1, len(trans_Machine[sv[3]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][3] = trans_Machine[sv[3]][i]
			# Machine
			if synced is not None:
				if sv[4] != -1:
					if len(trans_Machine_1[sv[4]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][4] = trans_Machine_1[sv[4]][0]
						for i in range(1, len(trans_Machine_1[sv[4]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][4] = trans_Machine_1[sv[4]][i]
			# GlobalSync
			if synced is not None:
				if sv[5] != -1:
					if len(trans_GlobalSync[sv[5]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][5] = trans_GlobalSync[sv[5]][0]
						for i in range(1, len(trans_GlobalSync[sv[5]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][5] = trans_GlobalSync[sv[5]][i]
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
		combs = [[-1, -1, -1, -1, -1, -1]]
		probs = [1.0]
		if transition.transitions[0] != -1:
			existing = len(combs)
			branch_count = self._aut_Worker.get_branch_count(state, transition.transitions[0])
			for i in range(1, branch_count):
				probability = self._aut_Worker.get_probability_value(state, transition.transitions[0], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][0] = i
					probs.append(probs[j] * probability)
			probability = self._aut_Worker.get_probability_value(state, transition.transitions[0], 0)
			for i in range(existing):
				combs[i][0] = 0
				probs[i] *= probability
		if transition.transitions[1] != -1:
			existing = len(combs)
			branch_count = self._aut_Worker_1.get_branch_count(state, transition.transitions[1])
			for i in range(1, branch_count):
				probability = self._aut_Worker_1.get_probability_value(state, transition.transitions[1], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][1] = i
					probs.append(probs[j] * probability)
			probability = self._aut_Worker_1.get_probability_value(state, transition.transitions[1], 0)
			for i in range(existing):
				combs[i][1] = 0
				probs[i] *= probability
		if transition.transitions[2] != -1:
			existing = len(combs)
			branch_count = self._aut_Factory.get_branch_count(state, transition.transitions[2])
			for i in range(1, branch_count):
				probability = self._aut_Factory.get_probability_value(state, transition.transitions[2], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][2] = i
					probs.append(probs[j] * probability)
			probability = self._aut_Factory.get_probability_value(state, transition.transitions[2], 0)
			for i in range(existing):
				combs[i][2] = 0
				probs[i] *= probability
		if transition.transitions[3] != -1:
			existing = len(combs)
			branch_count = self._aut_Machine.get_branch_count(state, transition.transitions[3])
			for i in range(1, branch_count):
				probability = self._aut_Machine.get_probability_value(state, transition.transitions[3], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][3] = i
					probs.append(probs[j] * probability)
			probability = self._aut_Machine.get_probability_value(state, transition.transitions[3], 0)
			for i in range(existing):
				combs[i][3] = 0
				probs[i] *= probability
		if transition.transitions[4] != -1:
			existing = len(combs)
			branch_count = self._aut_Machine_1.get_branch_count(state, transition.transitions[4])
			for i in range(1, branch_count):
				probability = self._aut_Machine_1.get_probability_value(state, transition.transitions[4], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][4] = i
					probs.append(probs[j] * probability)
			probability = self._aut_Machine_1.get_probability_value(state, transition.transitions[4], 0)
			for i in range(existing):
				combs[i][4] = 0
				probs[i] *= probability
		if transition.transitions[5] != -1:
			existing = len(combs)
			branch_count = self._aut_GlobalSync.get_branch_count(state, transition.transitions[5])
			for i in range(1, branch_count):
				probability = self._aut_GlobalSync.get_probability_value(state, transition.transitions[5], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][5] = i
					probs.append(probs[j] * probability)
			probability = self._aut_GlobalSync.get_probability_value(state, transition.transitions[5], 0)
			for i in range(existing):
				combs[i][5] = 0
				probs[i] *= probability
		# Convert to Branch instances
		for i in range(len(combs)):
			combs[i] = Branch(probs[i], combs[i])
		# Done
		return list(filter(lambda b: b.probability > 0.0, combs))
	
	def jump(self, state: State, transition: Transition, branch: Branch, expressions: List[int] = []) -> State:
		transient = self._get_initial_transient()
		for i in range(0, 1):
			target_state = State()
			state.copy_to(target_state)
			target_transient = Transient()
			transient.copy_to(target_transient)
			if transition.transitions[0] != -1:
				self._aut_Worker.jump(state, transient, transition.transitions[0], branch.branches[0], i, target_state, target_transient)
			if transition.transitions[1] != -1:
				self._aut_Worker_1.jump(state, transient, transition.transitions[1], branch.branches[1], i, target_state, target_transient)
			if transition.transitions[2] != -1:
				self._aut_Factory.jump(state, transient, transition.transitions[2], branch.branches[2], i, target_state, target_transient)
			if transition.transitions[3] != -1:
				self._aut_Machine.jump(state, transient, transition.transitions[3], branch.branches[3], i, target_state, target_transient)
			if transition.transitions[4] != -1:
				self._aut_Machine_1.jump(state, transient, transition.transitions[4], branch.branches[4], i, target_state, target_transient)
			if transition.transitions[5] != -1:
				self._aut_GlobalSync.jump(state, transient, transition.transitions[5], branch.branches[5], i, target_state, target_transient)
			state = target_state
			transient = target_transient
		for i in range(len(expressions)):
			expressions[i] = self._get_jump_expression_value(state, transient, expressions[i])
		return state
	
	def jump_np(self, state: State, transition: Transition, expressions: List[int] = []) -> State:
		return self.jump(state, transition, self.get_branches(state, transition)[0], expressions)
