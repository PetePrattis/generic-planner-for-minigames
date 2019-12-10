# -*- coding: utf-8 -*-
import sys
import heapq, random
import string
import random   
import copy
import numpy as np


#same gia ola ta probs
class PriorityQueue:
    """
      Implements a priority queue data structure. Each inserted item
      has a priority associated with it and the client is usually interested
      in quick retrieval of the lowest-priority item in the queue. This
      data structure allows O(1) access to the lowest-priority item.
      Note that this PriorityQueue does not allow you to change the priority
      of an item.  However, you may insert the same item multiple times with
      different priorities.
    """
    def  __init__(self):
        self.heap = []
        self.count = 0

    def lenHeap(self):
        return len(self.heap)
    
    def push(self, item, priority):
        # FIXME: restored old behaviour to check against old results better
        # FIXED: restored to stable behaviour
        entry = (priority, self.count, item)
        # entry = (priority, item)
        heapq.heappush(self.heap, entry)
        self.count += 1

    def pop(self):
        (_, _, item) = heapq.heappop(self.heap)
        #  (_, item) = heapq.heappop(self.heap)
        return item

    def isEmpty(self):
        return len(self.heap) == 0
 
    def aStarSearch(node,heuristic=nullHeuristic):
        "Search the node that has the lowest combined cost and heuristic first."
        
        closed = []#set()
        #waterjug
        Q = PriorityQueue()
       
        iter=0
        #heuristic=0
    
    	#blocks world
        startNode = node#NodeBlocks(startSt)
        #startNode2 = copy.deepcopy(startNode)
        
        Q.push(startNode, startNode.pathCost())
        
        visited = 0
        while True:
            #print Q.lenHeap()
            if Q.isEmpty():
                print ('Solution is not possible, goal state is not achievable from given problem state.')
                return "sol not found"
            node = Q.pop()
            visited +=1
            #blocks world
            if node.goalTest():
                return "Solution found"
            iter+=1
            #closed.append(node.state)
                #print 'vimata pros tin lusi',len(closed)
                #return node.path
            if node.state not in closed:
                closed.append(node.state)
                for childNode in node.getSuccessors(heuristic):
                    Q.push(childNode, childNode.pathCost())

#-------------------------------Text menu in Python--------------------------------------
      
def print_menu():       ## Your menu design here
    print 30 * "-" , "MENU" , 30 * "-"
    print "1. Blocks World"
    print "2. Water Jug"
    print "3. 8 - Puzzle"
    print "4. Menu Option 4"
    print "5. Exit"
    print 67 * "-"
  
loop=True      
  
