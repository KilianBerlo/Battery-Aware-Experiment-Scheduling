# traingate

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
	__slots__ = ("closed", "at_crossing", "Train_location", "t", "Gate_location", "c", "Controller_location")

	def get_variable_value(self, variable: int):
		if variable == 0:
			return self.closed
		elif variable == 1:
			return self.at_crossing
		elif variable == 2:
			return self.Train_location
		elif variable == 3:
			return self.t
		elif variable == 4:
			return self.Gate_location
		elif variable == 5:
			return self.c
		elif variable == 6:
			return self.Controller_location

	def copy_to(self, other: State):
		other.closed = self.closed
		other.at_crossing = self.at_crossing
		other.Train_location = self.Train_location
		other.t = self.t
		other.Gate_location = self.Gate_location
		other.c = self.c
		other.Controller_location = self.Controller_location

	def __eq__(self, other):
		return isinstance(other, self.__class__) and self.closed == other.closed and self.at_crossing == other.at_crossing and self.Train_location == other.Train_location and self.t == other.t and self.Gate_location == other.Gate_location and self.c == other.c and self.Controller_location == other.Controller_location

	def __ne__(self, other):
		return not self.__eq__(other)

	def __hash__(self):
		result = 75619
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.closed)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.at_crossing)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.Train_location)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.t)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.Gate_location)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.c)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.Controller_location)) & 0xFFFFFFFF
		return result

	def __str__(self):
		result = "("
		result += "closed = " + str(self.closed)
		result += ", at_crossing = " + str(self.at_crossing)
		result += ", Train_location = " + str(self.Train_location)
		result += ", t = " + str(self.t)
		result += ", Gate_location = " + str(self.Gate_location)
		result += ", c = " + str(self.c)
		result += ", Controller_location = " + str(self.Controller_location)
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

# Automaton: Train
class TrainAutomaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")

	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [2, 2, 2]
		self.transition_labels = [[1, 5], [0, 5], [2, 5]]
		self.branch_counts = [[1, 1], [1, 1], [1, 1]]

	def set_initial_values(self, state: State) -> None:
		state.Train_location = 0
		state.t = 0

	def set_initial_transient_values(self, transient: Transient) -> None:
		pass

	def get_transient_value(self, state: State, transient_variable: str):
		location = state.Train_location
		return None

	def get_transition_count(self, state: State) -> int:
		return self.transition_counts[state.Train_location]

	def get_transition_label(self, state: State, transition: int) -> int:
		return self.transition_labels[state.Train_location][transition]

	def get_guard_value(self, state: State, transition: int) -> bool:
		location = state.Train_location
		if location == 0:
			if transition == 0:
				return (state.t >= 4)
			elif transition == 1:
				return (state.t < 30)
		elif location == 1:
			if transition == 0:
				return (state.t >= 7)
			elif transition == 1:
				return (state.t < 42)
		elif location == 2:
			if transition == 0:
				return True
			elif transition == 1:
				return (state.t < 10)

	def get_branch_count(self, state: State, transition: int) -> int:
		return self.branch_counts[state.Train_location][transition]

	def get_probability_value(self, state: State, transition: int, branch: int) -> float:
		location = state.Train_location
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

	def jump(self, state: State, transient: Transient, transition: int, branch: int, assignment_index: int, target_state: State, target_transient: Transient) -> None:
		if assignment_index == 0:
			location = state.Train_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.t = 0
				elif transition == 1:
					if branch == 0:
						target_state.t = min((state.t + 1), 43)
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.t = 0
						target_state.at_crossing = True
				elif transition == 1:
					if branch == 0:
						target_state.t = min((state.t + 1), 43)
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.at_crossing = False
				elif transition == 1:
					if branch == 0:
						target_state.t = min((state.t + 1), 43)
		elif assignment_index == 1:
			location = state.Train_location
			if location == 2:
				if transition == 0:
					if branch == 0:
						target_state.t = 0
		elif assignment_index == 3:
			location = state.Train_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.Train_location = 1
				elif transition == 1:
					if branch == 0:
						target_state.Train_location = 0
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.Train_location = 2
				elif transition == 1:
					if branch == 0:
						target_state.Train_location = 1
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.Train_location = 0
				elif transition == 1:
					if branch == 0:
						target_state.Train_location = 2

