# test-demo

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
	__slots__ = ("i", "is_done", "Main_location")
	
	def get_variable_value(self, variable: int):
		if variable == 0:
			return self.i
		elif variable == 1:
			return self.is_done
		elif variable == 2:
			return self.Main_location
	
	def copy_to(self, other: State):
		other.i = self.i
		other.is_done = self.is_done
		other.Main_location = self.Main_location
	
	def __eq__(self, other):
		return isinstance(other, self.__class__) and self.i == other.i and self.is_done == other.is_done and self.Main_location == other.Main_location
	
	def __ne__(self, other):
		return not self.__eq__(other)
	
	def __hash__(self):
		result = 75619
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.i)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.is_done)) & 0xFFFFFFFF
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.Main_location)) & 0xFFFFFFFF
		return result
	
	def __str__(self):
		result = "("
		result += "i = " + str(self.i)
		result += ", is_done = " + str(self.is_done)
		result += ", Main_location = " + str(self.Main_location)
		result += ")"
		return result

# Transients
class Transient(object):
	__slots__ = ("step")
	
	def copy_to(self, other: Transient):
		other.step = self.step
	
	def __eq__(self, other):
		return isinstance(other, self.__class__) and self.step == other.step
	
	def __ne__(self, other):
		return not self.__eq__(other)
	
	def __hash__(self):
		result = 75619
		result = (((101 * result) & 0xFFFFFFFF) + hash(self.step)) & 0xFFFFFFFF
		return result
	
	def __str__(self):
		result = "("
		result += "step = " + str(self.step)
		result += ")"
		return result

# Automaton: Main
class MainAutomaton(object):
	__slots__ = ("network", "transition_counts", "transition_labels", "branch_counts")
	
	def __init__(self, network: Network):
		self.network = network
		self.transition_counts = [1, 2, 1, 0]
		self.transition_labels = [[1], [2, 0], [3], []]
		self.branch_counts = [[1], [1, 1], [1], []]
	
	def set_initial_values(self, state: State) -> None:
		state.Main_location = 0
	
	def set_initial_transient_values(self, transient: Transient) -> None:
		pass
	
	def get_transient_value(self, state: State, transient_variable: str):
		location = state.Main_location
		return None
	
	def get_transition_count(self, state: State) -> int:
		return self.transition_counts[state.Main_location]
	
	def get_transition_label(self, state: State, transition: int) -> int:
		return self.transition_labels[state.Main_location][transition]
	
	def get_guard_value(self, state: State, transition: int) -> bool:
		location = state.Main_location
		if location == 0 or location == 2:
			return True
		elif location == 1:
			if transition == 0:
				return (state.i < 5)
			elif transition == 1:
				return (state.i >= 3)
	
	def get_branch_count(self, state: State, transition: int) -> int:
		return self.branch_counts[state.Main_location][transition]
	
	def get_probability_value(self, state: State, transition: int, branch: int) -> float:
		location = state.Main_location
		if location == 0:
			if transition == 0:
				return 1
		elif location == 1:
			if transition == 0:
				return 1
			elif transition == 1:
				return 1
		elif location == 2:
			if transition == 0:
				return 1
		elif location == 3:
			pass
	
	def jump(self, state: State, transient: Transient, transition: int, branch: int, assignment_index: int, target_state: State, target_transient: Transient) -> None:
		if assignment_index == 0:
			location = state.Main_location
			if location == 0:
				if transition == 0:
					if branch == 0:
						target_state.Main_location = 1
			elif location == 1:
				if transition == 0:
					if branch == 0:
						target_state.i = (state.i + 1)
						if target_state.i > 5:
							raise OverflowError("Assigned value of " + str(target_state.i) + " is greater than the upper bound of 5 for variable \"i\".")
						target_transient.step = True
						target_state.Main_location = 1
				elif transition == 1:
					if branch == 0:
						target_state.Main_location = 2
			elif location == 2:
				if transition == 0:
					if branch == 0:
						target_state.is_done = True
						target_state.Main_location = 3

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
	
	def __init__(self, sync_vector: int, label: int = 0, transitions: List[int] = [-1]):
		self.sync_vector = sync_vector
		self.label = label
		self.transitions = transitions

class Branch(object):
	__slots__ = ("probability", "branches")
	
	def __init__(self, probability = 0.0, branches = [0]):
		self.probability = probability
		self.branches = branches

