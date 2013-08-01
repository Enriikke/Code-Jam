
input_file_name = '../inputs/polygraph.in'
output_file_name = '../outputs/polygraph.out'


try:
    in_file = open(input_file_name)
    out_file = open(output_file_name, 'w')
    
    # Number of Cases
    N = in_file.readline()
    
    for n in range(int(N)):
        P, S = in_file.readline().split()
        googlia_map = {}
        
        solution = '0'
        if P == C: solution = str(min(S))
        else:
            solution = 'OTHER'
        
        
        out_file.write('Case #' + str(n + 1) + ': ' + solution + '\n')
        
    # Done
    in_file.close()
    out_file.close()
    
except IOError as e:
    print 'File ' + input_file_name + ' not found.'
    print e.errno
    print e.strerror