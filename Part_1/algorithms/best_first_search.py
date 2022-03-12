from collections import deque
from operator import itemgetter

# This class acts like a wrapper for the state.
class State:

	# Initialize the class
	def __init__(self, current_state:(), parent_state:(), transition = None, total_cost = 0, cost = 0):
		self.current_state = current_state
		self.parent_state = parent_state
		self.transition = transition

		# The total cost to get to this state since the initial state.
		self.total_cost = total_cost
		
		# The cost to get to this state.
		self.cost = cost


def best_first_search(network, goal, xmin, debug):

	trace = []

	# Get the initial state from the data structure.
	initial_state = network.get_initial_state()

	open = []
	closed = []

	if debug:
		clock = 0

	# Use the state instance to hold: current state, parent state, cost up to this point.
	start_node = State(initial_state, None)
	open.append(start_node)

	# Loop until the open list is empty.
	while len(open) > 0:

		# Sort the open list to get the node with the lowest cost first.
		open.sort(key=lambda node: node.total_cost)
		#sorted(open, key=lambda node: node.total_cost)

		# Get the node with the lowest cost.
		state = open.pop(0)

		# Add the current node to the closed list
		closed.append(state.current_state)

		# Check if we have reached the goal.
		if network.get_expression_value(state.current_state, goal):
			path = []
			temp = state
			
			# Reconstruct the path.
			while temp.current_state != initial_state:
				path.append("---" + str(network.transition_labels[temp.transition.label]) + "--> \t" + "cost: (" + str(temp.cost) + ")\t" + str(temp.current_state))
				temp = temp.parent_state
			
			# Append the initial node as well.
			path.append("---True(0)--> \t" + "cost: (" + str(temp.cost) + ")\t" + str(initial_state))

			# Trace is now the reverse of the path.
			inverse_trace = path[::-1]
			for transition_and_state in inverse_trace:
				trace.append(transition_and_state)

			return (True, state.total_cost, trace)
		
		# Goal not reached.
		# Determine all possible transitions of current state.
		transitions = network.get_transitions(state.current_state) 

		# Print clock to see progress of model progress in debug mode
		if debug:
			clocktemp = int(str(state.current_state).split()[2][:-1])
			if  clocktemp > clock:
				clock = clocktemp
				print("clock: ", clock)
			
		for transition in transitions: #Traverse all transitions

			# Get the neighbour state of this transition.
			reward_exps = [network.properties[xmin].exp.args[0]]
			neighbour = network.jump_np(state.current_state, transition, reward_exps) 

			# Check if the neighbor is in the closed list:
			if (neighbour in closed):
				continue

			# Create a new (neighbour) state instance with the updated cost to get here.
			neighbour_state = State(neighbour, state, transition, state.total_cost + reward_exps[0], reward_exps[0])

			# Check if the neighbour should be added to the open list.
			if should_be_added_to_open(open, neighbour_state) == True:
				open.append(neighbour_state)

	return (False, float('inf'), trace)

def should_be_added_to_open(open, neighbour):
	for node in open:
		if (neighbour.current_state == node.current_state and neighbour.cost >= node.cost):
			return False
	return True
	