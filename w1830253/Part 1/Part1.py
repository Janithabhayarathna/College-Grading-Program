# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: 20200571
# Date: 25/04/2021


# Part 1 - Student Version.........

print('---------* Progression outcome program *-------')
print(' ')

def check_validity(n):                      #user defined function to check the validity of the input credits.
     if n >= 0 and n <= 120 and n % 20 == 0:
          condition = True
     else:
          print('Range error! Please check your input')
          condition = False

     return condition


_sum =False
while _sum == False:        #Assign '_sum' as false to get inputs until '_sum' become true(120).

    credit_validity = False
    while credit_validity == False:    #Iterate until valid input.
        try:
            print('--------------------------------------------------------------')
            pass_credits = int(input('Please enter your credits at pass: '))
            credit_validity = check_validity(pass_credits)
                
                    
        except ValueError:                       #if there is a value error in the pass credit input,  this 'except' block will run.
            print('Please enter only an integer!')
            credit_validity = False

    credit_validity = False
    while credit_validity == False:    #Iterate until valid input.
        try:
            defer_credits = int(input('Please enter your credit at defer: '))
            credit_validity = check_validity(defer_credits)
            
        except ValueError:                       #if there is a value error in the defer credit input, this 'except' block will run.
            print('Please enter an integer!')
            credit_validity = False
                
    credit_validity = False
    while credit_validity == False:    #Iterate until valid input.
        try:
            fail_credits = int(input('Please enter your credit at fail: '))
            credit_validity = check_validity(fail_credits)
                 
        except ValueError:                      #if there is a value error in the fail credit input, this 'except' block will run.
            print('Please enter an integer!')
            credit_validation = False


        
    total = pass_credits+defer_credits+fail_credits     #finding the total of the credits.
    if total == 120:                                    #check whether the total of credit is equal to 120.
        _sum = True
    else:
        _sum = False
        print('Issue with the total of the credits. Please re-check your inputs and try again')

   
if pass_credits == 120:
     outcome = 'progress'

elif pass_credits == 100:
     outcome = 'Progress (module trailer)'

elif fail_credits >= 80:
     outcome = 'Exclude'

else:
     outcome = 'Do not progress – module retriever'
print(outcome)
print('-------------------------------------------------------------')

print(' ')
print('*** Thank you for using this program and good luck ***')



#Validity part also has been inserted as it requirs to part 1 of my program.
