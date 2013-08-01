# by Enrique Gonzalez (Enriikke)
# enjoy!

import Queue

# Setup the files here.
in_file = '../inputs/treasure.in'
out_file = '../outputs/treasure.out'
try:
    in_file = open(in_file, 'r')
    out_file = open(out_file, 'w')
except IOError as e:
    print e.errno
    print e.strerror


# Quick util function to print out a single case solution.
def print_solution(case_number, solution, file=out_file):
    try:
        file.write('Case #{0!s}: {1}\n'.format(case_number, solution))
    except Exception as e:
        print type(e)
        print e.args


# This is just a place holder and it makes it easier to read the code.
def parse_data(file=in_file):
    K, N = file.readline().split()
    K, N = int(K), int(N)
    
    keys = {}
    key_data = file.readline().split()
    for kd in key_data:
        if int(kd) in keys: keys[int(kd)] += 1
        else: keys[int(kd)] = 1
    
    
    chest_graph = {}
    chest_queue = Queue.PriorityQueue()
    for n in range(1, N + 1):
        chest_data = file.readline().split()
        chest_graph[n] = { 'key_needed': int(chest_data[0]), 'keys_inside': {} }
        chest_queue.put((n, ''))
        
        for key in chest_data[2:]:
            keys_inside = chest_graph[n]['keys_inside']
            if int(key) in keys_inside: keys_inside[int(key)] += 1
            else: keys_inside[int(key)] = 1 
    
    chest_graph['total_chests'] = N
     
    
    return chest_graph, chest_queue, keys

 

def can_traverse(c, keys, graph):
    key_needed = graph[c]['key_needed']
    if key_needed in keys and keys[key_needed] > 0: return True
    
    return False


def update_keys(c, keys, graph, action='to'):
    key_needed = graph[c]['key_needed']
    if action == 'to': keys[key_needed] -= 1
    elif action == 'from': keys[key_needed] += 1
    
    for key in graph[c]['keys_inside']:
        if action == 'to':
            if key in keys: keys[key] += graph[c]['keys_inside'][key]
            else: keys[key] = graph[c]['keys_inside'][key]
        
        elif action == 'from':
            keys[key] -= graph[c]['keys_inside'][key]


def traverse(queue, keys, graph):
    
    path = []
    visited = []
    popped_chest = ''
    while queue.empty() == False:
        
        c = queue.get()
        if can_traverse(c[0], keys, graph):
            update_keys(c[0], keys, graph)
            path.append(str(c[0]))
            if popped_chest: queue.put((popped_chest, ''))
            popped_chest = ''
            if len(path) == graph['total_chests']: return ' '.join(path)
        
        else:
            visited.append(c[0])
        
        
        
        if queue.empty() and len(path) > 0:
            
            found_move = False
            for v in visited:
                if can_traverse(v, keys, graph):
                    path.append(str(v))
                    update_keys(v, keys, graph)
                    if popped_chest: queue.put((popped_chest, ''))
                    popped_chest = ''
                    
                    found_move = True
                    break

            
            if found_move == False:
                c = (int(path[-1]), '')
                if popped_chest: queue.put((popped_chest, ''))
                popped_chest = c[0]
                del path[-1]
                update_keys(c[0], keys, graph, action='from')
            
            for v in visited: queue.put((v, ''))
            visited = []
        

            
                        
    return ''


def solve_it():
    # Number of test cases
    N = int(in_file.readline())
    
    # Iterate through every test case
    for n in range(1, N + 1):
        
        # Get my case data ready
        graph, queue, keys = parse_data()
        
        
        # Magic goes here
        solution = traverse(queue, keys, graph)
        if len(solution) == (graph['total_chests'] * 2 - 1):
            print_solution(n, solution)
        else:
            print_solution(n, 'IMPOSSIBLE')
        
    
    
    # Close both files
    in_file.close()
    out_file.close()


solve_it()
