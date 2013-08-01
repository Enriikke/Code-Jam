# by Enrique Gonzalez (Enriikke)
# enjoy!


############### FILE NAMES ###############
input = '../inputs/falling_diamonds.in'
output = '../outputs/falling_diamonds.out'

import math

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
        N, X, Y = file.readline().split()
        return int(N), int(X), int(Y)
        
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
        D, X, Y = parse_data(input_file)
        
        # Do all the magic here.
        if D >= 15:
            if math.abs(X) <= 4 and math.abs(Y) <= 4: solution = 1.0
            elif D == 15: solution = 0.0
            else:
                D = D - 15
                pass
                
        
        elif D >= 6:
            if math.abs(X) <= 2 and math.abs(Y) <= 2: solution = 1.0
            elif D == 6: solution == 0.0
            else:
                D = D - 6
                pass
        
        elif D >= 1:
            if math.abs(X) == 0 and math.abs(Y) == 0: solution = 1.0
            elif D == 1: solution == 0.0
            else:
                D = D - 1
                pass
        
        
        # Print solution to file.
        print_solution(case, solution, output_file)
        
    
    # Close the files used.
    input_file.close()
    output_file.close()



import cProfile
cProfile.run('solve()')

