# by Enrique Gonzalez (Enriikke)
# enjoy!


############### FILE NAMES ###############
input = '../inputs/lawnmower.in'
output = '../outputs/lawnmower.out'



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
        case_data = { 'lawn': [], 'max': [] }
        case_data['total_rows'], case_data['total_cols'] = [int(x) for x in file.readline().split()]
        
        max_rows = []
        for r in range(case_data['total_rows']):
            row = [int(x) for x in file.readline().split()]
            case_data['lawn'].append(row)
            max_rows.append(max(row))
        
        
        max_cols = []
        for c in range(case_data['total_cols']):
            col = []
            for r in range(case_data['total_rows']): col.append(case_data['lawn'][r][c])
            max_cols.append(max(col))
        
        
        case_data['max'].append(max_rows)
        case_data['max'].append(max_cols)
        
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
        solution = 'NO'
        lawn = []
        
        for r in range(case_data['total_rows']):
            lawn.append([case_data['max'][0][r] for i in range(case_data['total_cols'])])
        
        for c in range(case_data['total_cols']):
            max_col = case_data['max'][1][c]
            for r in range(case_data['total_rows']):
                if lawn[r][c] > max_col: lawn[r][c] = max_col
        
        
        if case_data['lawn'] == lawn: solution = 'YES'
        
        
        # Print solution to file.
        print_solution(case, solution, output_file)
        
    
    # Close the files used.
    input_file.close()
    output_file.close()



import cProfile
cProfile.run('solve()')


