# This program solves the knight on a dial pad problem
# via monte-carlo simulations.
# The recursion depth is limited, so that must be adjusted.
import sys, numpy

# Set recursion depth to solve the problem of 1024 moves.
sys.setrecursionlimit(2048)

# Number of Monte Carlo simulations -- set high in an attempt to converge
numtrials = 99999999
nummoves = 0
sum = 0
count = 0

# Each dial pad number has its own routine except number 5 since
# the is no way for the knight to reach that square.
# Each routine increments the count, checks it against the number of moves
# adds to the running sum and randomly moves the knight to the next square
# if it has not reached its move limit.
#
# Two routines have three possible moves.
def dial_zero():
    global sum
    global count
    global nummoves
    
    count += 1
    roll = numpy.random.randint(0,2)

    if count == nummoves:
        return
    elif roll == 0:
        dial_four()
    else:
        dial_six()

    return

def dial_one():
    global sum
    global count
    global nummove
    
    count += 1
    sum += 1
    roll = numpy.random.randint(0,2)

    if count == nummoves:
        return
    elif roll == 0:
        dial_six()
    else:
        dial_eight()

    return

def dial_two():
    global sum
    global count
    global nummoves
    
    count += 1
    sum += 2
    roll = numpy.random.randint(0,2)

    if count == nummoves:
        return
    elif roll == 0:
        dial_seven()
    else:
        dial_nine()
        
    return

def dial_three():
    global sum
    global count
    global nummoves
    
    count += 1
    sum += 3
    roll = numpy.random.randint(0,2)

    if count == nummoves:
        return
    elif roll == 0:
        dial_four()
    else:
        dial_eight()

    return

def dial_four():
    global sum
    global count
    global nummoves
    
    count += 1
    sum += 4
    roll = numpy.random.randint(0,3)

    if count == nummoves:
        return
    elif roll == 0:
        dial_three()
    elif roll == 1:
        dial_nine()
    else:
        dial_zero()

    return
    
def dial_six():
    global sum
    global count
    global nummoves
    
    count += 1
    sum += 6
    roll = numpy.random.randint(0,3)

    if count == nummoves:
        return
    elif roll == 0:
        dial_one()
    elif roll == 1:
        dial_seven()
    else:
        dial_zero()
        
    return

def dial_seven():
    global sum
    global count
    global nummoves
    
    count += 1
    sum += 7
    roll = numpy.random.randint(0,2)

    if count == nummoves:
        return
    elif roll == 0:
        dial_two()
    else:
        dial_six()
        
    return

def dial_eight():
    global sum
    global count
    global nummoves
    
    count += 1
    sum += 8
    roll = numpy.random.randint(0,2)

    if count == nummoves:
        return
    elif roll == 0:
        dial_one()
    else:
        dial_three()
    return

def dial_nine():
    global sum
    global count
    global nummoves

    count += 1
    sum += 9
    roll = numpy.random.randint(0,2)

    if count == nummoves:
        return
    elif roll == 0:
        dial_two()
    else:
        dial_four()
        
    return

# Main routine
# First run goes through the 10 move questions
# Second run goes through the 1024 move questions
def main():
    global nummoves
    
    nummoves=10
    start_monte(7,5)

    nummoves=1024
    start_monte(29,23)
    
    return

# Function that controls the starting and ending of the recursion
def start_monte(a, b):
    global sum
    global count
    global nummoves
    global numtrials

    sumlist=[]
    
    sumtot = 0

    # Start the simulations, placing the knight at zero.
    # Store the sums in a list
    for i in range(numtrials):
        sum = 0
        count = 0

        dial_zero()

        sumlist.append(sum)

    # Output the results for the EV of S mod 10 and the standard deviation
    sumarray = numpy.asarray(sumlist)
    print("Average mod {0:g} is: {1:.10f}".format(nummoves,numpy.average(sumarray%nummoves)))
    print("Standard deviation is: {0:.10f}".format(numpy.std(sumarray%nummoves)))

    # Find the probability of the the sum being divisible by b
    # given that it's divisible by a.
    top = 0
    bottom = 0
    for value in sumarray:
        if value%a == 0:
            bottom += 1
            if value%b == 0:
                top +=1
                
    print("The probability of S mod ", b, " = 0 given that S mod ", a," = 0 is: {0:.10f}".format(float(top)/bottom))


if __name__ == "__main__":
    sys.exit(main())