class Network(object):
	__slots__ = ("network", "components", "transition_labels", "sync_vectors", "properties", "variables", "_initial_transient", "_aut_Main")
	
	def __init__(self):
		self.network = self
		self.transition_labels = { 0: "τ", 1: "a", 2: "step", 3: "done" }
		self.sync_vectors = [[0, 0], [1, 1], [2, 2], [3, 3]]
		self.properties = [Property("The Property", PropertyExpression("exists", [PropertyExpression("eventually", [PropertyExpression("ap", [0])])])), Property("The Property (for the simulator)", PropertyExpression("pmax", [PropertyExpression("eventually", [PropertyExpression("ap", [0])])])), Property("Cost-optimal", PropertyExpression("xmin", [1, PropertyExpression("ap", [0])]))]
		self.variables = [VariableInfo("i", None, "int", 0, 5), VariableInfo("is_done", None, "bool"), VariableInfo("Main_location", 0, "int", 0, 3)]
		self._aut_Main = MainAutomaton(self)
		self.components = [self._aut_Main]
		self._initial_transient = self._get_initial_transient()
	
	def get_initial_state(self) -> State:
		state = State()
		state.i = 0
		state.is_done = False
		self._aut_Main.set_initial_values(state)
		return state
	
	def _get_initial_transient(self) -> Transient:
		transient = Transient()
		transient.step = False
		self._aut_Main.set_initial_transient_values(transient)
		return transient
	
	def get_expression_value(self, state: State, expression: int):
		if expression == 0:
			return state.is_done
		elif expression == 1:
			return (1 if self.network._get_transient_value(state, "step") else 0)
		else:
			raise IndexError
	
	def _get_jump_expression_value(self, state: State, transient: Transient, expression: int):
		if expression == 0:
			return state.is_done
		elif expression == 1:
			return (1 if transient.step else 0)
		else:
			raise IndexError
	
	def _get_transient_value(self, state: State, transient_variable: str):
		# Query the automata for the current value of the transient variable
		result = self._aut_Main.get_transient_value(state, transient_variable)
		if result is not None:
			return result
		# No automaton has a value: return the transient variable's (cached) initial value
		return getattr(self._initial_transient, transient_variable)
	
	def get_transitions(self, state: State) -> List[Transition]:
		# Collect all automaton transitions, gathered by label
		transitions = []
		trans_Main = [[], [], [], []]
		transition_count = self._aut_Main.get_transition_count(state)
		for i in range(transition_count):
			if self._aut_Main.get_guard_value(state, i):
				trans_Main[self._aut_Main.get_transition_label(state, i)].append(i)
		# Match automaton transitions onto synchronisation vectors
		for svi in range(len(self.sync_vectors)):
			sv = self.sync_vectors[svi]
			synced = [[-1, -1]]
			# Main
			if synced is not None:
				if sv[0] != -1:
					if len(trans_Main[sv[0]]) == 0:
						synced = None
					else:
						existing = len(synced)
						for i in range(existing):
							synced[i][0] = trans_Main[sv[0]][0]
						for i in range(1, len(trans_Main[sv[0]])):
							for j in range(existing):
								synced.append(synced[j][:])
								synced[-1][0] = trans_Main[sv[0]][i]
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
		combs = [[-1]]
		probs = [1.0]
		if transition.transitions[0] != -1:
			existing = len(combs)
			branch_count = self._aut_Main.get_branch_count(state, transition.transitions[0])
			for i in range(1, branch_count):
				probability = self._aut_Main.get_probability_value(state, transition.transitions[0], i)
				for j in range(existing):
					combs.append(combs[j][:])
					combs[-1][0] = i
					probs.append(probs[j] * probability)
			probability = self._aut_Main.get_probability_value(state, transition.transitions[0], 0)
			for i in range(existing):
				combs[i][0] = 0
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
				self._aut_Main.jump(state, transient, transition.transitions[0], branch.branches[0], i, target_state, target_transient)
			state = target_state
			transient = target_transient
		for i in range(len(expressions)):
			expressions[i] = self._get_jump_expression_value(state, transient, expressions[i])
		return state
	
	def jump_np(self, state: State, transition: Transition, expressions: List[int] = []) -> State:
		return self.jump(state, transition, self.get_branches(state, transition)[0], expressions)