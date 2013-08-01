
input_file_name = '../inputs/odd_man_out.in'
output_file_name = '../outputs/odd_man_out.out'


try:
    in_file = open(input_file_name)
    out_file = open(output_file_name, 'w')
    
    # Number of Cases
    N = in_file.readline()
    
    for n in range(int(N)):
        G = in_file.readline()
        C = in_file.readline().split()
        guests = {}
        
        for c in C:
            if c in guests: del guests[c]
            else: guests[c] = ''
        
        solution = guests.keys()[0]
        
        out_file.write('Case #' + str(n + 1) + ': ' + solution + '\n')
        
    # Done
    in_file.close()
    out_file.close()
    
except IOError as e:
    print 'File ' + input_file_name + ' not found.'
    print e.errno
    print e.strerror