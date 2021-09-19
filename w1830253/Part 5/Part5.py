# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: 20200571.
# Date: 29/04/2021.

# Part 5 - Alternative Staff Version 


print(' ')
print('---------* Progression outcome program *-------')
print(' ')

# Histogram part
def histogram():
  print('Progress', progress, ' :', '*' * progress, end='')
  print('\nTrailer', trailer, '  :', '*' * trailer, end='')
  print('\nRetriever', retriever, ':', '*' * retriever, end='')
  print('\nExcluded', excluded, ' :', '*' * excluded, end='')
  print('\n ')
  print(progress + trailer + retriever + excluded, 'outcomes in total.')


progress = 0
trailer = 0
retriever = 0
excluded = 0

credit_list = [[120,0,0],[100,20,0],[100,0,20],[80,20,20],[60,40,20],[40,40,40],[20,40,60],[20,20,80],[20,0,100],[0,0,120]]

for i in range(0,len(credit_list)):
  pass_credit = credit_list[i][0]
  defer_credit = credit_list[i][1]
  fail_credit = credit_list[i][2]

  # Finding the relavant progression outcome

  if pass_credit == 120 and defer_credit == 0 and fail_credit == 0:
    print('Progress')
    progress = progress + 1
  elif pass_credit == 100 and (defer_credit == 0 or fail_credit == 0) and (defer_credit == 20 or fail_credit == 20):
    print('Progress (module trailer)')
    trailer = trailer + 1
  elif fail_credit >= 80 and (pass_credit + defer_credit <= 40):
    print('Exclude')
    excluded = excluded + 1
  else:
    print('Do not pregress-module retriever')
    retriever = retriever + 1
  print(' ')


# calling histogram part.
histogram()


print('-------------------------------------------------------------')
print(' ')
print(' ')
print('*** Thank you for using this program and good luck ***')
