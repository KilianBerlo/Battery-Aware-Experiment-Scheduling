# jobshop_lunch_Xmin

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
	__slots__ = ("jobs_in_progress", "jobs_done", "had_lunch", "success", "time", "Worker_location", "x", "Machine_location", "x_1")
	
	def get_variable_value(self, variable: int):
		if variable == 0:
			return self.jobs_in_progress
		elif variable == 1:
			return self.jobs_done
		elif variable == 2:
			return self.had_lunch
		elif variable == 3:
			return self.success
		elif variable == 4:
			return self.time
		elif variable == 5:
			return self.Worker_location
		elif variable == 6:
			return self.x
		elif variable == 7:
			return self.Machine_location
		elif variable == 8:
			return self.x_1
	
	def copy_to(self, other: State):
		other.jobs_in_progress = self.jobs_in_progress
		other.jobs_done = self.jobs_done
		other.had_lunch = self.had_lunch
		other.success = self.success
		other.time = self.time
		other.Worker_location = self.Worker_location
		other.x = self.x
		other.Machine_location = self.Machine_location
		other.x_1 = self.x_1
	
	def __eq__(self, other):
		return isinstance(other, self.__class__) and self.jobs_in_progress == other.jobs_in_progress and self.jobs_done == other.jobs_done and self.had_lunch == other.had_lunch and self.success == other.success and self.time == other.time and self.Worker_location == other.Worker_location and self.x == other.x and self.Machine_location == other.Machine_location and self.x_1 == other.x_1
	
	def __ne__(self, other):
		return not self.__eq__(other)
	
	def __hash__(self):
		result = 75619
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.jobs_in_progress)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.jobs_done)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.had_lunch)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.success)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.time)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.Worker_location)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.x)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.Machine_location)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.x_1)) & 0xFFFFFFFF
		return result
	
	def __str__(self):
		result = "("
		result += "jobs_in_progress = " + str(self.jobs_in_progress)
		result += ", jobs_done = " + str(self.jobs_done)
		result += ", had_lunch = " + str(self.had_lunch)
		result += ", success = " + str(self.success)
		result += ", time = " + str(self.time)
		result += ", Worker_location = " + str(self.Worker_location)
		result += ", x = " + str(self.x)
		result += ", Machine_location = " + str(self.Machine_location)
		result += ", x_1 = " + str(self.x_1)
		result += ")"
		return result

# Transients
class Transient(object):
	__slots__ = ("R_Succ_jobsdone_edge_reward", "activate")
	
	def copy_to(self, other: Transient):
		other.R_Succ_jobsdone_edge_reward = self.R_Succ_jobsdone_edge_reward
		other.activate = self.activate
	
	def __eq__(self, other):
		return isinstance(other, self.__class__) and self.R_Succ_jobsdone_edge_reward == other.R_Succ_jobsdone_edge_reward and self.activate == other.activate
	
	def __ne__(self, other):
		return not self.__eq__(other)
	
	def __hash__(self):
		result = 75619
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.R_Succ_jobsdone_edge_reward)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.activate)) & 0xFFFFFFFF
		return result
	
	def __str__(self):
		result = "("
		result += "R_Succ_jobsdone_edge_reward = " + str(self.R_Succ_jobsdone_edge_reward)
		result += ", activate = " + str(self.activate)
		result += ")"
		return result

# Automaton: Worker
class WorkerAutomaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [2, 1, 2, 1, 2]
		self.transition_labels = [[6, 1], [2], [3, 5], [4], [6, 5]]
		self.branch_counts = [[1, 1], [1], [1, 1], [1], [1, 1]]
	
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
		if location == 1 or location == 3:
			return True
		elif location == 0:
			if transition == 0:
				return (((not state.had_lunch) and (state.time >= 180)) and (state.time <= 300))
			elif transition == 1:
				return True
		elif location == 2:
			if transition >= 0 and transition < 2:
				return True
		elif location == 4:
			if transition == 0:
				return (state.x >= 30)
			elif transition == 1:
				return (state.x < 30)
	
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
	
	def jump(self, state: State, transient: Transient, transition: int, branch: int, assignment_index: int, target_state: State, target_transient: Transient) -> None:
		if assignment_index == 0:
			location = state.Worker_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.x = 0
			elif location == 4:
				if transition == 0:
					if branch == 0:
						target_state.had_lunch = True
						target_state.x = 0
				elif transition == 1:
					if branch == 0:
						target_state.x = min((state.x + 1), 31)
		elif assignment_index == 2:
			location = state.Worker_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.Worker_location = 4
				elif transition == 1:
					if branch == 0:
						target_state.Worker_location = 1
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.Worker_location = 2
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.Worker_location = 3
				elif transition == 1:
					if branch == 0:
						target_state.Worker_location = 2
			elif location == 3:
				if transition == 0:
					if branch == 0:
						target_state.Worker_location = 0
			elif location == 4:
				if transition == 0:
					if branch == 0:
						target_state.Worker_location = 0
				elif transition == 1:
					if branch == 0:
						target_state.Worker_location = 4

