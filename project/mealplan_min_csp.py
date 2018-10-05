from mealplan import *
from csp_base import *
from random import shuffle
import itertools

def mealplan_min_csp_model():
    while True:
        age = input("Age: ")
        try:
            a = int(age)
            if a < 0 or a > 125: 
                print("Please enter a valid age")
                continue
            break
        except ValueError:
            print("Please enter a valid age")     
    print(a)
    
    while True:
        gender = input("Gender(M/F): ")
        try:
            g = gender
            if g != 'M' and g != 'F': 
                print("Please enter a valid gender")
                continue
            break
        except ValueError:
            print("Please enter a valid gender")     
    print(g)
    
    while True:
        height = input("Height(cm): ")
        try:
            h = float(height)
            if h < 20 or h > 255: 
                print("Please enter a valid height")
                continue
            break
        except ValueError:
            print("Please enter a valid height")     
    print(h)
    
    while True:
        weight = input("Weight(kg): ")
        try:
            w = float(weight)
            if w < 1 or h > 635: 
                print("Please enter a valid weight")
                continue
            break
        except ValueError:
            print("Please enter a valid weight")     
    print(w)
    
    while True:
        print('Exercise levels listed:')
        print('A. Little to no exercise')
        print('B. Light exercise (1–3 days per week)')
        print('C. Moderate exercise (3–5 days per week)')
        print('D. Heavy exercise (6–7 days per week)')
        print('E. Very heavy exercise (twice per day, extra heavy workouts)')    
        
        exercise = input("Please enter your exercise level: ")
        try:
            e = exercise
            if e not in ['a','b','c','d','e','A','B','C','D','E']: 
                print("Please enter a valid option")
                continue
            break
        except ValueError:
            print("Please enter a valid option")     
    print(e)
    
    BMR = 0
    if g == 'M':
        BMR = 88.362 + (13.397 * w) + (4.799 * h) - (5.677 * a)
    if g == 'F':
        BMR = 447.593 + (9.247 * w) + (3.098 * h) - (4.330 * a)
    
    cal = 0
    if e in ['A', 'a']:
        cal = BMR * 1.2
    if e in ['B', 'b']:
        cal = BMR * 1.375
    if e in ['C', 'c']:
        cal = BMR * 1.55
    if e in ['D', 'd']:
        cal = BMR * 1.725
    if e in ['E', 'e']:
        cal = BMR * 1.9
    
    print('Your suggested intake calories per day is ' + str(cal))
    
    while True:
        bc = input('Please enter your expected calories intake for breakfast: ')
        try:
            b_c = float(bc)
            if b_c < 0: 
                print("The calories value has to be a positive number")
                continue
            break
        except ValueError:
            print("The calories value has to be a number")     
    print(b_c)
    
    while True:
        lc = input('Please enter your expected calories intake for lunch: ')
        try:
            l_c = float(lc)
            if l_c < 0: 
                print("The calories value has to be a positive number")
                continue
            break
        except ValueError:
            print("The calories value has to be a number")     
    print(l_c)
    
    while True:
        dc = input('Please enter your expected calories intake for dinner: ')
        try:
            d_c = float(dc)
            if d_c < 0: 
                print("The calories value has to be a positive number")
                continue
            break
        except ValueError:
            print("The calories value has to be a number")     
    print(d_c)
    
    allergies = input("Please enter the food that you are allergic to(all lowercases singular words seperated by comma): ")
    allergy_inputed = allergies.split(',')
    allergy_available = []
    for i in allergy_inputed:
        if i.strip() in mealplan.food:
            allergy_available.append(i.strip())
    
    
    
    not_for_b = input("Please enter the food that you don't want to eat for breakfast(all lowercases singular words seperated by comma): ")
    not_fb = not_for_b.split(',')
    nfb = []
    nfb_all = []
    for i in not_fb:
        nfb_all.append(i.strip())
        if i.strip() in mealplan.food:
            nfb.append(i.strip())
	    
               
    not_for_l = input("Please enter the food that you don't want to eat for lunch(all lowercases singular words seperated by comma): ")
    not_fl = not_for_l.split(',')
    nfl = []
    nfl_all = []
    for i in not_fl:
        nfl_all.append(i.strip())
        if i.strip() in mealplan.food:
            nfl.append(i.strip())

    
    not_for_d = input("Please enter the food that you don't want to eat for dinner(all lowercases singular words seperated by comma): ")
    not_fd = not_for_d.split(',')
    nfd = []
    nfd_all = []
    for i in not_fd:
        nfd_all.append(i.strip())
        if i.strip() in mealplan.food:
            nfd.append(i.strip())
	    
            

    
    #want to eat xxx
    valid = False
    while valid == False:
        for_b = input("Please enter the food that you want to eat for breakfast(all lowercases singular words seperated by comma): ")
        fl = for_b.split(',')
        b_dict = []
        if for_b == '':
            break
        all_valid = True
        not_in = ''
        for i in fl:
            if i.strip() in mealplan.food:
                b_dict.append(i.strip())
            else:
                not_in += i.strip() + ', '
                all_valid = False
        if all_valid:
            valid = True
        else:
            print('Note that '+ not_in +'is not in the database!')	
	

            
    valid = False
    while valid == False:
        for_l = input("Please enter the food that you want to eat for lunch(all lowercases singular words seperated by comma): ")
        fl = for_l.split(',')
        l_dict = []
        not_in = ''
        if for_l == '':
            break
        all_valid = True
        for i in fl:
            if i.strip() in mealplan.food:
                l_dict.append(i.strip())
            else:
                not_in += i.strip() + ', '		
                all_valid = False
        if all_valid:
            valid = True
        else:
            print('Note that '+ not_in +'is not in the database!')		
			
		
		
		
 
    
    valid = False
    while valid == False:
        for_d = input("Please enter the food that you want to eat for dinner(all lowercases singular words seperated by comma): ")
        fd = for_d.split(',')
        d_dict = []
        not_in = ''
        if for_d == '':
            break
        all_valid = True
        for i in fd:
            if i.strip() in mealplan.food:
                d_dict.append(i.strip())
            else:
                not_in += i.strip() + ', '	
                all_valid = False
        if all_valid:
            valid = True
        else:
            print('Note that '+ not_in +'is not in the database!')
	     

    t = False
    while True:
        twice = input("Do you mind eating the same food twice or more in a day(Y/N): ") #yes = mind
        try:
    
            if twice == 'Y':
                t = True
            if twice != 'Y' and twice != 'N': 
                print("Please enter a valid option")
                continue
            break
        except ValueError:
            print("Please enter a valid option")     
    
    while True:
        budgetb = input("What is your budget for breakfast?")
        try:
            bb = float(budgetb)
            if bb < 0 : 
                print("Please enter a valid number")
                continue
            break
        except ValueError:
            print("Please enter a valid number")
	    
    while True:
        budgetl = input("What is your budget for lunch?")
        try:
            bl = float(budgetl)
            if bl < 0 : 
                print("Please enter a valid number")
                continue
            break
        except ValueError:
            print("Please enter a valid number")
	    
    while True:
        budgetd = input("What is your budget for dinner?")
        try:
            bd = float(budgetd)
            if bd < 0 : 
                print("Please enter a valid number")
                continue
            break
        except ValueError:
            print("Please enter a valid number")     
    
    food = mealplan.food
    for aa in allergy_available:
        food.pop(aa, None)
        
    var_array = []
    #generating csp for breakfast

    for j in range(1,5):
        var_name = "B_" + str(j) #i = day of the week, j = category
        domain = []
        if j == 1:
            for f in food:
                if (food[f][1] == 'beverage' and (food[f][0] not in nfb) ):
                    domain.append((f, 1, food[f][-1] * 1))
                    domain.append((f, 2, food[f][-1] * 2))
        if j == 2:
            for f in food:
                if ((food[f][1] == 'meat' or food[f][0] == 'dairy') and (food[f][0] not in nfb)):
                    domain.append((f, 1, food[f][-1] * 1))
                    domain.append((f, 2, food[f][-1] * 2))
        if j == 3:
            for f in food:
                if (food[f][1] == 'vegetable' and food[f][0] not in nfb):
                    domain.append((f, 1, food[f][-1] * 1))
                    domain.append((f, 2, food[f][-1] * 2))    
        if j == 4:
            for f in food:
                if (food[f][1] == 'fruit' and food[f][0] not in nfb):
                    domain.append((f, 1, food[f][-1] * 1))
                    domain.append((f, 2, food[f][-1] * 2))   
        var = Variable(var_name, domain)
        var_array.append(var)
	
    for j in range(1,5):
        var_name = "L_"  + str(j) #i = day of the week, j = category
        domain = []
        if j == 1:
            for f in food:
                if (food[f][1] == 'beverage' and food[f][0] not in nfl):
                    domain.append((f, 1, food[f][-1] * 1))
                    domain.append((f, 2, food[f][-1] * 2))
        if j == 2:
            for f in food:
                if ((food[f][1] == 'meat' or food[f][0] == 'seafood') and food[f][0] not in nfl):
                    domain.append((f, 1, food[f][-1] * 1))
                    domain.append((f, 2, food[f][-1] * 2))
        if j == 3:
            for f in food:
                if (food[f][1] == 'main' and  food[f][0] not in nfl):
                    domain.append((f, 1, food[f][-1] * 1))
                    domain.append((f, 2, food[f][-1] * 2))    
        if j == 4:
            for f in food:
                if (food[f][1] == 'vegetable' and  food[f][0] not in nfl):
                    domain.append((f, 1, food[f][-1] * 1))
                    domain.append((f, 2, food[f][-1] * 2))
        var = Variable(var_name, domain)
        var_array.append(var)
    
    for j in range(1,5):
        var_name = "D_"  + str(j) #i = day of the week, j = category
        domain = []
        if j == 1:
            for f in food:
                if ((food[f][1] == 'meat' or food[f][1] == 'seafood') and food[f][0] not in nfd):
                    domain.append((f, 1, food[f][-1] * 1))
                    domain.append((f, 2, food[f][-1] * 2))
        if j == 2:
            for f in food:
                if (food[f][1] == 'main' and food[f][0] not in nfd):
                    domain.append((f, 1, food[f][-1] * 1))
                    domain.append((f, 2, food[f][-1] * 2))
        if j == 3:
            for f in food:
                if (food[f][1] == 'vegetable' and food[f][0] not in nfd):
                    domain.append((f, 1, food[f][-1] * 1))
                    domain.append((f, 2, food[f][-1] * 2))    
        if j == 4:
            for f in food:
                if (food[f][1] == 'fruit' and food[f][0] not in nfd):
                    domain.append((f, 1, food[f][-1] * 1))
                    domain.append((f, 2, food[f][-1] * 2))
        var = Variable(var_name, domain)
        var_array.append(var)    

    #--------------------------------------------------------------------------------------------------
    #breakfast
    cons = []
    
    

    scope = []
    iterables = []
    scope.append(var_array[0])
    iterables.append(var_array[0].domain())
    
    scope.append(var_array[1])
    iterables.append(var_array[1].domain())
    
    scope.append(var_array[2])
    iterables.append(var_array[2].domain())
    
    scope.append(var_array[3])
    iterables.append(var_array[3].domain())    

    pos_com = itertools.product(*iterables) 
    sat_tup = []
    for p in pos_com:
        total_cal = food[p[0][0]][2] * float(p[0][1]) + food[p[1][0]][2] * float(p[1][1]) + food[p[2][0]][2] * float(p[2][1]) + food[p[3][0]][2] * float(p[3][1])
        total_price = p[0][2] + p[1][2] + p[2][2] + p[3][2]
        if (total_cal <= b_c and total_price <= bb and (not b_dict)):
            sat_tup.append(p)
        if (total_cal <= b_c and total_price <= bb and b_dict):
            does_sat = True
            for j in b_dict:
                if ((str(j) != p[0][0]) and (str(j) != p[1][0]) and (str(j) != p[2][0]) and (str(j) != p[3][0]) ):
                    does_sat = False
            if does_sat:
                sat_tup.append(p)     
    

    
    name = "BC"
    constraint = Constraint(name, scope)
    constraint.add_satisfying_tuples(sat_tup)    
    cons.append(constraint)



    scope = []
    iterables = []
    scope.append(var_array[4])
    iterables.append(var_array[4].domain())
    
    scope.append(var_array[5])
    iterables.append(var_array[5].domain())
    
    scope.append(var_array[6])
    iterables.append(var_array[6].domain())
    
    scope.append(var_array[7])
    iterables.append(var_array[7].domain())  

    pos_com = itertools.product(*iterables) 
    sat_tup = []
    for p in pos_com:
        total_cal = food[p[0][0]][2] * float(p[0][1]) + food[p[1][0]][2] * float(p[1][1]) + food[p[2][0]][2] * float(p[2][1]) + food[p[3][0]][2] * float(p[3][1])
        total_price = p[0][2] + p[1][2] + p[2][2] + p[3][2]
        if (total_cal <= l_c and total_price <= bl and (not l_dict) ):
            sat_tup.append(p)
        if (total_cal <= l_c and total_price <= bl and l_dict ):
            does_sat = True
            for j in l_dict:
                if ((str(j) != p[0][0]) and (str(j) != p[1][0]) and (str(j) != p[2][0]) and (str(j) != p[3][0]) ):
                    does_sat = False
            if does_sat:
                sat_tup.append(p)       


    name = "LC"
    constraint = Constraint(name, scope)	
    constraint.add_satisfying_tuples(sat_tup)    
    cons.append(constraint)
    
    

    scope = []
    iterables = []
    scope.append(var_array[8])
    iterables.append(var_array[8].domain())
    
    scope.append(var_array[9])
    iterables.append(var_array[9].domain())
    
    scope.append(var_array[10])
    iterables.append(var_array[10].domain())
    
    scope.append(var_array[11])
    iterables.append(var_array[11].domain())    

    pos_com = itertools.product(*iterables) 
    sat_tup = []
    
    
    for p in pos_com:
        total_cal = food[p[0][0]][2] * float(p[0][1]) + food[p[1][0]][2] * float(p[1][1]) + food[p[2][0]][2] * float(p[2][1]) + food[p[3][0]][2] * float(p[3][1])
        total_price = p[0][2] + p[1][2] + p[2][2] + p[3][2]
        if (total_cal <= d_c and total_price <= bd and (not d_dict) ):
            sat_tup.append(p)
        if (total_cal <= d_c and total_price <= bd and d_dict ):
            does_sat = True
            for j in d_dict:
                if ((str(j) != p[0][0]) and (str(j) != p[1][0]) and (str(j) != p[2][0]) and (str(j) != p[3][0]) ):
                    does_sat = False
            if does_sat:
                sat_tup.append(p)    
  
    name = "DC"
    constraint = Constraint(name, scope)
    constraint.add_satisfying_tuples(sat_tup)    
    cons.append(constraint)
    
    if t == True:  
        scope = []
        iterables = []
	
        scope.append(var_array[0])
        iterables.append(var_array[0].domain())
	
        scope.append(var_array[4])
        iterables.append(var_array[4].domain())
	
        pos_com = itertools.product(*iterables) 
        sat_tup = []
	
        for p in pos_com:
            if p[0][0] != p[1][0]:
                sat_tup.append(p)
		
    
        name = "BLB"
        constraint = Constraint(name, scope)
        constraint.add_satisfying_tuples(sat_tup)    
        cons.append(constraint)    
	

    scope = []
    iterables = []
    
    scope.append(var_array[1])
    iterables.append(var_array[1].domain())
    
    scope.append(var_array[5])
    iterables.append(var_array[5].domain())
    
    scope.append(var_array[8])
    iterables.append(var_array[8].domain())    
    
    pos_com = itertools.product(*iterables) 
    sat_tup = []
    
    for p in pos_com:
	#print(p)
        if (p[0][0] != p[1][0] and p[0][0] != p[2][0] and p[2][0] != p[1][0]):
            sat_tup.append(p)
	    

    name = "BLDM"
    constraint = Constraint(name, scope)
    constraint.add_satisfying_tuples(sat_tup)    
    cons.append(constraint)  
	
 
    scope = []
    iterables = []
    
    scope.append(var_array[2])
    iterables.append(var_array[2].domain())
    
    scope.append(var_array[7])
    iterables.append(var_array[7].domain())
    
    scope.append(var_array[10])
    iterables.append(var_array[10].domain())    
    
    pos_com = itertools.product(*iterables) 
    sat_tup = []
    
    for p in pos_com:
        if (p[0][0] != p[1][0] and p[0][0] != p[2][0] and p[2][0] != p[1][0]):
            sat_tup.append(p)
	    

    name = "BLDV"
    constraint = Constraint(name, scope)
    constraint.add_satisfying_tuples(sat_tup)    
    cons.append(constraint)  
	
	    

    scope = []
    iterables = []
    
    scope.append(var_array[3])
    iterables.append(var_array[3].domain())
    
    scope.append(var_array[11])                                                        
    iterables.append(var_array[11].domain())
    
    pos_com = itertools.product(*iterables) 
    sat_tup = []
    
    for p in pos_com:
        if p[0][0] != p[1][0]:
            sat_tup.append(p)
	    

    name = "BDF"
    constraint = Constraint(name, scope)
    constraint.add_satisfying_tuples(sat_tup)    
    cons.append(constraint)    
    

    scope = []
    iterables = []
    
    scope.append(var_array[6])
    iterables.append(var_array[6].domain())
    
    scope.append(var_array[9])
    iterables.append(var_array[9].domain())
    
    pos_com = itertools.product(*iterables) 
    sat_tup = []
    
    for p in pos_com:
        if p[0][0] != p[1][0]:
            sat_tup.append(p)
	    

    name = "LDM"
    constraint = Constraint(name, scope)
    constraint.add_satisfying_tuples(sat_tup)    
    cons.append(constraint)  
            

    csp = CSP("mealplan", var_array)   
    for c in cons:
        csp.add_constraint(c)
    return csp, var_array, food      


















