# Automaton: Gate
class GateAutomaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")

	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [2, 2, 2, 2]
		self.transition_labels = [[3, 5], [0, 5], [4, 5], [0, 5]]
		self.branch_counts = [[1, 1], [1, 1], [1, 1], [1, 1]]

	def set_initial_values(self, state: State) -> None:
		state.Gate_location = 0
		state.c = 0

	def set_initial_transient_values(self, transient: Transient) -> None:
		pass

	def get_transient_value(self, state: State, transient_variable: str):
		location = state.Gate_location
		return None

	def get_transition_count(self, state: State) -> int:
		return self.transition_counts[state.Gate_location]

	def get_transition_label(self, state: State, transition: int) -> int:
		return self.transition_labels[state.Gate_location][transition]

	def get_guard_value(self, state: State, transition: int) -> bool:
		location = state.Gate_location
		if location == 0:
			if transition >= 0 and transition < 2:
				return True
		elif location == 1:
			if transition == 0:
				return (state.c >= 6)
			elif transition == 1:
				return (state.c < 6)
		elif location == 2:
			if transition >= 0 and transition < 2:
				return True
		elif location == 3:
			if transition == 0:
				return (state.c >= 4)
			elif transition == 1:
				return (state.c < 4)

	def get_branch_count(self, state: State, transition: int) -> int:
		return self.branch_counts[state.Gate_location][transition]

	def get_probability_value(self, state: State, transition: int, branch: int) -> float:
		location = state.Gate_location
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
			elif transition == 1:
				return 1

	def jump(self, state: State, transient: Transient, transition: int, branch: int, assignment_index: int, target_state: State, target_transient: Transient) -> None:
		if assignment_index == 0:
			location = state.Gate_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.c = 0
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.closed = True
				elif transition == 1:
					if branch == 0:
						target_state.c = min((state.c + 1), 7)
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.c = 0
			elif location == 3:
				if transition == 0:
					if branch == 0:
						target_state.closed = False
						target_state.c = 0
				elif transition == 1:
					if branch == 0:
						target_state.c = min((state.c + 1), 7)
		elif assignment_index == 3:
			location = state.Gate_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.Gate_location = 1
				elif transition == 1:
					if branch == 0:
						target_state.Gate_location = 0
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.c = 0
						target_state.Gate_location = 2
				elif transition == 1:
					if branch == 0:
						target_state.Gate_location = 1
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.Gate_location = 3
				elif transition == 1:
					if branch == 0:
						target_state.Gate_location = 2
			elif location == 3:
				if transition == 0:
					if branch == 0:
						target_state.Gate_location = 0
				elif transition == 1:
					if branch == 0:
						target_state.Gate_location = 3

# Automaton: Controller
class ControllerAutomaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")

	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [2, 1, 2, 1]
		self.transition_labels = [[1, 5], [3], [2, 5], [4]]
		self.branch_counts = [[1, 1], [1], [1, 1], [1]]

	def set_initial_values(self, state: State) -> None:
		state.Controller_location = 0

	def set_initial_transient_values(self, transient: Transient) -> None:
		pass

	def get_transient_value(self, state: State, transient_variable: str):
		location = state.Controller_location
		return None

	def get_transition_count(self, state: State) -> int:
		return self.transition_counts[state.Controller_location]

	def get_transition_label(self, state: State, transition: int) -> int:
		return self.transition_labels[state.Controller_location][transition]

	def get_guard_value(self, state: State, transition: int) -> bool:
		location = state.Controller_location
		if location == 1 or location == 3:
			return True
		elif location == 0:
			if transition >= 0 and transition < 2:
				return True
		elif location == 2:
			if transition >= 0 and transition < 2:
				return True

	def get_branch_count(self, state: State, transition: int) -> int:
		return self.branch_counts[state.Controller_location][transition]

	def get_probability_value(self, state: State, transition: int, branch: int) -> float:
		location = state.Controller_location
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

	def jump(self, state: State, transient: Transient, transition: int, branch: int, assignment_index: int, target_state: State, target_transient: Transient) -> None:
		if assignment_index == 3:
			location = state.Controller_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.Controller_location = 1
				elif transition == 1:
					if branch == 0:
						target_state.Controller_location = 0
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.Controller_location = 2
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.Controller_location = 3
				elif transition == 1:
					if branch == 0:
						target_state.Controller_location = 2
			elif location == 3:
				if transition == 0:
					if branch == 0:
						target_state.Controller_location = 0

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

	def __init__(self, sync_vector: int, label: int = 0, transitions: List[int] = [-1, -1, -1]):
		self.sync_vector = sync_vector
		self.label = label
		self.transitions = transitions

