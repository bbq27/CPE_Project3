# Project 3 Graduate Rate (2017-2018)
# Name: Berfredd Quezon
# Instructor: Dr. S. Einakian
# Section: 11
# main program: You need to call the functions you wrote in the graduate_funcs.py
# in an order to create the csv files for each division and produce the outputs on the screen.)
from graduate_funcs import *

# PRINT SCREEN 1
grad_list = create_graduate(read_file('graduate_rate.csv'))
total_comp_info_sci = total_grad_in_div(grad_list, '3400')
print('Total Of Processed number of graduates in Computer and information sciences and support service\n' +
      '(all levels for females and for males-two values as tuple): ' + str(total_comp_info_sci) + '\n')


# PRINT SCREEN 2
divisions = create_files(create_division(read_file('graduate_rate.csv')),create_graduate(read_file('graduate_rate.csv')))

total_comp_grads = total_comp_info_sci[0]+total_comp_info_sci[1] #from before
total_females = total_comp_info_sci[0]/total_comp_grads
total_males = total_comp_info_sci[1]/total_comp_grads
print('Average of Processed Female and Male in Computer and information sciences and support service\n' +
      '(average of females, means total of females/ total of male and female and average of males, means total of males/ total of male\n' +
      'and female- two values as tuple): ' + str((total_females,total_males)) + '\n')


# PRINT SCREEN 3
total_ag = total_grad_in_div(grad_list, '3200')
total_comp = total_grad_in_div(grad_list, '3400')
total_edu = total_grad_in_div(grad_list, '3600')
total_eng = total_grad_in_div(grad_list, '3800')
total_grad_females = total_ag[0] + total_comp[0] + total_edu[0] + total_eng[0]
total_grad_males = total_ag[1] + total_comp[1] + total_edu[1] + total_eng[1]
print('Total of all Females and Males Graduate in all Majors (total of females, total of males): ' + str((total_grad_females,total_grad_males)) + '\n')


# PRINT SCREEN 4
total_grads = total_grad_males + total_grad_females
cs_to_total_ratio = total_comp_grads/total_grads
print('Compare total graduate of Computer and information sciences and support service to\n' +
      'all other Majors (cs/(total-cs)): ' + str(cs_to_total_ratio))