## ignore
#from cspbase import *
#import itertools

#def kenken_csp_model(kenken_grid):
    #'''Returns a CSP object representing a Kenken CSP problem along 
       #with an array of variables for the problem. That is return

       #kenken_csp, variable_array

       #where kenken_csp is a csp representing the kenken model
       #and variable_array is a list of lists

       #[ [  ]
         #[  ]
         #.
         #.
         #.
         #[  ] ]

       #such that variable_array[i][j] is the Variable (object) that
       #you built to represent the value to be placed in cell i,j of
       #the board (indexed from (0,0) to (N-1,N-1))

       
       #The input grid is specified as a list of lists. The first list
	   #has a single element which is the size N; it represents the
	   #dimension of the square board.
	   
	   #Every other list represents a constraint a cage imposes by 
	   #having the indexes of the cells in the cage (each cell being an 
	   #integer out of 11,...,NN), followed by the target number and the
	   #operator (the operator is also encoded as an integer with 0 being
	   #'+', 1 being '-', 2 being '/' and 3 being '*'). If a list has two
	   #elements, the first element represents a cell, and the second 
	   #element is the value imposed to that cell. With this representation,
	   #the input will look something like this:
	   
	   #[[N],[cell_ij,...,cell_i'j',target_num,operator],...]
	   
       #This routine returns a model which consists of a variable for
       #each cell of the board, with domain equal to {1-N}.
       
       #This model will also contain BINARY CONSTRAINTS OF NOT-EQUAL between
       #all relevant variables (e.g., all pairs of variables in the
       #same row, etc.) and an n-ary constraint for each cage in the grid.
    #'''

    ###IMPLEMENT
    #size = kenken_grid[0][0]

    #var = generate_var_array(size)

    ##constraints
    #row_cons = [binary_constraint(i, ji, i, jj, var)
                #for i in range(size)
                #for ji in range(size) for jj in range(size)
                #if ji < jj]
    #col_cons = [binary_constraint(ii, j, ij, j, var)
                #for j in range(size)
                #for ii in range(size) for ij in range(size)
                #if ii < ij]
    #cons = []

    ##cage
    #cage = kenken_grid[1:]
    #num = 1
    #for i in cage:
        
        #scope = []
        #coor = []
        #for v in i[:-2]:
            #scope.append(var[v // 10 - 1][v % 10 - 1])
            #coor.append((v // 10 - 1, v % 10 - 1))
        #coor_x = set([int(c[0]) for c in coor])
        #coor_y = set([int(c[1]) for c in coor])
        #if (len(coor_x) > 1) and (len(coor_y) > 1):
            #com = list(itertools.combinations_with_replacement(range(1, size + 1), len(i[:-2])))
        #else:
            #com = list(itertools.combinations(range(1, size + 1), len(i[:-2])))
            
        #sat_tup = []
        #for tup in com:
            #if i[-1] == 0:
                #if sum(tup) == i[-2]:
                    #per = list(itertools.permutations(list(tup), len(tup)))
                    #sat_tup.extend(per)
            #if i[-1] == 1:
                #per = list(itertools.permutations(list(tup), len(tup)))
                #for p in per:
                    #result = p[0]
                    #for n in range(1, len(p)):
                        #result -= p[n]
                    #if result == i[-2]:
                        #sat_tup.extend(per)
            #if i[-1] == 2:
                #per = list(itertools.permutations(list(tup), len(tup)))
                #for p in per:
                    #result = p[0]
                    #for n in range(1, len(p)):
                        #result = result / p[n]
                    #if result == i[-2]:
                        #sat_tup.extend(per)                              
            #if i[-1] == 3:
                #product = 1
                #for n in tup:
                    #product = product * n
                #if product == i[-2]:
                    #per = list(itertools.permutations(list(tup), len(tup)))
                    #sat_tup.extend(per)
         
        
        #name = "N({0})".format(num)
        #num += 1
        #constraint = Constraint(name, scope)
        #constraint.add_satisfying_tuples(sat_tup)
        #cons.append(constraint)
        
    #cons.extend(row_cons)
    #cons.extend(col_cons)
    #v_new = []
    #for i in range(len(var)):
        #for j in range(len(var)):
            #v_new.append(var[i][j])
    #csp = CSP("kenken", v_new)   
    #for c in cons:
        #csp.add_constraint(c)
    #return csp, var        


