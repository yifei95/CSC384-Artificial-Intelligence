#Look for #IMPLEMENT tags in this file. These tags indicate what has
#to be implemented to complete the Snowman Puzzle domain.

#   You may add only standard python imports---i.e., ones that are automatically
#   available on TEACH.CS
#   You may not remove any imports.
#   You may not import or otherwise source any of your own files

# import os for time functions
import os
from search import * #for search engines
from snowman import SnowmanState, Direction, snowman_goal_state #for snowball specific classes and problems
from test_problems import PROBLEMS #20 test problems

#snowball HEURISTICS
def heur_simple(state):
  '''trivial admissible snowball heuristic'''
  '''INPUT: a snowball state'''
  '''OUTPUT: a numeric value that serves as an estimate of the distance of the state (# of moves required to get) to the goal.'''   
  return len(state.snowballs)

def heur_zero(state):
  return 0

def heur_manhattan_distance(state):
#IMPLEMENT
    '''admissible snowball puzzle heuristic: manhattan distance'''
    '''INPUT: a snowball state'''
    '''OUTPUT: a numeric value that serves as an estimate of the distance of the state to the goal.'''      
    #We want an admissible heuristic, which is an optimistic heuristic. 
    #It must always underestimate the cost to get from the current state to the goal.
    #The sum of the Manhattan distances between the snowballs and the destination for the Snowman is such a heuristic.  
    #When calculating distances, assume there are no obstacles on the grid.
    #You should implement this heuristic function exactly, even if it is tempting to improve it.
    #Your function should return a numeric value; this is the estimate of the distance to the goal.
    result = 0
    coords = state.snowballs.keys()
    dest = state.destination
    snowb = state.snowballs
    for i in coords:
      # for snowballs with sizes A, B, C, double the distance
      if snowb[i] == 6:  
        result += 3 * (abs(i[0] - dest[0]) + abs(i[1] - dest[1]))
      elif snowb[i] >= 3:  
        result += 2 * (abs(i[0] - dest[0]) + abs(i[1] - dest[1]))
      else:
        result += abs(i[0] - dest[0]) + abs(i[1] - dest[1])
    
    return result

def heur_alternate(state): 
#IMPLEMENT
    '''a better heuristic'''
    '''INPUT: a snowball state'''
    '''OUTPUT: a numeric value that serves as an estimate of the distance of the state to the goal.'''        
    #heur_manhattan_distance has flaws.   
    #Write a heuristic function that improves upon heur_manhattan_distance to estimate distance between the current state and the goal.
    #Your function should return a numeric value for the estimate of the distance to the goal.
    result = 0
    coords = state.snowballs.keys()
    dest = state.destination
    snowb = state.snowballs
    obs = state.obstacles
    h = state.height - 1
    w = state.width - 1
    robot = state.robot
    for i in coords:
      #excluding corner cases when the snowball is not at the destination
      if i != dest:
        #snowball is at the corner of the board
        if ((i == (0, 0)) or (i == (0, h)) or (i == (w, 0)) or (i == (w, h))):
          return float("inf")
        
        
        #snowball is beside the wall but destination is not beside the same wall
        if (i[0] == 0) and (dest[0] != 0):
          return float("inf")
        if (i[1] == 0) and (dest[1] != 0):
          return float("inf")
        if (i[1] == h) and (dest[1] != h):
          return float("inf")
        if (i[0] == w) and (dest[0] != w):
          return float("inf")
        
        #snow ball is at the coner of a wall and an obstacle
        if (i[0] == 0) and (((0, i[1] + 1) in obs) or ((0, i[1] - 1) in obs)):
          return float("inf")
        if (i[1] == 0) and (((i[0] + 1, 0) in obs) or ((i[0] - 1, 0) in obs)):
          return float("inf")
        if (i[0] == w) and (((w, i[1] + 1) in obs) or ((w, i[1] - 1) in obs)):
          return float("inf")
        if (i[1] == h) and (((i[0] + 1, h) in obs) or ((i[0] - 1, h) in obs)):
          return float("inf")        
        
        #snowball is at the corner of two obstacles
        if ((i[0], i[1] - 1) in obs) and ((i[0] - 1, i[1]) in obs):
          return float("inf")
        if ((i[0], i[1] - 1) in obs) and ((i[0] + 1, i[1]) in obs):
          return float("inf")
        if ((i[0], i[1] + 1) in obs) and ((i[0] + 1, i[1]) in obs):
          return float("inf")
        if ((i[0], i[1] + 1) in obs) and ((i[0] - 1, i[1]) in obs):
          return float("inf")        
      
      # use Euclidean distance instead of Manhattan distance
      # for snowballs with sizes A, B, C, double the distance
      if snowb[i] == 6:
        result += 3 * (((i[0] - dest[0]) ** 2 + (i[1] - dest[1]) ** 2) ** 0.5)
        result += 3 * (((i[0] - robot[0]) ** 2 + (i[1] - robot[1]) ** 2) ** 0.5)
      if snowb[i] >= 3:
        result += 2 * (((i[0] - dest[0]) ** 2 + (i[1] - dest[1]) ** 2) ** 0.5)
        result += 2 * (((i[0] - robot[0]) ** 2 + (i[1] - robot[1]) ** 2) ** 0.5)
      else:
        result += ((i[0] - dest[0]) ** 2 + (i[1] - dest[1]) ** 2) ** 0.5
        result += ((i[0] - robot[0]) ** 2 + (i[1] - robot[1]) ** 2) ** 0.5

    return result