# Automaton: Factory
class FactoryAutomaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [4]
		self.transition_labels = [[1, 4, 4, 5]]
		self.branch_counts = [[1, 1, 1, 1]]
	
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
			if transition == 0:
				return True
			elif transition == 1:
				return (state.jobs_done == 160)
			elif transition == 2:
				return (state.jobs_done <= 159)
			elif transition == 3:
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
			elif transition == 2:
				return 1
			elif transition == 3:
				return 1
	
	def jump(self, state: State, transient: Transient, transition: int, branch: int, assignment_index: int, target_state: State, target_transient: Transient) -> None:
		if assignment_index == 0:
			location = 0
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.jobs_in_progress = (state.jobs_in_progress + 1)
						if target_state.jobs_in_progress > 1:
							raise OverflowError("Assigned value of " + str(target_state.jobs_in_progress) + " is greater than the upper bound of 1 for variable \"jobs_in_progress\".")
				elif transition == 1:
					if branch == 0:
						target_state.jobs_in_progress = (state.jobs_in_progress - 1)
						if target_state.jobs_in_progress < 0:
							raise OverflowError("Assigned value of " + str(target_state.jobs_in_progress) + " is less than the lower bound of 0 for variable \"jobs_in_progress\".")
						target_state.success = True
				elif transition == 2:
					if branch == 0:
						target_state.jobs_done = (state.jobs_done + 1)
						if target_state.jobs_done > 160:
							raise OverflowError("Assigned value of " + str(target_state.jobs_done) + " is greater than the upper bound of 160 for variable \"jobs_done\".")
						target_state.jobs_in_progress = (state.jobs_in_progress - 1)
						if target_state.jobs_in_progress < 0:
							raise OverflowError("Assigned value of " + str(target_state.jobs_in_progress) + " is less than the lower bound of 0 for variable \"jobs_in_progress\".")
		elif assignment_index == 2:
			location = 0
			if location == 0:
				if transition == 0:
					if branch == 0:
						pass
				elif transition == 1:
					if branch == 0:
						pass
				elif transition == 2:
					if branch == 0:
						pass
				elif transition == 3:
					if branch == 0:
						pass

# Automaton: Machine
class MachineAutomaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [2, 2]
		self.transition_labels = [[2, 5], [3, 5]]
		self.branch_counts = [[1, 1], [1, 1]]
	
	def set_initial_values(self, state: State) -> None:
		state.Machine_location = 0
		state.x_1 = 0
	
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
			if transition >= 0 and transition < 2:
				return True
		elif location == 1:
			if transition == 0:
				return (state.x_1 >= 40)
			elif transition == 1:
				return (state.x_1 < 50)
	
	def get_branch_count(self, state: State, transition: int) -> int:
		return self.branch_counts[state.Machine_location][transition]
	
	def get_probability_value(self, state: State, transition: int, branch: int) -> float:
		location = state.Machine_location
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
	
	def jump(self, state: State, transient: Transient, transition: int, branch: int, assignment_index: int, target_state: State, target_transient: Transient) -> None:
		if assignment_index == 0:
			location = state.Machine_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.x_1 = 0
						target_transient.activate = 1
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.x_1 = 0
				elif transition == 1:
					if branch == 0:
						target_state.x_1 = min((state.x_1 + 1), 51)
		elif assignment_index == 2:
			location = state.Machine_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.Machine_location = 1
				elif transition == 1:
					if branch == 0:
						target_state.Machine_location = 0
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.Machine_location = 0
				elif transition == 1:
					if branch == 0:
						target_state.Machine_location = 1

# Automaton: GlobalSync
class GlobalSyncAutomaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [2]
		self.transition_labels = [[5, 6]]
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
						target_state.time = min((state.time + 1), 481)
		elif assignment_index == 2:
			location = 0
			if location == 0:
				if transition == 0:
					if branch == 0:
						pass
				elif transition == 1:
					if branch == 0:
						target_transient.R_Succ_jobsdone_edge_reward = transient.activate

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
	
	def __init__(self, sync_vector: int, label: int = 0, transitions: List[int] = [-1, -1, -1, -1]):
		self.sync_vector = sync_vector
		self.label = label
		self.transitions = transitions

