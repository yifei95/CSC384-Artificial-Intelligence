from mealplan_csp import *
from propagator import *
from ordering import *
from mealplan_min_csp import *

def print_min_mealplan_soln(var_array, food):
    print('Breakfast:')
    result = str(var_array[0].get_assigned_value()[1] * food[(var_array[0].get_assigned_value())[0]][3]) + ' ' + food[(var_array[0].get_assigned_value())[0]][4] + ' of ' + (var_array[0].get_assigned_value())[0]
    print(result)
    result = str(var_array[1].get_assigned_value()[1]* food[(var_array[1].get_assigned_value())[0]][3]) + ' ' + food[(var_array[1].get_assigned_value())[0]][4] + ' of ' + (var_array[1].get_assigned_value())[0]
    print(result)
    result = str(var_array[2].get_assigned_value()[1]* food[(var_array[2].get_assigned_value())[0]][3]) + ' ' + food[(var_array[2].get_assigned_value())[0]][4] + ' of ' + (var_array[2].get_assigned_value())[0]
    print(result)
    result = str(var_array[3].get_assigned_value()[1]* food[(var_array[3].get_assigned_value())[0]][3]) + ' ' + food[(var_array[3].get_assigned_value())[0]][4] + ' of ' + (var_array[3].get_assigned_value())[0]
    print(result)   
    price_b = var_array[0].get_assigned_value()[-1] + var_array[1].get_assigned_value()[-1] + var_array[2].get_assigned_value()[-1] + var_array[3].get_assigned_value()[-1]
    print('The total cost for breakfast is: $' + str(price_b) + '.')
    print(' ')
    print('Lunch:')
    result = str(var_array[4].get_assigned_value()[1]* food[(var_array[4].get_assigned_value())[0]][3]) + ' ' + food[(var_array[4].get_assigned_value())[0]][4] + ' of ' + (var_array[4].get_assigned_value())[0]
    print(result)
    result = str(var_array[5].get_assigned_value()[1]* food[(var_array[5].get_assigned_value())[0]][3]) + ' ' + food[(var_array[5].get_assigned_value())[0]][4] + ' of ' + (var_array[5].get_assigned_value())[0]
    print(result)
    result = str(var_array[6].get_assigned_value()[1]* food[(var_array[6].get_assigned_value())[0]][3]) + ' ' + food[(var_array[6].get_assigned_value())[0]][4] + ' of ' + (var_array[6].get_assigned_value())[0]
    print(result)
    result = str(var_array[7].get_assigned_value()[1]* food[(var_array[7].get_assigned_value())[0]][3]) + ' ' + food[(var_array[7].get_assigned_value())[0]][4] + ' of ' + (var_array[7].get_assigned_value())[0]
    print(result)
    price_l = var_array[4].get_assigned_value()[-1] + var_array[5].get_assigned_value()[-1] + var_array[6].get_assigned_value()[-1] + var_array[7].get_assigned_value()[-1]
    print('The total cost for lunch is: $' + str(price_l) + '.')
    print(' ')    
    print('Dinner:')
    result = str(var_array[8].get_assigned_value()[1]* food[(var_array[8].get_assigned_value())[0]][3]) + ' ' + food[(var_array[8].get_assigned_value())[0]][4] + ' of ' + (var_array[8].get_assigned_value())[0]
    print(result)
    result = str(var_array[9].get_assigned_value()[1]* food[(var_array[9].get_assigned_value())[0]][3]) + ' ' + food[(var_array[9].get_assigned_value())[0]][4] + ' of ' + (var_array[9].get_assigned_value())[0]
    print(result)
    result = str(var_array[10].get_assigned_value()[1]* food[(var_array[10].get_assigned_value())[0]][3]) + ' ' + food[(var_array[10].get_assigned_value())[0]][4] + ' of ' + (var_array[10].get_assigned_value())[0]
    print(result)
    result = str(var_array[11].get_assigned_value()[1]* food[(var_array[11].get_assigned_value())[0]][3]) + ' ' + food[(var_array[11].get_assigned_value())[0]][4] + ' of ' + (var_array[11].get_assigned_value())[0]
    print(result)
    price_d = var_array[8].get_assigned_value()[-1] + var_array[9].get_assigned_value()[-1] + var_array[10].get_assigned_value()[-1] + var_array[11].get_assigned_value()[-1]
    print('The total cost for dinner is: $' + str(price_d) + '.')
    print(' ')    


