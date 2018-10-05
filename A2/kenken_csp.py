#Look for #IMPLEMENT tags in this file.

'''
Construct and return Kenken CSP model.
'''

from cspbase import *
import itertools

def kenken_csp_model(kenken_grid):
    '''Returns a CSP object representing a Kenken CSP problem along 
       with an array of variables for the problem. That is return

       kenken_csp, variable_array

       where kenken_csp is a csp representing the kenken model
       and variable_array is a list of lists

       [ [  ]
         [  ]
         .
         .
         .
         [  ] ]

       such that variable_array[i][j] is the Variable (object) that
       you built to represent the value to be placed in cell i,j of
       the board (indexed from (0,0) to (N-1,N-1))

       
       The input grid is specified as a list of lists. The first list
	   has a single element which is the size N; it represents the
	   dimension of the square board.
	   
	   Every other list represents a constraint a cage imposes by 
	   having the indexes of the cells in the cage (each cell being an 
	   integer out of 11,...,NN), followed by the target number and the
	   operator (the operator is also encoded as an integer with 0 being
	   '+', 1 being '-', 2 being '/' and 3 being '*'). If a list has two
	   elements, the first element represents a cell, and the second 
	   element is the value imposed to that cell. With this representation,
	   the input will look something like this:
	   
	   [[N],[cell_ij,...,cell_i'j',target_num,operator],...]
	   
       This routine returns a model which consists of a variable for
       each cell of the board, with domain equal to {1-N}.
       
       This model will also contain BINARY CONSTRAINTS OF NOT-EQUAL between
       all relevant variables (e.g., all pairs of variables in the
       same row, etc.) and an n-ary constraint for each cage in the grid.
    '''

    ##IMPLEMENT
    size = kenken_grid[0][0]

    var = generate_var_array(size)

    #constraints
    row_cons = [binary_constraint(i, ji, i, jj, var)
                for i in range(size)
                for ji in range(size) for jj in range(size)
                if ji < jj]
    col_cons = [binary_constraint(ii, j, ij, j, var)
                for j in range(size)
                for ii in range(size) for ij in range(size)
                if ii < ij]
    cons = []

    #cage
    cage = kenken_grid[1:]
    num = 1
    for i in cage:
        
        scope = []
        coor = []
        for v in i[:-2]:
            scope.append(var[v // 10 - 1][v % 10 - 1])
            coor.append((v // 10 - 1, v % 10 - 1))
        coor_x = set([int(c[0]) for c in coor])
        coor_y = set([int(c[1]) for c in coor])
        if (len(coor_x) > 1) and (len(coor_y) > 1):
            com = list(itertools.combinations_with_replacement(range(1, size + 1), len(i[:-2])))
        else:
            com = list(itertools.combinations(range(1, size + 1), len(i[:-2])))
            
        sat_tup = []
        for tup in com:
            if i[-1] == 0:
                if sum(tup) == i[-2]:
                    per = list(itertools.permutations(list(tup), len(tup)))
                    sat_tup.extend(per)
            if i[-1] == 1:
                per = list(itertools.permutations(list(tup), len(tup)))
                for p in per:
                    result = p[0]
                    for n in range(1, len(p)):
                        result -= p[n]
                    if result == i[-2]:
                        sat_tup.extend(per)
            if i[-1] == 2:
                per = list(itertools.permutations(list(tup), len(tup)))
                for p in per:
                    result = p[0]
                    for n in range(1, len(p)):
                        result = result / p[n]
                    if result == i[-2]:
                        sat_tup.extend(per)                              
            if i[-1] == 3:
                product = 1
                for n in tup:
                    product = product * n
                if product == i[-2]:
                    per = list(itertools.permutations(list(tup), len(tup)))
                    sat_tup.extend(per)
         
        
        name = "N({0})".format(num)
        num += 1
        constraint = Constraint(name, scope)
        constraint.add_satisfying_tuples(sat_tup)
        cons.append(constraint)
        
    cons.extend(row_cons)
    cons.extend(col_cons)
    v_new = []
    for i in range(len(var)):
        for j in range(len(var)):
            v_new.append(var[i][j])
    csp = CSP("kenken", v_new)   
    for c in cons:
        csp.add_constraint(c)
    return csp, var        


def generate_var_array(n):
    """
    Generate a variable array with the correct size.
    """
    var_array = []
    domain = list(range(1, n + 1))

    for i in range(n):
        var_array.append([])
        for j in range(n):
            var_name = "V_" + str(i) + str(j)
            var = Variable(var_name, domain)
            var_array[i].append(var)
    return var_array


def binary_constraint(ii, ji, ij, jj, var):
    """
    Create binary constraint
    """
    var1 = var[ii][ji]
    var2 = var[ij][jj]
    name = "B({0},{1})".format(var1.name[-2:], var2.name[-2:])
    scope = [var1, var2]
    constraint = Constraint(name, scope)
    satisfying_tuple = [(value1, value2)
                        for value1 in var1.domain() for value2 in var2.domain()
                        if value1 != value2]
    constraint.add_satisfying_tuples(satisfying_tuple)
    return constraint
