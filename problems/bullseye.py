# by Enrique Gonzalez (Enriikke)
# enjoy!


############### FILE NAMES ###############
input = '../inputs/bullseye.in'
output = '../outputs/bullseye.out'

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
        r, t = [ int(x) for x in file.readline().split()]
        return r, t
        
    except Exception as e:
        print type(e)
        print e.args

def paint_ring(radius, paint):
    area = radius**2 - (radius - 1)**2
    if paint >= area: return 1 + paint_ring(radius + 2, paint - area)
    else: return 0


# Solve the problem!!
def solve():
    # Open the files needed.
    input_file, output_file = open_files(input, output)
    
    # Get the total number of cases.
    total_cases = int(input_file.readline())
    for case in range(1, total_cases + 1):
        
        #Get the case data.
        radius, paint = parse_data(input_file)
        
        # Do all the magic here.
        max_area = paint * math.pi
        radius += 1
        
           
        solution = paint_ring(radius, paint)
        
        
        # Print solution to file.
        print_solution(case, solution, output_file)
        
    
    # Close the files used.
    input_file.close()
    output_file.close()



import cProfile
cProfile.run('solve()')

