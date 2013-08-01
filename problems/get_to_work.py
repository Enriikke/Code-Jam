
input_file_name = '../inputs/get_to_work.in'
output_file_name = '../outputs/get_to_work.out'


try:
    in_file = open(input_file_name)
    out_file = open(output_file_name, 'w')
    
    # Number of Cases
    N = in_file.readline()
    
    for n in range(int(N)):
        T, O = in_file.readline().split()
        T, O = int(T), int(O)
        E = int(in_file.readline())
        
        town_map = {}
        
        for e in range(E):
            H, P = in_file.readline().split()
            H, P = int(H), int(P)
            
            if H in town_map: 
                town_map[H]['employees'] = town_map[H]['employees'] + 1
                if P > 0: town_map[H]['cars'].append(P)
            else:
                town_map[H] = {'id': H, 'employees': 1, 'cars': [P], 'used_cars': 0}
                
        s = []
        solution = ''
        for t in range(T):
            if t + 1 in town_map:
                if t + 1 == O:
                    s.append('0')
                else:
                    town = town_map[t + 1]
                    if town['employees'] > sum(town['cars']):
                        solution = 'IMPOSSIBLE'
                        break
                    else:
                        town['cars'].sort()
                        town['cars'].reverse()
                        for c in town['cars']:
                            town['employees'] = town['employees'] - c
                            town['used_cars'] = town['used_cars'] + 1
                            if town['employees'] <= 0: 
                                s.append(str(town['used_cars']))
                                break
                    
            else:
                s.append('0')
                
        
        if solution != 'IMPOSSIBLE': solution = ' '.join(s)
        out_file.write('Case #' + str(n + 1) + ': ' + solution + '\n')
    
    # Done
    in_file.close()
    out_file.close()
    
except IOError as e:
    print 'File ' + input_file_name + ' not found.'
    print e.errno
    print e.strerror