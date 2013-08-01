# by Enrique Gonzalez (Enriikke)
# enjoy!


############### FILE NAMES ###############
input = '../inputs/tic_tac_toe_tomek.in'
output = '../outputs/tic_tac_toe_tomek.out'



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
        case_data = { 'board': '', 'is_full': True }
        board = []
        for i in range(4):
            row = file.readline()
            if case_data['is_full'] and row.find('.') > -1: 
                case_data['is_full'] = False
            
            board.append(row.strip())
        
        # Add game board to dictionary.
        case_data['board'] = board
        
        # Read empty line at the end of every case.
        file.readline()
        
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
        solution = 'Draw'
        board = case_data['board']
        
        # Check rows first.
        for row in board:
            if row.replace('T', 'X') == 'XXXX':
                solution = 'X won'
                break
            
            if row.replace('T', 'O') == 'OOOO':
                solution = 'O won'
                break
                
        
        # If we didn't find a winner then check columns.
        if solution == 'Draw':
            for col in range(4):
                col_join = []
                for row in board: col_join.append(row[col])
                col_join = ''.join(col_join)
                
                if col_join.replace('T', 'X') == 'XXXX':
                    solution = 'X won'
                    break
            
                if col_join.replace('T', 'O') == 'OOOO':
                    solution = 'O won'
                    break
            
        
        # If we haven't found a winner yet then need to check diagonals.
        if solution == 'Draw':
            diagonal1 = []
            diagonal2 = []
            for dia in range(4):
                diagonal1.append(board[dia][dia])
                diagonal2.append(board[3-dia][dia])
                
            diagonal1 = ''.join(diagonal1)
            diagonal2 = ''.join(diagonal2)
            
            if diagonal1.replace('T', 'X') == 'XXXX':
                solution = 'X won'
            elif diagonal1.replace('T', 'O') == 'OOOO':
                solution = 'O won'
            elif diagonal2.replace('T', 'X') == 'XXXX':
                solution = 'X won'
            elif diagonal2.replace('T', 'O') == 'OOOO':
                solution = 'O won'
             
        
        # Finally if we didn't find a winner then we need to check if the board is full.
        if solution == 'Draw' and case_data['is_full'] == False:
            solution = 'Game has not completed'
        
        # Print solution to file.
        print_solution(case, solution, output_file)
        
    
    # Close the files used.
    input_file.close()
    output_file.close()



import cProfile
cProfile.run('solve()')


