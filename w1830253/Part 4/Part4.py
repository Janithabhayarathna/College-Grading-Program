# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: 20200571.
# Date: 29/04/2021.

# Part 4

print(' ')
print('---------* Progression outcome program *-------')
print(' ')


def check_validity(n):                      # user defined function to check the validity of the input credits.
    if n >= 0 and n <= 120 and n % 20 == 0:
        condition = True
    else:
        print('Out of range.')
        condition = False

    return condition


progress = 0
trailer = 0
retriever = 0
excluded = 0

print('Staff version with Histogram')
q = 'y'
while q == 'y':               #Assigned q as y to get the first set of inputs
  _sum = False              #Assigned '_sum' as false to get inputs until '_sum' become true(120).
  while _sum == False:

    #Getting inputs from user and Validation
    credit_validity = False
    while credit_validity == False :  # Iterate until valid input.
        try:
            pass_credits = int(input('Please enter your credits at pass: '))
            credit_validity = check_validity(pass_credits)
        except ValueError:    # if there is a value error in the pass credit input,  this 'except' block will run.
            print('Integer required')
            credit_validity = False

    credit_validity = False
    while credit_validity == False:  # Iterate until valid input.
        try:
            defer_credits = int(input('Please enter your credit at defer: '))
            credit_validity = check_validity(defer_credits)
        except ValueError:  # if there is a value error in the defer credit input, this 'except' block will run.
            print('Integer required')
            credit_validity = False

    credit_validity = False
    while credit_validity == False:  # Iterate until valid input.
        try:
            fail_credits = int(input('Please enter your credit at fail: '))
            credit_validity = check_validity(fail_credits)
        except ValueError:  # if there is a value error in the fail credit input, this 'except' block will run.
            print('Please enter an integer!')
            credit_validation = False

    total = pass_credits + defer_credits + fail_credits  # finding the total of the credits.
    if total == 120:    # checking whether the total of credit is equal to 120.
        _sum = True
    else:
        _sum = False
        print('Total incorrect.')
  # Finding the relavant progression outcome
  if pass_credits == 120:
    outcome = 'progress'
    progress = progress+1

  elif pass_credits == 100:
    outcome = 'Progress (module trailer)'
    trailer = trailer+1

  elif fail_credits >= 80:
    outcome = 'Exclude'
    excluded = excluded+1

  else:
    outcome = 'Do not progress – module retriever'
    retriever = retriever+1
  print(outcome)
  print(' ')

  try:
    q=input("Would you like to enter another set of data?\n Enter 'y' for yes or 'q' to quit and view results: ").lower() #Asking whether user need to input more or not
    print(' ')
  except ValueError:
    print("Please enter only 'y' or 'q'.")
    break

# Histogram part.
print('Vertical Histogram')
print(' ')
maximum = max(progress,trailer,retriever,excluded)
print('Progress  Trailing  Retriever  Excluded')
i = 1
while i <= maximum:
    if progress > 0:
        print('   *', end='         ')
        progress = progress-1
    else:
        print(' ', end='            ')
    if trailer > 0:
        print('*', end='         ')
        trailer = trailer-1
    else:
        print(' ', end='         ')
    if retriever > 0:
        print('*', end='          ')
        retriever = retriever-1
    else:
        print(' ', end='          ')
    if excluded > 0:
        print('*', end='       \n')
        excluded = excluded-1
    else:
        print('  ', end='       \n')
    i = i+1

print('\n-------------------------------------------------------------')
print(' ')
print(' ')
print('*** Thank you for using this program and good luck ***')
