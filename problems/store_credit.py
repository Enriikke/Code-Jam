
input_file_name = '../inputs/store_credit.in'
output_file_name = '../outputs/store_credits.out'

try:
    in_file = open(input_file_name)
    out_file = open(output_file_name, 'w')
    
    # Number of Cases
    N = in_file.readline()

    for n in range(int(N)):
        # Total store credit
        C = int(in_file.readline())
        # Number of items in store
        I = int(in_file.readline())
        # Price list
        L = in_file.readline().split()
        
        # Iterate through the products
        solution = ''
        found = False
        for i in range(len(L)):
            p1 = int(L[i])
            for j in range(i + 1, len(L)):
                p2 = int(L[j])
                if p1 + p2 == C:
                    solution = str(i + 1) + ' ' + str(j + 1)
                    found = True
                    break
                    
            if found: break
            
        out_file.write('Case #' + str(n + 1) + ': ' + solution + '\n')
        
    
    # Done
    in_file.close()
    out_file.close()
    
except IOError as e:
    print 'File ' + input_file_name + ' not found.'
    print e.errno
    print e.strerror
    
