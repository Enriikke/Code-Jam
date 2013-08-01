# by Enrique Gonzalez (Enriikke)
# enjoy!


############### FILE NAMES ###############
input = '../inputs/manage_your_energy.in'
output = '../outputs/manage_your_energy.out'



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
        case_data = {'max_energy': 0, 'regain': 0, 'calendar': []}
        data = file.readline().split()
        case_data['max_energy'] = data[0]
        case_data['regain'] = data[1]
        case_data['calendar'] = file.readline().split()
        case_data['max_gain'] = max(case_data['calendar'])
        
        return case_data
        
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
        case_data = parse_data(input_file)
        
        # Do all the magic here.
        solution = 0
        calendar = case_data['calendar']
        for a in calendar:
            pass
            
        solution = str(solution)
        
        # Print solution to file.
        print_solution(case, solution, output_file)
        
    
    # Close the files used.
    input_file.close()
    output_file.close()



import cProfile
cProfile.run('solve()')

