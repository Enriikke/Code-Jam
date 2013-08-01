# by Enrique Gonzalez (Enriikke)
# enjoy!

import math
import time

# Setup the files here.
in_file = '../inputs/fair_and_square.in'
out_file = '../outputs/fair_and_square.out'
try:
    in_file = open(in_file, 'r')
    out_file = open(out_file, 'w')
except IOError as e:
    print e.errno
    print e.strerror


# Quick util function to print out a single case solution.
def print_solution(case_number, solution, file=out_file):
    try:
        file.write('Case #{0!s}: {1}\n'.format(case_number, solution))
    except Exception as e:
        print type(e)
        print e.args


# This is just a place holder and it makes it easier to read the code.
def parse_data(file=in_file):
    A, B = file.readline().split()
    A = int(math.ceil(int(A) ** 0.5))
    B = int(math.floor(int(B) ** 0.5))
    
    return A, B


def solve_it():
    # Number of test cases
    N = int(in_file.readline())
    answer = []
    
    # Iterate through every test case
    for n in xrange(1, N + 1):
        # Get my case data ready
        A, B = parse_data()
        
        # Magic goes here
        solution = ''
        fair_square_count = 0
        for i in xrange (A, B + 1):
            square = str(i * i)
            is_palindrome = str(i) == str(i)[::-1]
            if is_palindrome and square == square[::-1]: 
                fair_square_count = fair_square_count + 1
        
        #solution = str(fair_square_count)
        answer.append('Case #{0!s}: {1}'.format(n, str(fair_square_count)))
        
        # Print solution
        #print_solution(n, solution)
    
    out_file.write('\n'.join(answer))
    
    # Close both files
    in_file.close()
    out_file.close()


time_start = time.time()
print time_start
solve_it()
time_end = time.time()
print time_end
print '\nTOTAL TIME: ' + str((time_end - time_start) / 60.0)