while loop:          ## While loop which will keep going until loop = False
    print_menu()    ## Displays menu
    choice = input("Enter your choice [1-5]: ")
     
    if choice==1:     
        print "Blocks World has been selected"
        
        #---------------------------------Blocks World------------------------------------------        


        stacks=int(input("Stacks: "))
        blocks=int(input("Blocks: "))
        while (stacks<0 or blocks<0):
            print ("Parakalw mono thetikous arithmous")
            stacks=input("Stacks: ")
            blocks=input("Blocks: ")

        def startState(stacks,blocks) : #ok
            l = stacks
            b = list(string.digits) #string.ascii_uppercase
            list_blocks = b[:blocks]
            random.shuffle(list_blocks)
            
            problem_state = []
            while blocks :
                if not list_blocks : break
            
                if stacks == 1 :
                    problem_state.append(list_blocks)
                    break
            
                else :
                    r = random.randint(1,blocks)
                    s = list_blocks[:r]
                    problem_state.append(s)
            
                blocks -= r
                stacks -= 1
                list_blocks = list_blocks[r:]
            
            while len(problem_state) < l :
                problem_state += [[]]
            
            random.shuffle(problem_state)
            return problem_state
        
        startSt = startState(stacks,blocks)
        
        def finalState(startSt) : #ok
            final = []
            for stack in startSt:
                final += stack
            final.sort()
            final = [final]
                
            for i in range(len(startSt)-1) :
                final += [[]]
            return final
        
        finalSt = finalState(startSt)
        
        def nullHeuristic(state):
                return 0
        
        class NodeBlocks :
            def __init__(self, elements,parent=None) :
                self.state = elements   #array of stacks, represents the current state like [['D'], ['C', 'A'], ['B', 'E']]
                self.parent = parent
                self.cost = 0
                if parent:
                    self.cost = parent.cost + 1 #depth
                print self.state
                #print self.parent
                #print self.cost
            
            def goalTest(self) :
                if self.state == finalSt :
                    print ("Solution Found!")
                    self.traceback()
                    return True
                else :
                    return False
            
            def heuristics(self) :
                not_on_stack_zero = len(finalSt[0]) - len(self.state[0])
            
                wrong_on_stack_zero = 0
                for i in range(len(self.state[0])) :
                    if self.state[0][i] != finalSt[0][i] :
                        wrong_on_stack_zero += 2
                
        
                dis_bw_pairs = 0
                for stack_iter in range(1, len(self.state)):
                    for val in range(len(self.state[stack_iter])-1):
                        if self.state[stack_iter][val] > self.state[stack_iter][val+1]:
                            dis_bw_pairs += 1
                return not_on_stack_zero + 4 * wrong_on_stack_zero - dis_bw_pairs
            
            def getSuccessors(self,heuristic) :
                children = []
                for i,stack in enumerate(self.state) :
                    for j, stack1 in enumerate(self.state) :
                        if i != j and len(stack1):
                            temp = copy.deepcopy(stack)
                            child = copy.deepcopy(self)
                            temp1 = copy.deepcopy(stack1)
                            temp.append(temp1[-1])
                            del temp1[-1]
                            child.state[i] = temp
                            child.state[j] = temp1
                            child.parent = copy.deepcopy(self)
                            children.append(child)
                return children
            
            def traceback(self):
                s, path_back = self, []
                while s:
                    path_back.append(s.state)
                    s = s.parent
                
                print ('Number of MOVES required : ', len(path_back))
                print ('-------------------------------------------------')
                
                print ("List of nodes forming the path from the root to the goal.")
                for i in list(reversed(path_back)) :
                    print (i)
            
            def pathCost(self) :
                return self.heuristics() + self.cost
            
            aStarSearch(NodeBlocks(startSt),0)

        
    elif choice==2:
        print "Water Jug has been selected"
        ## You can add your code or functions here
        
        data1=input("Litra/Galonia stin Kanata 1: ")
        data2=input("Litra/Galonia stin Kanata 2: ")
        while (data1<0 or data2<0):
            print ("Parakalw mono thetikous arithmous")
            data1=input("Litra/Galonia stin Kanata 1: ")
            data2=input("Litra/Galonia stin Kanata 2: ") 
        t = (data1,data2)#size of jugs
        
        def getSuccessorsWater((J1, J2)):  #epistrefei tin lista me tous diadoxous stin katastasi
                successors = [] # lista
                (C1, C2) = t #arxikes posotites
                #J1,J2 posotites tis parousas katastasis
                if(J1 < C1):  successors.append(((C1, J2),'Gemise tin kanata 1', 1)) # i dunates energeies, kinhseis
                if(J2 < C2):  successors.append(((J1, C2),'Gemise tin kanata 2', 1))
                if J1 > 0:    successors.append(((0, J2),'Adeiase tin kanata 1', 1))
                if J2 > 0:    successors.append(((J1, 0),'Adeiase tin kanata 2', 1))
                
                #print J1,J2
        
                if J1+J2 <= C1:#4
                    alpha=J1+J2
                    successors.append(((alpha,0),'Adeiase oli tin kanata 2 stin kanata 1',1))
                if J1+J2 <= C2: #3
                    alpha=J1+J2
                    successors.append(((0,alpha),'Adeiase oli tin kanata 1 stin kanata 2',1))
                if J1+J2 > C1:#4
                    alpha = J1+J2-C1
                    successors.append(((C1,alpha),'Gemise tin kanata 1 apo tin kanata 2',1))
                if J1+J2 > C2:#3
                    alpha = J1+J2-C2
                    successors.append(((alpha,C2),'Gemise tin kanata 2 apo tin kanata 1',1))
        
                return successors
         
        def waterHeurestic(state):
            return abs(state[0]-2)
        
        def nullHeuristic(state):
            return 0
            
        class NodeWater:
            def __init__(self, state, path, cost=0, heuristic=0):
                self.state = state
                self.path = path
                self.cost = cost
                self.heuristic = heuristic
                
            def getSuccessors(self, heuristicFunction=None):
                children = []
                for successor in getSuccessorsWater(self.state):
                    state = successor[0]
                    path = list(self.path)
                    path.append(successor[1])
                    cost = self.cost + successor[2]
                    if heuristicFunction:
                        heuristic = heuristicFunction(self.state)
                    else:
                        heuristic = 0
                    node = NodeWater(state, path, cost, heuristic)
                    children.append(node)
                return children
            def pathCost(self):
        		return self.cost + self.heuristic
            def goalTest(self): #testarei an vriskomaste stin katastasi stoxo i oxi
                if self.state[0] == 2:
                    print self.path
                    return True
                else:
                    return False
                #return self.state[0] == 2 #(2,y)
            
        aStarSearch(NodeWater((0,0),[],0,0),waterHeurestic)
    
    elif choice==3:
        print " 8 - Puzzle has been selected"
        ## You can add your code or functions here
    elif choice==4:
        print "Choice 4 has been selected"
        ## You can add your code or functions here
    elif choice==5:
        print "Exit has been selected"
        ## You can add your code or functions here
        loop=False # This will make the while loop to end as not value of loop is set to False
    else:
        # Any integer inputs other than values 1-5 we print an error message
        raw_input("Wrong option selection. Enter any key to try again..")


        


