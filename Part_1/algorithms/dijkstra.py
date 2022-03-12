from collections import deque

def dijkstra(network, goal, xmin, debug): 
	visited = set() # Set to keep track of visited nodes.
	trace = []
	node = network.get_initial_state()
	vertices = []
	vertices.append(node)
	queue = deque([(node, [])]) # FIFO which keeps track of nodes to be checked.
	destination_node = None

	while queue:
		current_state, path = queue.popleft()
		#print ("Current state:", n)

		if current_state not in visited:
			visited.add(current_state)
			transitions = network.get_transitions(current_state) #Determine all possible transitions of current node from the model

			for transition in transitions: #Traverse all transitions
				next_state = network.jump_np(current_state, transition) #Get the state from the model
				vertices.append(next_state)

				if network.get_expression_value(next_state, goal):
					destination_node = next_state

				if next_state not in queue:
					queue.append((next_state, path + [transition]))	
	
	# Complete state space of the model has now been loaded into "vertices"
	# We can now start with finding the lowest cost path and actually use Dijkstra
	distances = {vertex: float('inf') for vertex in vertices}
	distances[node] = 0

	shortest_path_steps = float('inf')
	previous_vertices = {vertex: None for vertex in vertices}
	
	while(vertices):
		smallest = min(vertices, key= lambda vertex: distances[vertex])
		
		if(distances[smallest] == 'inf'):
			print('Well that is quite a long path, we cant continue anymore..')
			return (False, 0, trace)

		transitions = network.get_transitions(smallest) #Determine all possible transitions of current node from the model
		
		for transition in transitions: #Traverse all transitions
			reward_exps = [network.properties[xmin].exp.args[0]]
			next_state = network.jump_np(smallest, transition, reward_exps) #Get the next state from the model	

			alternative_route_cost = distances[smallest] + reward_exps[0]

			if network.get_expression_value(next_state, goal):
				if alternative_route_cost < shortest_path_steps:
					shortest_path_steps = alternative_route_cost
				destination_node = (next_state, transition)

			if alternative_route_cost < distances[next_state]:	
				distances[next_state] = alternative_route_cost
				previous_vertices[(next_state)] = (smallest, transition)

		vertices.remove(smallest)
	
	#print('Lowest cost path (X_min) has a cost : ', shortest_path_steps)

	path = deque()
	current_vertex, transition = destination_node
	while previous_vertices[current_vertex] is not None:
		path.appendleft((current_vertex, transition))
		current_vertex, transition = previous_vertices[current_vertex]
	if path:
		path.appendleft((current_vertex, transition))

	for p in path:
		current_vertex, transition = p
		trace.append(str(current_vertex) + ": " + str(network.transition_labels[transition.label]))
	
	return (True, shortest_path_steps, trace)