def print_mealplan_soln(var_array, food):
    
    for i in range(len(var_array)):
        if i == 0:
            print('Monday:')
            print('Breakfast:')
            result = str(var_array[i][0].get_assigned_value()[1] * food[(var_array[i][0].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][0].get_assigned_value())[0]][4] + ' of ' + (var_array[i][0].get_assigned_value())[0]
            print(result)
            result = str(var_array[i][1].get_assigned_value()[1]* food[(var_array[i][1].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][1].get_assigned_value())[0]][4] + ' of ' + (var_array[i][1].get_assigned_value())[0]
            print(result)
            result = str(var_array[i][2].get_assigned_value()[1]* food[(var_array[i][2].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][2].get_assigned_value())[0]][4] + ' of ' + (var_array[i][2].get_assigned_value())[0]
            print(result)
            result = str(var_array[i][3].get_assigned_value()[1]* food[(var_array[i][3].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][3].get_assigned_value())[0]][4] + ' of ' + (var_array[i][3].get_assigned_value())[0]
            print(result)
            print('Lunch:')
            result = str(var_array[i][4].get_assigned_value()[1]* food[(var_array[i][4].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][4].get_assigned_value())[0]][4] + ' of ' + (var_array[i][4].get_assigned_value())[0]
            print(result)
            result = str(var_array[i][5].get_assigned_value()[1]* food[(var_array[i][5].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][5].get_assigned_value())[0]][4] + ' of ' + (var_array[i][5].get_assigned_value())[0]
            print(result)
            result = str(var_array[i][6].get_assigned_value()[1]* food[(var_array[i][6].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][6].get_assigned_value())[0]][4] + ' of ' + (var_array[i][6].get_assigned_value())[0]
            print(result)
            result = str(var_array[i][7].get_assigned_value()[1]* food[(var_array[i][7].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][7].get_assigned_value())[0]][4] + ' of ' + (var_array[i][7].get_assigned_value())[0]
            print(result)
            print('Dinner:')
            result = str(var_array[i][8].get_assigned_value()[1]* food[(var_array[i][8].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][8].get_assigned_value())[0]][4] + ' of ' + (var_array[i][8].get_assigned_value())[0]
            print(result)
            result = str(var_array[i][9].get_assigned_value()[1]* food[(var_array[i][9].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][9].get_assigned_value())[0]][4] + ' of ' + (var_array[i][9].get_assigned_value())[0]
            print(result)
            result = str(var_array[i][10].get_assigned_value()[1]* food[(var_array[i][10].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][10].get_assigned_value())[0]][4] + ' of ' + (var_array[i][10].get_assigned_value())[0]
            print(result)
            result = str(var_array[i][11].get_assigned_value()[1]* food[(var_array[i][11].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][11].get_assigned_value())[0]][4] + ' of ' + (var_array[i][11].get_assigned_value())[0]
            print(result)  
            
        if i == 1:
            print( ' ')
            print('Tuesday:')
            print('Breakfast:')
            result = str(var_array[i][0].get_assigned_value()[1] * food[(var_array[i][0].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][0].get_assigned_value())[0]][4] + ' of ' + (var_array[i][0].get_assigned_value())[0]
            print(result)
            result = str(var_array[i][1].get_assigned_value()[1]* food[(var_array[i][1].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][1].get_assigned_value())[0]][4] + ' of ' + (var_array[i][1].get_assigned_value())[0]
            print(result)
            result = str(var_array[i][2].get_assigned_value()[1]* food[(var_array[i][2].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][2].get_assigned_value())[0]][4] + ' of ' + (var_array[i][2].get_assigned_value())[0]
            print(result)
            result = str(var_array[i][3].get_assigned_value()[1]* food[(var_array[i][3].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][3].get_assigned_value())[0]][4] + ' of ' + (var_array[i][3].get_assigned_value())[0]
            print(result)
            print('Lunch:')
            result = str(var_array[i][4].get_assigned_value()[1]* food[(var_array[i][4].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][4].get_assigned_value())[0]][4] + ' of ' + (var_array[i][4].get_assigned_value())[0]
            print(result)
            result = str(var_array[i][5].get_assigned_value()[1]* food[(var_array[i][5].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][5].get_assigned_value())[0]][4] + ' of ' + (var_array[i][5].get_assigned_value())[0]
            print(result)
            result = str(var_array[i][6].get_assigned_value()[1]* food[(var_array[i][6].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][6].get_assigned_value())[0]][4] + ' of ' + (var_array[i][6].get_assigned_value())[0]
            print(result)
            result = str(var_array[i][7].get_assigned_value()[1]* food[(var_array[i][7].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][7].get_assigned_value())[0]][4] + ' of ' + (var_array[i][7].get_assigned_value())[0]
            print(result)
            print('Dinner:')
            result = str(var_array[i][8].get_assigned_value()[1]* food[(var_array[i][8].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][8].get_assigned_value())[0]][4] + ' of ' + (var_array[i][8].get_assigned_value())[0]
            print(result)
            result = str(var_array[i][9].get_assigned_value()[1]* food[(var_array[i][9].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][9].get_assigned_value())[0]][4] + ' of ' + (var_array[i][9].get_assigned_value())[0]
            print(result)
            result = str(var_array[i][10].get_assigned_value()[1]* food[(var_array[i][10].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][10].get_assigned_value())[0]][4] + ' of ' + (var_array[i][10].get_assigned_value())[0]
            print(result)
            result = str(var_array[i][11].get_assigned_value()[1]* food[(var_array[i][11].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][11].get_assigned_value())[0]][4] + ' of ' + (var_array[i][11].get_assigned_value())[0]
            print(result) 

        if i == 2:
            print( ' ')
            print('Wednesday:')
            print('Breakfast:')
            result = str(var_array[i][0].get_assigned_value()[1] * food[(var_array[i][0].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][0].get_assigned_value())[0]][4] + ' of ' + (var_array[i][0].get_assigned_value())[0]
            print(result)
            result = str(var_array[i][1].get_assigned_value()[1]* food[(var_array[i][1].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][1].get_assigned_value())[0]][4] + ' of ' + (var_array[i][1].get_assigned_value())[0]
            print(result)
            result = str(var_array[i][2].get_assigned_value()[1]* food[(var_array[i][2].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][2].get_assigned_value())[0]][4] + ' of ' + (var_array[i][2].get_assigned_value())[0]
            print(result)
            result = str(var_array[i][3].get_assigned_value()[1]* food[(var_array[i][3].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][3].get_assigned_value())[0]][4] + ' of ' + (var_array[i][3].get_assigned_value())[0]
            print(result)
            print('Lunch:')
            result = str(var_array[i][4].get_assigned_value()[1]* food[(var_array[i][4].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][4].get_assigned_value())[0]][4] + ' of ' + (var_array[i][4].get_assigned_value())[0]
            print(result)
            result = str(var_array[i][5].get_assigned_value()[1]* food[(var_array[i][5].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][5].get_assigned_value())[0]][4] + ' of ' + (var_array[i][5].get_assigned_value())[0]
            print(result)
            result = str(var_array[i][6].get_assigned_value()[1]* food[(var_array[i][6].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][6].get_assigned_value())[0]][4] + ' of ' + (var_array[i][6].get_assigned_value())[0]
            print(result)
            result = str(var_array[i][7].get_assigned_value()[1]* food[(var_array[i][7].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][7].get_assigned_value())[0]][4] + ' of ' + (var_array[i][7].get_assigned_value())[0]
            print(result)
            print('Dinner:')
            result = str(var_array[i][8].get_assigned_value()[1]* food[(var_array[i][8].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][8].get_assigned_value())[0]][4] + ' of ' + (var_array[i][8].get_assigned_value())[0]
            print(result)
            result = str(var_array[i][9].get_assigned_value()[1]* food[(var_array[i][9].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][9].get_assigned_value())[0]][4] + ' of ' + (var_array[i][9].get_assigned_value())[0]
            print(result)
            result = str(var_array[i][10].get_assigned_value()[1]* food[(var_array[i][10].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][10].get_assigned_value())[0]][4] + ' of ' + (var_array[i][10].get_assigned_value())[0]
            print(result)
            result = str(var_array[i][11].get_assigned_value()[1]* food[(var_array[i][11].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][11].get_assigned_value())[0]][4] + ' of ' + (var_array[i][11].get_assigned_value())[0]
            print(result) 
            
        if i == 3:
            print( ' ')
            print('Thursday:')
            print('Breakfast:')
            result = str(var_array[i][0].get_assigned_value()[1] * food[(var_array[i][0].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][0].get_assigned_value())[0]][4] + ' of ' + (var_array[i][0].get_assigned_value())[0]
            print(result)
            result = str(var_array[i][1].get_assigned_value()[1]* food[(var_array[i][1].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][1].get_assigned_value())[0]][4] + ' of ' + (var_array[i][1].get_assigned_value())[0]
            print(result)
            result = str(var_array[i][2].get_assigned_value()[1]* food[(var_array[i][2].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][2].get_assigned_value())[0]][4] + ' of ' + (var_array[i][2].get_assigned_value())[0]
            print(result)
            result = str(var_array[i][3].get_assigned_value()[1]* food[(var_array[i][3].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][3].get_assigned_value())[0]][4] + ' of ' + (var_array[i][3].get_assigned_value())[0]
            print(result)
            print('Lunch:')
            result = str(var_array[i][4].get_assigned_value()[1]* food[(var_array[i][4].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][4].get_assigned_value())[0]][4] + ' of ' + (var_array[i][4].get_assigned_value())[0]
            print(result)
            result = str(var_array[i][5].get_assigned_value()[1]* food[(var_array[i][5].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][5].get_assigned_value())[0]][4] + ' of ' + (var_array[i][5].get_assigned_value())[0]
            print(result)
            result = str(var_array[i][6].get_assigned_value()[1]* food[(var_array[i][6].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][6].get_assigned_value())[0]][4] + ' of ' + (var_array[i][6].get_assigned_value())[0]
            print(result)
            result = str(var_array[i][7].get_assigned_value()[1]* food[(var_array[i][7].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][7].get_assigned_value())[0]][4] + ' of ' + (var_array[i][7].get_assigned_value())[0]
            print(result)
            print('Dinner:')
            result = str(var_array[i][8].get_assigned_value()[1]* food[(var_array[i][8].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][8].get_assigned_value())[0]][4] + ' of ' + (var_array[i][8].get_assigned_value())[0]
            print(result)
            result = str(var_array[i][9].get_assigned_value()[1]* food[(var_array[i][9].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][9].get_assigned_value())[0]][4] + ' of ' + (var_array[i][9].get_assigned_value())[0]
            print(result)
            result = str(var_array[i][10].get_assigned_value()[1]* food[(var_array[i][10].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][10].get_assigned_value())[0]][4] + ' of ' + (var_array[i][10].get_assigned_value())[0]
            print(result)
            result = str(var_array[i][11].get_assigned_value()[1]* food[(var_array[i][11].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][11].get_assigned_value())[0]][4] + ' of ' + (var_array[i][11].get_assigned_value())[0]
            print(result) 
            
        if i == 4:
            print( ' ')
            print('Friday:')
            print('Breakfast:')
            result = str(var_array[i][0].get_assigned_value()[1] * food[(var_array[i][0].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][0].get_assigned_value())[0]][4] + ' of ' + (var_array[i][0].get_assigned_value())[0]
            print(result)
            result = str(var_array[i][1].get_assigned_value()[1]* food[(var_array[i][1].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][1].get_assigned_value())[0]][4] + ' of ' + (var_array[i][1].get_assigned_value())[0]
            print(result)
            result = str(var_array[i][2].get_assigned_value()[1]* food[(var_array[i][2].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][2].get_assigned_value())[0]][4] + ' of ' + (var_array[i][2].get_assigned_value())[0]
            print(result)
            result = str(var_array[i][3].get_assigned_value()[1]* food[(var_array[i][3].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][3].get_assigned_value())[0]][4] + ' of ' + (var_array[i][3].get_assigned_value())[0]
            print(result)
            print('Lunch:')
            result = str(var_array[i][4].get_assigned_value()[1]* food[(var_array[i][4].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][4].get_assigned_value())[0]][4] + ' of ' + (var_array[i][4].get_assigned_value())[0]
            print(result)
            result = str(var_array[i][5].get_assigned_value()[1]* food[(var_array[i][5].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][5].get_assigned_value())[0]][4] + ' of ' + (var_array[i][5].get_assigned_value())[0]
            print(result)
            result = str(var_array[i][6].get_assigned_value()[1]* food[(var_array[i][6].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][6].get_assigned_value())[0]][4] + ' of ' + (var_array[i][6].get_assigned_value())[0]
            print(result)
            result = str(var_array[i][7].get_assigned_value()[1]* food[(var_array[i][7].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][7].get_assigned_value())[0]][4] + ' of ' + (var_array[i][7].get_assigned_value())[0]
            print(result)
            print('Dinner:')
            result = str(var_array[i][8].get_assigned_value()[1]* food[(var_array[i][8].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][8].get_assigned_value())[0]][4] + ' of ' + (var_array[i][8].get_assigned_value())[0]
            print(result)
            result = str(var_array[i][9].get_assigned_value()[1]* food[(var_array[i][9].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][9].get_assigned_value())[0]][4] + ' of ' + (var_array[i][9].get_assigned_value())[0]
            print(result)
            result = str(var_array[i][10].get_assigned_value()[1]* food[(var_array[i][10].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][10].get_assigned_value())[0]][4] + ' of ' + (var_array[i][10].get_assigned_value())[0]
            print(result)
            result = str(var_array[i][11].get_assigned_value()[1]* food[(var_array[i][11].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][11].get_assigned_value())[0]][4] + ' of ' + (var_array[i][11].get_assigned_value())[0]
            print(result) 
            
        if i == 5:
            print(' ')
            print('Saturday:')
            print('Breakfast:')
            result = str(var_array[i][0].get_assigned_value()[1] * food[(var_array[i][0].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][0].get_assigned_value())[0]][4] + ' of ' + (var_array[i][0].get_assigned_value())[0]
            print(result)
            result = str(var_array[i][1].get_assigned_value()[1]* food[(var_array[i][1].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][1].get_assigned_value())[0]][4] + ' of ' + (var_array[i][1].get_assigned_value())[0]
            print(result)
            result = str(var_array[i][2].get_assigned_value()[1]* food[(var_array[i][2].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][2].get_assigned_value())[0]][4] + ' of ' + (var_array[i][2].get_assigned_value())[0]
            print(result)
            result = str(var_array[i][3].get_assigned_value()[1]* food[(var_array[i][3].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][3].get_assigned_value())[0]][4] + ' of ' + (var_array[i][3].get_assigned_value())[0]
            print(result)
            print('Lunch:')
            result = str(var_array[i][4].get_assigned_value()[1]* food[(var_array[i][4].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][4].get_assigned_value())[0]][4] + ' of ' + (var_array[i][4].get_assigned_value())[0]
            print(result)
            result = str(var_array[i][5].get_assigned_value()[1]* food[(var_array[i][5].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][5].get_assigned_value())[0]][4] + ' of ' + (var_array[i][5].get_assigned_value())[0]
            print(result)
            result = str(var_array[i][6].get_assigned_value()[1]* food[(var_array[i][6].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][6].get_assigned_value())[0]][4] + ' of ' + (var_array[i][6].get_assigned_value())[0]
            print(result)
            result = str(var_array[i][7].get_assigned_value()[1]* food[(var_array[i][7].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][7].get_assigned_value())[0]][4] + ' of ' + (var_array[i][7].get_assigned_value())[0]
            print(result)
            print('Dinner:')
            result = str(var_array[i][8].get_assigned_value()[1]* food[(var_array[i][8].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][8].get_assigned_value())[0]][4] + ' of ' + (var_array[i][8].get_assigned_value())[0]
            print(result)
            result = str(var_array[i][9].get_assigned_value()[1]* food[(var_array[i][9].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][9].get_assigned_value())[0]][4] + ' of ' + (var_array[i][9].get_assigned_value())[0]
            print(result)
            result = str(var_array[i][10].get_assigned_value()[1]* food[(var_array[i][10].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][10].get_assigned_value())[0]][4] + ' of ' + (var_array[i][10].get_assigned_value())[0]
            print(result)
            result = str(var_array[i][11].get_assigned_value()[1]* food[(var_array[i][11].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][11].get_assigned_value())[0]][4] + ' of ' + (var_array[i][11].get_assigned_value())[0]
            print(result)  
            
        if i == 6:
            print(' ')
            print('Sunday:')
            print('Breakfast:')
            result = str(var_array[i][0].get_assigned_value()[1] * food[(var_array[i][0].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][0].get_assigned_value())[0]][4] + ' of ' + (var_array[i][0].get_assigned_value())[0]
            print(result)
            result = str(var_array[i][1].get_assigned_value()[1]* food[(var_array[i][1].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][1].get_assigned_value())[0]][4] + ' of ' + (var_array[i][1].get_assigned_value())[0]
            print(result)
            result = str(var_array[i][2].get_assigned_value()[1]* food[(var_array[i][2].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][2].get_assigned_value())[0]][4] + ' of ' + (var_array[i][2].get_assigned_value())[0]
            print(result)
            result = str(var_array[i][3].get_assigned_value()[1]* food[(var_array[i][3].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][3].get_assigned_value())[0]][4] + ' of ' + (var_array[i][3].get_assigned_value())[0]
            print(result)
            print('Lunch:')
            result = str(var_array[i][4].get_assigned_value()[1]* food[(var_array[i][4].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][4].get_assigned_value())[0]][4] + ' of ' + (var_array[i][4].get_assigned_value())[0]
            print(result)
            result = str(var_array[i][5].get_assigned_value()[1]* food[(var_array[i][5].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][5].get_assigned_value())[0]][4] + ' of ' + (var_array[i][5].get_assigned_value())[0]
            print(result)
            result = str(var_array[i][6].get_assigned_value()[1]* food[(var_array[i][6].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][6].get_assigned_value())[0]][4] + ' of ' + (var_array[i][6].get_assigned_value())[0]
            print(result)
            result = str(var_array[i][7].get_assigned_value()[1]* food[(var_array[i][7].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][7].get_assigned_value())[0]][4] + ' of ' + (var_array[i][7].get_assigned_value())[0]
            print(result)
            print('Dinner:')
            result = str(var_array[i][8].get_assigned_value()[1]* food[(var_array[i][8].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][8].get_assigned_value())[0]][4] + ' of ' + (var_array[i][8].get_assigned_value())[0]
            print(result)
            result = str(var_array[i][9].get_assigned_value()[1]* food[(var_array[i][9].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][9].get_assigned_value())[0]][4] + ' of ' + (var_array[i][9].get_assigned_value())[0]
            print(result)
            result = str(var_array[i][10].get_assigned_value()[1]* food[(var_array[i][10].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][10].get_assigned_value())[0]][4] + ' of ' + (var_array[i][10].get_assigned_value())[0]
            print(result)
            result = str(var_array[i][11].get_assigned_value()[1]* food[(var_array[i][11].get_assigned_value())[0]][3]) + ' ' + food[(var_array[i][11].get_assigned_value())[0]][4] + ' of ' + (var_array[i][11].get_assigned_value())[0]
            print(result) 



if __name__ == "__main__":
    #csp, var_array, food = mealplan_csp_model()
    #solver = BT(csp)
    #print("One Week Meal Plan")
    ##print("FC")
    ##solver.bt_search(prop_FC)
    ##print("GAC")
    #has_soln = solver.bt_search(prop_GAC)
    #if has_soln:
        #print("Solution")
        #print_mealplan_soln(var_array, food)
    #else:
        #pass
    
    print(' ')
    csp, var_array, food = mealplan_min_csp_model()
    solver = BT(csp)
    print("One Day Meal Plan with budget")
    #print("FC")
    #solver.bt_search(prop_FC)
    #print("GAC")
    has_soln = solver.bt_search(prop_GAC)
    if has_soln:
        print("Solution")
        print_min_mealplan_soln(var_array, food)
    else:
        pass    
    