class Branch(object):
	__slots__ = ("probability", "branches")

	def __init__(self, probability = 0.0, branches = [0, 0, 0]):
		self.probability = probability
		self.branches = branches

class Network(object):
	__slots__ = ("network", "components", "transition_labels", "sync_vectors", "properties", "variables", "_initial_transient", "_aut_Train", "_aut_Gate", "_aut_Controller")

	def __init__(self):
		self.network = self
		self.transition_labels = { 0: "τ", 1: "approaching", 2: "leave", 3: "close", 4: "open", 5: "tick" }
		self.sync_vectors = [[0, -1, -1, 0], [-1, 0, -1, 0], [-1, -1, 0, 0], [1, -1, 1, 1], [2, -1, 2, 2], [-1, 3, 3, 3], [-1, 4, 4, 4], [5, 5, 5, 5]]
		self.properties = [Property("E_Safe", PropertyExpression("exists", [PropertyExpression("eventually", [PropertyExpression("ap", [0])])]))]
		self.variables = [VariableInfo("closed", None, "bool"), VariableInfo("at_crossing", None, "bool"), VariableInfo("Train_location", 0, "int", 0, 2), VariableInfo("t", 0, "int", 0, 43), VariableInfo("Gate_location", 1, "int", 0, 3), VariableInfo("c", 1, "int", 0, 7), VariableInfo("Controller_location", 2, "int", 0, 3)]
		self._aut_Train = TrainAutomaton(self)
		self._aut_Gate = GateAutomaton(self)
		self._aut_Controller = ControllerAutomaton(self)
		self.components = [self._aut_Train, self._aut_Gate, self._aut_Controller]
		self._initial_transient = self._get_initial_transient()

	def get_initial_state(self) -> State:
		state = State()
		state.closed = False
		state.at_crossing = False
		self._aut_Train.set_initial_values(state)
		self._aut_Gate.set_initial_values(state)
		self._aut_Controller.set_initial_values(state)
		return state

	def _get_initial_transient(self) -> Transient:
		transient = Transient()
		self._aut_Train.set_initial_transient_values(transient)
		self._aut_Gate.set_initial_transient_values(transient)
		self._aut_Controller.set_initial_transient_values(transient)
		return transient

	def get_expression_value(self, state: State, expression: int):
		if expression == 0:
			return (state.at_crossing and (not state.closed))
		else:
			raise IndexError

	def _get_jump_expression_value(self, state: State, transient: Transient, expression: int):
		if expression == 0:
			return (state.at_crossing and (not state.closed))
		else:
			raise IndexError

	def _get_transient_value(self, state: State, transient_variable: str):
		# Query the automata for the current value of the transient variable
		result = self._aut_Train.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		result = self._aut_Gate.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		result = self._aut_Controller.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		# No automaton has a value: return the transient variable's (cached) initial value
		return getattr(self._initial_transient, transient_variable)

	def get_transitions(self, state: State) -> List[Transition]:
		# Collect all automaton transitions, gathered by label
		transitions = []
		trans_Train = [[], [], [], [], [], []]
		transition_count = self._aut_Train.get_transition_count(state)
		for i in range(transition_count):
			if self._aut_Train.get_guard_value(state, i):
				trans_Train[self._aut_Train.get_transition_label(state, i)].append(i)
		trans_Gate = [[], [], [], [], [], []]
		transition_count = self._aut_Gate.get_transition_count(state)
		for i in range(transition_count):
			if self._aut_Gate.get_guard_value(state, i):
				trans_Gate[self._aut_Gate.get_transition_label(state, i)].append(i)
		trans_Controller = [[], [], [], [], [], []]
		transition_count = self._aut_Controller.get_transition_count(state)
		for i in range(transition_count):
			if self._aut_Controller.get_guard_value(state, i):
				trans_Controller[self._aut_Controller.get_transition_label(state, i)].append(i)
		# Match automaton transitions onto synchronisation vectors
		for svi in range(len(self.sync_vectors)):
			sv = self.sync_vectors[svi]
			synced = [[-1, -1, -1, -1]]
			# Train
			if synced is not None:
				if sv[0] != -1:
					if len(trans_Train[sv[0]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][0] = trans_Train[sv[0]][0]
						for i in range(1, len(trans_Train[sv[0]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][0] = trans_Train[sv[0]][i]
			# Gate
			if synced is not None:
				if sv[1] != -1:
					if len(trans_Gate[sv[1]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][1] = trans_Gate[sv[1]][0]
						for i in range(1, len(trans_Gate[sv[1]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][1] = trans_Gate[sv[1]][i]
			# Controller
			if synced is not None:
				if sv[2] != -1:
					if len(trans_Controller[sv[2]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][2] = trans_Controller[sv[2]][0]
						for i in range(1, len(trans_Controller[sv[2]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][2] = trans_Controller[sv[2]][i]
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
		combs = [[-1, -1, -1]]
		probs = [1.0]
		if transition.transitions[0] != -1:
			existing = len(combs)
			branch_count = self._aut_Train.get_branch_count(state, transition.transitions[0])
			for i in range(1, branch_count):
				probability = self._aut_Train.get_probability_value(state, transition.transitions[0], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][0] = i
					probs.append(probs[j] * probability)
			probability = self._aut_Train.get_probability_value(state, transition.transitions[0], 0)
			for i in range(existing):
				combs[i][0] = 0
				probs[i] *= probability
		if transition.transitions[1] != -1:
			existing = len(combs)
			branch_count = self._aut_Gate.get_branch_count(state, transition.transitions[1])
			for i in range(1, branch_count):
				probability = self._aut_Gate.get_probability_value(state, transition.transitions[1], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][1] = i
					probs.append(probs[j] * probability)
			probability = self._aut_Gate.get_probability_value(state, transition.transitions[1], 0)
			for i in range(existing):
				combs[i][1] = 0
				probs[i] *= probability
		if transition.transitions[2] != -1:
			existing = len(combs)
			branch_count = self._aut_Controller.get_branch_count(state, transition.transitions[2])
			for i in range(1, branch_count):
				probability = self._aut_Controller.get_probability_value(state, transition.transitions[2], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][2] = i
					probs.append(probs[j] * probability)
			probability = self._aut_Controller.get_probability_value(state, transition.transitions[2], 0)
			for i in range(existing):
				combs[i][2] = 0
				probs[i] *= probability
		# Convert to Branch instances
		for i in range(len(combs)):
			combs[i] = Branch(probs[i], combs[i])
		# Done
		return list(filter(lambda b: b.probability > 0.0, combs))

	def jump(self, state: State, transition: Transition, branch: Branch, expressions: List[int] = []) -> State:
		transient = self._get_initial_transient()
		for i in range(0, 4):
			target_state = State()
			state.copy_to(target_state)
			target_transient = Transient()
			transient.copy_to(target_transient)
			if transition.transitions[0] != -1:
				self._aut_Train.jump(state, transient, transition.transitions[0], branch.branches[0], i, target_state, target_transient)
			if transition.transitions[1] != -1:
				self._aut_Gate.jump(state, transient, transition.transitions[1], branch.branches[1], i, target_state, target_transient)
			if transition.transitions[2] != -1:
				self._aut_Controller.jump(state, transient, transition.transitions[2], branch.branches[2], i, target_state, target_transient)
			state = target_state
			transient = target_transient
		for i in range(len(expressions)):
			expressions[i] = self._get_jump_expression_value(state, transient, expressions[i])
		return state

	def jump_np(self, state: State, transition: Transition, expressions: List[int] = []) -> State:
		return self.jump(state, transition, self.get_branches(state, transition)[0], expressions)