class Branch(object):
	__slots__ = ("probability", "branches")
	
	def __init__(self, probability = 0.0, branches = [0, 0, 0, 0]):
		self.probability = probability
		self.branches = branches

class Network(object):
	__slots__ = ("network", "components", "transition_labels", "sync_vectors", "properties", "variables", "_initial_transient", "_aut_Worker", "_aut_Factory", "_aut_Machine", "_aut_GlobalSync")
	
	def __init__(self):
		self.network = self
		self.transition_labels = { 0: "τ", 1: "start_job", 2: "start_machine", 3: "machine_done", 4: "job_done", 5: "tick", 6: "tau" }
		self.sync_vectors = [[0, -1, -1, -1, 0], [-1, 0, -1, -1, 0], [-1, -1, 0, -1, 0], [-1, -1, -1, 0, 0], [1, 1, -1, 6, 1], [4, 4, -1, 6, 4], [2, -1, 2, 6, 2], [3, -1, 3, 6, 3], [6, -1, -1, 6, 0], [5, 5, 5, 5, 5]]
		self.properties = [Property("E_time", PropertyExpression("exists", [PropertyExpression("eventually", [PropertyExpression("ap", [0])])])), Property("R_Succ_jobsdone", PropertyExpression("xmin", [1, PropertyExpression("ap", [2])]))]
		self.variables = [VariableInfo("jobs_in_progress", None, "int", 0, 1), VariableInfo("jobs_done", None, "int", 0, 160), VariableInfo("had_lunch", None, "bool"), VariableInfo("success", None, "bool"), VariableInfo("time", None, "int", 0, 481), VariableInfo("Worker_location", 0, "int", 0, 4), VariableInfo("x", 0, "int", 0, 31), VariableInfo("Machine_location", 2, "int", 0, 1), VariableInfo("x", 2, "int", 0, 51)]
		self._aut_Worker = WorkerAutomaton(self)
		self._aut_Factory = FactoryAutomaton(self)
		self._aut_Machine = MachineAutomaton(self)
		self._aut_GlobalSync = GlobalSyncAutomaton(self)
		self.components = [self._aut_Worker, self._aut_Factory, self._aut_Machine, self._aut_GlobalSync]
		self._initial_transient = self._get_initial_transient()
	
	def get_initial_state(self) -> State:
		state = State()
		state.jobs_in_progress = 0
		state.jobs_done = 0
		state.had_lunch = False
		state.success = False
		state.time = 0
		self._aut_Worker.set_initial_values(state)
		self._aut_Factory.set_initial_values(state)
		self._aut_Machine.set_initial_values(state)
		self._aut_GlobalSync.set_initial_values(state)
		return state
	
	def _get_initial_transient(self) -> Transient:
		transient = Transient()
		transient.R_Succ_jobsdone_edge_reward = 0
		transient.activate = 0
		self._aut_Worker.set_initial_transient_values(transient)
		self._aut_Factory.set_initial_transient_values(transient)
		self._aut_Machine.set_initial_transient_values(transient)
		self._aut_GlobalSync.set_initial_transient_values(transient)
		return transient
	
	def get_expression_value(self, state: State, expression: int):
		if expression == 0:
			return ((((state.time == 480) and (state.jobs_in_progress == 0)) and (state.jobs_done >= 11)) and state.had_lunch)
		elif expression == 1:
			return self.network._get_transient_value(state, "R_Succ_jobsdone_edge_reward")
		elif expression == 2:
			return state.success
		else:
			raise IndexError
	
	def _get_jump_expression_value(self, state: State, transient: Transient, expression: int):
		if expression == 0:
			return ((((state.time == 480) and (state.jobs_in_progress == 0)) and (state.jobs_done >= 11)) and state.had_lunch)
		elif expression == 1:
			return transient.R_Succ_jobsdone_edge_reward
		elif expression == 2:
			return state.success
		else:
			raise IndexError
	
	def _get_transient_value(self, state: State, transient_variable: str):
		# Query the automata for the current value of the transient variable
		result = self._aut_Worker.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		result = self._aut_Factory.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		result = self._aut_Machine.get_transient_value(state, transient_variable)
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
		trans_Worker = [[], [], [], [], [], [], []]
		transition_count = self._aut_Worker.get_transition_count(state)
		for i in range(transition_count):
			if self._aut_Worker.get_guard_value(state, i):
				trans_Worker[self._aut_Worker.get_transition_label(state, i)].append(i)
		trans_Factory = [[], [], [], [], [], [], []]
		transition_count = self._aut_Factory.get_transition_count(state)
		for i in range(transition_count):
			if self._aut_Factory.get_guard_value(state, i):
				trans_Factory[self._aut_Factory.get_transition_label(state, i)].append(i)
		trans_Machine = [[], [], [], [], [], [], []]
		transition_count = self._aut_Machine.get_transition_count(state)
		for i in range(transition_count):
			if self._aut_Machine.get_guard_value(state, i):
				trans_Machine[self._aut_Machine.get_transition_label(state, i)].append(i)
		trans_GlobalSync = [[], [], [], [], [], [], []]
		transition_count = self._aut_GlobalSync.get_transition_count(state)
		for i in range(transition_count):
			if self._aut_GlobalSync.get_guard_value(state, i):
				trans_GlobalSync[self._aut_GlobalSync.get_transition_label(state, i)].append(i)
		# Match automaton transitions onto synchronisation vectors
		for svi in range(len(self.sync_vectors)):
			sv = self.sync_vectors[svi]
			synced = [[-1, -1, -1, -1, -1]]
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
			# Factory
			if synced is not None:
				if sv[1] != -1:
					if len(trans_Factory[sv[1]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][1] = trans_Factory[sv[1]][0]
						for i in range(1, len(trans_Factory[sv[1]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][1] = trans_Factory[sv[1]][i]
			# Machine
			if synced is not None:
				if sv[2] != -1:
					if len(trans_Machine[sv[2]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][2] = trans_Machine[sv[2]][0]
						for i in range(1, len(trans_Machine[sv[2]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][2] = trans_Machine[sv[2]][i]
			# GlobalSync
			if synced is not None:
				if sv[3] != -1:
					if len(trans_GlobalSync[sv[3]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][3] = trans_GlobalSync[sv[3]][0]
						for i in range(1, len(trans_GlobalSync[sv[3]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][3] = trans_GlobalSync[sv[3]][i]
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
		combs = [[-1, -1, -1, -1]]
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
			branch_count = self._aut_Factory.get_branch_count(state, transition.transitions[1])
			for i in range(1, branch_count):
				probability = self._aut_Factory.get_probability_value(state, transition.transitions[1], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][1] = i
					probs.append(probs[j] * probability)
			probability = self._aut_Factory.get_probability_value(state, transition.transitions[1], 0)
			for i in range(existing):
				combs[i][1] = 0
				probs[i] *= probability
		if transition.transitions[2] != -1:
			existing = len(combs)
			branch_count = self._aut_Machine.get_branch_count(state, transition.transitions[2])
			for i in range(1, branch_count):
				probability = self._aut_Machine.get_probability_value(state, transition.transitions[2], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][2] = i
					probs.append(probs[j] * probability)
			probability = self._aut_Machine.get_probability_value(state, transition.transitions[2], 0)
			for i in range(existing):
				combs[i][2] = 0
				probs[i] *= probability
		if transition.transitions[3] != -1:
			existing = len(combs)
			branch_count = self._aut_GlobalSync.get_branch_count(state, transition.transitions[3])
			for i in range(1, branch_count):
				probability = self._aut_GlobalSync.get_probability_value(state, transition.transitions[3], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][3] = i
					probs.append(probs[j] * probability)
			probability = self._aut_GlobalSync.get_probability_value(state, transition.transitions[3], 0)
			for i in range(existing):
				combs[i][3] = 0
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
				self._aut_Worker.jump(state, transient, transition.transitions[0], branch.branches[0], i, target_state, target_transient)
			if transition.transitions[1] != -1:
				self._aut_Factory.jump(state, transient, transition.transitions[1], branch.branches[1], i, target_state, target_transient)
			if transition.transitions[2] != -1:
				self._aut_Machine.jump(state, transient, transition.transitions[2], branch.branches[2], i, target_state, target_transient)
			if transition.transitions[3] != -1:
				self._aut_GlobalSync.jump(state, transient, transition.transitions[3], branch.branches[3], i, target_state, target_transient)
			state = target_state
			transient = target_transient
		for i in range(len(expressions)):
			expressions[i] = self._get_jump_expression_value(state, transient, expressions[i])
		return state
	
	def jump_np(self, state: State, transition: Transition, expressions: List[int] = []) -> State:
		return self.jump(state, transition, self.get_branches(state, transition)[0], expressions)
