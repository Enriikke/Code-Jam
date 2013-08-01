# by Enrique Gonzalez (Enriikke)
# enjoy!


############### FILE NAMES ###############
input = '../inputs/osmos.in'
output = '../outputs/osmos.out'



# Open (create) the files needed to read the data and write the solution.
def open_files(input, output):
    try:
        input_file = open(input, 'r')
        output_file = open(output, 'w')
        
        return input_file, output_file
        
    except Exception as e:
        print type(e)
        print e.args
        


# Quick util function to print out a single case solution.
def print_solution(case_number, solution, file):
    try:
        file.write('Case #{0!s}: {1}\n'.format(case_number, solution))
    
    except Exception as e:
        print type(e)
        print e.args
        


# Read the data for a single case from the input file.
def parse_data(file):
    try:
        A, N = file.readline().split()
        motes = sorted([int(x) for x in file.readline().split()])
        print A
        print motes
        return int(A), int(N), motes
        
    except Exception as e:
        print type(e)
        print e.args



# Solve the problem!!
def solve():
    # Open the files needed.
    input_file, output_file = open_files(input, output)
    
    # Get the total number of cases.
    total_cases = int(input_file.readline())
    for case in range(1, total_cases + 1):
        
        #Get the case data.
        A, N, motes = parse_data(input_file)
        
        # Do all the magic here.
        solution = 0
        if A > 1:
            for i in range(N):
                m = int(motes[i])
                if A > m: 
                    A += m
                elif (A * 2 - 1) > m:
                    A += A - 1 + m
                    solution += 1
                elif i >= N - 2:
                    solution += 1
                else:
                    a = A
                    s = 0
                    while a <= m:
                        a += a - 1
                        s += 1
                    
                    a += m
                    
                    if s >= N - i:
                        solution += N - i
                        break
                    
                    else:
                        solution += s
                        A += a
                    
        else:
            solution = N
        
        
        # Print solution to file.
        print_solution(case, solution, output_file)
        
    
    # Close the files used.
    input_file.close()
    output_file.close()



import cProfile
cProfile.run('solve()')