def fval_function(sN, weight):
#IMPLEMENT
    """
    Provide a custom formula for f-value computation for Anytime Weighted A star.
    Returns the fval of the state contained in the sNode.

    @param sNode sN: A search node (containing a SnowballState)
    @param float weight: Weight given by Anytime Weighted A star
    @rtype: float
    """
  
    #Many searches will explore nodes (or states) that are ordered by their f-value.
    #For UCS, the fvalue is the same as the gval of the state. For best-first search, the fvalue is the hval of the state.
    #You can use this function to create an alternate f-value for states; this must be a function of the state and the weight.
    #The function must return a numeric f-value.
    #The value will determine your state's position on the Frontier list during a 'custom' search.
    #You must initialize your search engine object as a 'custom' search engine if you supply a custom fval function.
    return sN.gval + weight * sN.hval 

def anytime_gbfs(initial_state, heur_fn, timebound = 5):
#IMPLEMENT
    '''Provides an implementation of anytime greedy best-first search, as described in the HW1 handout'''
    '''INPUT: a snowball state that represents the start state and a timebound (number of seconds)'''
    '''OUTPUT: A goal state (if a goal is found), else False'''
    
    se = SearchEngine('best_first', 'full')
    start_t = os.times()[0]
    se.init_search(initial_state, snowman_goal_state, heur_fn)
    result = se.search(timebound)
    final_result = False
    cost_bound = (float("inf"), float("inf"), float("inf"))
    current_t = os.times()[0]
    
    while current_t - start_t < timebound:
      if result == False:
        return final_result
      if result.gval <= cost_bound[0]:
        cost_bound = (result.gval, result.gval, result.gval)
        final_result = result
      current_t = os.times()[0]
      result = se.search(timebound - current_t + start_t, cost_bound)
      
    return final_result

def anytime_weighted_astar(initial_state, heur_fn, weight=1., timebound = 5):
#IMPLEMENT
    '''Provides an implementation of anytime weighted a-star, as described in the HW1 handout'''
    '''INPUT: a snowball state that represents the start state and a timebound (number of seconds)'''
    '''OUTPUT: A goal state (if a goal is found), else False'''
    se = SearchEngine('custom', 'full')
    wrapped_fval_function = (lambda sN : fval_function(sN, weight))
    start_t = os.times()[0]
    se.init_search(initial_state, snowman_goal_state, heur_fn, wrapped_fval_function)
    result = se.search(timebound)
    final_result = False
    cost_bound = (float("inf"), float("inf"), float("inf"))
    current_t = os.times()[0]
    
    while current_t - start_t < timebound:
      if result == False:
        return final_result
      if result.gval + heur_fn(result) <= cost_bound[2]:
        cost_bound = (result.gval, heur_fn(result), result.gval + heur_fn(result))
        final_result = result
      current_t = os.times()[0]
      result = se.search(timebound - current_t + start_t, cost_bound)
      
    return final_result    

if __name__ == "__main__":
  #TEST CODE
  solved = 0; unsolved = []; counter = 0; percent = 0; timebound = 2; #2 second time limit for each problem
  print("*************************************")  
  print("Running A-star")     

  for i in range(0, 10): #note that there are 20 problems in the set that has been provided.  We just run through 10 here for illustration.

    print("*************************************")  
    print("PROBLEM {}".format(i))
    
    s0 = PROBLEMS[i] #Problems will get harder as i gets bigger

    se = SearchEngine('astar', 'full')
    se.init_search(s0, goal_fn=snowman_goal_state, heur_fn=heur_simple)
    final = se.search(timebound)

    if final:
      final.print_path()
      solved += 1
    else:
      unsolved.append(i)    
    counter += 1

  if counter > 0:  
    percent = (solved/counter)*100

  print("*************************************")  
  print("{} of {} problems ({} %) solved in less than {} seconds.".format(solved, counter, percent, timebound))  
  print("Problems that remain unsolved in the set are Problems: {}".format(unsolved))      
  print("*************************************") 

  solved = 0; unsolved = []; counter = 0; percent = 0; timebound = 8; #8 second time limit 
  print("Running Anytime Weighted A-star")   

  for i in range(0, 10):
    print("*************************************")  
    print("PROBLEM {}".format(i))

    s0 = PROBLEMS[i] #Problems get harder as i gets bigger
    weight = 10 
    final = anytime_weighted_astar(s0, heur_fn=heur_simple, weight=weight, timebound=timebound)

    if final:
      final.print_path()   
      solved += 1 
    else:
      unsolved.append(i)
    counter += 1      

  if counter > 0:  
    percent = (solved/counter)*100   
      
  print("*************************************")  
  print("{} of {} problems ({} %) solved in less than {} seconds.".format(solved, counter, percent, timebound))  
  print("Problems that remain unsolved in the set are Problems: {}".format(unsolved))      
  print("*************************************") 


