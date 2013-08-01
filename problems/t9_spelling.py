
input_file_name = '../inputs/t9_spelling.in'
output_file_name = '../outputs/t9_spelling.out'

t9_map =    {
             'A': 2,
             'B': 22,
             'C': 222,
             'D': 3,
             'E': 33,
             'F': 333,
             'G': 4,
             'H': 44,
             'I': 444,
             'J': 5,
             'K': 55,
             'L': 555,
             'M': 6,
             'N': 66,
             'O': 666,
             'P': 7,
             'Q': 77,
             'R': 777,
             'S': 7777,
             'T': 8,
             'U': 88,
             'V': 888,
             'W': 9,
             'X': 99,
             'Y': 999,
             'Z': 9999,
             ' ': 0
            }


try:
    in_file = open(input_file_name)
    out_file = open(output_file_name, 'w')
    
    # Number of Cases
    N = in_file.readline()
    
    for n in range(int(N)):
        L = in_file.readline()
        s = ['']
        
        for c in L:
            if c.upper() in t9_map:
                t9 = str(t9_map[c.upper()])
                if s[-1]:
                    if s[-1][-1] == t9[0]: s.append(' ')
                s.append(t9)
            
        solution = ''.join(s)
        
        out_file.write('Case #' + str(n + 1) + ': ' + solution + '\n')
        
    # Done
    in_file.close()
    out_file.close()
    
except IOError as e:
    print 'File ' + input_file_name + ' not found.'
    print e.errno
    print e.strerror