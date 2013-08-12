
input_file_name = '../inputs/reverse_words.in'
output_file_name = '../outputs/reverse_words.out'

try:
    in_file = open(input_file_name)
    out_file = open(output_file_name, 'w')
    
    # Number of Cases
    N = in_file.readline()
    
    for n in range(int(N)):
        W = in_file.readline().split()
        W.reverse()
        solution = ' '.join(W)
        
        out_file.write('Case #' + str(n + 1) + ': ' + solution + '\n')
        
    # Done
    in_file.close()
    out_file.close()
    
except IOError as e:
    print 'File ' + input_file_name + ' not found.'
    print e.errno
    print e.strerror