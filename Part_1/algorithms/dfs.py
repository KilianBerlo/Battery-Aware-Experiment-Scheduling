# This class acts like a wrapper for the state.
class State:

	# Initialize the class
	def __init__(self, current_state:(), parent_state:(), transition = None):
		self.current_state = current_state
		self.parent_state = parent_state
		self.transition = transition	

# DFS algorithm that checks if the exists properties hold
def dfs(network, goal):
	visited = set() # Set to keep track of visited nodes.
	numberofstates = 0
	trace = []

	initial_state = network.get_initial_state()

	stack = []

	# Use the state instance to hold: current state, parent state, cost up to this point.
	start_node = State(initial_state, None)

	stack.append(start_node)

	while stack:
		state = stack.pop()

		if state.current_state not in visited:
			#print ("Current state:", node)
			visited.add(state.current_state) #Add current node to visited nodes set
			transitions = network.get_transitions(state.current_state) #Determine all possible transitions of current node from the model
			
			for transition in reversed(transitions): #Traverse all transitions
				#print("Taking transition", network.transition_labels[transition.label])
				
				neighbour = network.jump_np(state.current_state, transition, [0]) #Get the state from the model
				#print("Next state in LTS:", str(state))
				if neighbour not in visited:	
					numberofstates += 1
					
					# Create a new (neighbour) state instance with the updated cost to get here.
					neighbour_state = State(neighbour, state, transition)
					stack.append(neighbour_state)
					
					if network.get_expression_value(neighbour, goal):
						path = []
						temp = neighbour_state
						
						# Reconstruct the path.
						while temp.current_state != initial_state:
							path.append("---" + str(network.transition_labels[temp.transition.label]) + "--> \t" + str(temp.current_state))
							temp = temp.parent_state
						
						# Append the initial node as well.
						path.append("---True--> \t" + str(initial_state))

						# Trace is now the reverse of the path.
						inverse_trace = path[::-1]
						for transition_and_state in inverse_trace:
							trace.append(transition_and_state)
						#Return to stop searching in the state space
						return (True, numberofstates, trace)

	return (False, numberofstates, trace)
	