from collections import deque

def bfs(network, goal):
	visited = set() # Set to keep track of visited nodes.
	trace = []
	numberofstates = 0
	initial_state = network.get_initial_state()

	
	queue = deque([(initial_state, [])]) # FIFO which keeps track of nodes to be checked.

	while queue:

		current_state, path = queue.popleft()
		#print ("Current state:", n)

		if current_state not in visited:
			visited.add(current_state)
			transitions = network.get_transitions(current_state) #Determine all possible transitions of current node from the model

			for transition in transitions: #Traverse all transitions
				#print("Taking transition", network.transition_labels[transition.label])
				state = network.jump_np(current_state, transition) #Get the state from the model
				trace.append(str(state) + ": " + str(network.transition_labels[transition.label]))

				if network.get_expression_value(state, goal):
					temppath = 0
					path.append(transition)
					for p in path:
						if str(network.transition_labels[p.label]) is not temppath:
							temppath = str(network.transition_labels[p.label])
							numberofstates += 1
					numberofstates -= 1 #minus "true" state
					return (True, numberofstates, trace)

				if state not in queue:
					queue.append((state, path + [transition]))
					#print("State: ", str(state), " is added to the queue.")
				#else:
					#print("State: ", str(state), "is already in the queue, so is skipped.")
	
	return (False, numberofstates, trace)