# -*- coding: utf-8 -*-
import heapq, random
import string
import random   
import copy
import numpy as np


#same gia ola ta probs
'''προκειται για την υλοποιηση μιας λιστας προτεραιοτητας. οι προσφερομενες ενεργειες ειναι το μηκος της λιστας, η εισαγωγη στοιχειων,
η διαγραφη στοιχειων και ο ελεγχος αν ειναι κενη λιστα. χρησιμοποιουμε τη λιστα αυτη προκειμενου να λειτουργησει σωστα ο α*, δηλαδη συμφωνα με τα βηματα του'''
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
 
def nullHeuristic(state):#μηδενικος ευρετικος μηχανισμος
                return 0
 #ο α* αλγοριθμος. εφοσον τα προβληματα προκειται για προβληματα αναζητησης (λυσης) επιλεγουμε τον αλγοριθμο αυτο ο οποιος θα λειτουργησει ως generic planner
def aStarSearch(node,heuristic=nullHeuristic): #node = κατασταση που παιρνουμε στοιχεια της για να δουμε αν το προβλημα επιλυεται, heuristic = ευρετικος μηχανισμος
        "Search the node that has the lowest combined cost and heuristic first."
        
        closed = []
		
        Q = PriorityQueue() #λιστα προτεραιοτητας
       
        iter=0 #επαναληψεις μεχρι την επιλυση (ή αποτυχια ευρεσης επιλυσης)
        #heuristic=0
    
    	
        startNode = node#ο αρχικοσ κοβμος
        #startNode2 = copy.deepcopy(startNode)
        
        Q.push(startNode, startNode.pathCost())#εισαγουμε ως 1ο στοιχειο λιστας την αρχικη κατασταση μαζι με το κοστος της. για τον α* το κοστος καθε βηματος ισουται με το πραγματικο κοστος + το κοστος που προκυπτει απο ευρετικο μηχανισμο
        
        visited = 0#πληθος κομβων που εχουν προσπελαστει
        while True:
            #print Q.lenHeap()
            if Q.isEmpty(): #αν η λιστα ειναι αδεια τοτε ο α* δεν μπορει να βρει λυση και ειδοποιει τον χρηστη
                print ('Den mporei na vrethei lusi. H teliki katastasi den mporei na prossegistei me tin sugkekrimeni arxiki katastasi.')
                return "Solution not found"
            node = Q.pop() #παιρνουμε τον κοβμο προς εξεταση και αφου ολοκληρωσουμε τις ενεργειες που θελουμε να κανουμε με αυτο, το διαγραφουμε απο τη λιστα
            visited +=1 #ηδη εχουμε επισκεφτει εναν κομβο-κατασταση αφου καναμε pop()
			
            if node.goalTest(): #αν η συγκεκριμενη κατασταση αντιστοιχει στην τελικη, τοτε βρεθηκε λυση
                return "Solution found"
            iter+=1 #αυξανουμε την επαναληψη εφοσον δεν βρεθηκε ακομη λυση του προβληματος
            
            if node.state not in closed: #αν δεν εχουμε ηδη επισκεφτει την συγκεκριμενη κατασταση
                closed.append(node.state) #την προσθετουμε αφου τωρα την εχουμε επεξεργαστει
                for childNode in node.getSuccessors(heuristic): # για τους κομβους παιδια του συγκεκριμενου κομβου (δεδομενου ενος ευρετικου μηχανισμου)
                    Q.push(childNode, childNode.pathCost()) #προσθετουμε στη λιστα τους επομενους κομβους προς εξεταση με τα αντιστοιχα κοστη τους που οριζονται απο τον α*

#-------------------------------Text menu in Python--------------------------------------
      
def print_menu():       ## Your menu design here
    print 30 * "-" , "MENU" , 30 * "-"
    print "1. Blocks World"
    print "2. Water Jug"
    print "3. n - Puzzle"
    print "4. Exit"
    print 67 * "-"
  
loop=True      
  
while loop:          ## While loop which will keep going until loop = False
    print_menu()    ## Displays menu
    choice = input("Enter your choice [1-4]: ")
     
    if choice==1:     
        print "Blocks World has been selected"
        
        #---------------------------------Blocks World------------------------------------------        


        stacks=int(input("Stacks: "))
        blocks=int(input("Blocks: "))
        while (stacks<0 or blocks<0):
            print ("Parakalw mono thetikous arithmous")
            stacks=input("Stacks: ")
            blocks=input("Blocks: ")

        def startState(stacks,blocks) : #ορισμος της αρχικης καταστασης δεδομενου του πληθος κυβων και στοιβων
            l = stacks
            b = list(string.digits) #ολα τα ψηφια
            list_blocks = b[:blocks] #η λιστα με τους κυβους ειναι απο 0 εως οσους κυβους εχουμε επιλεξει στο προβλημα 
            random.shuffle(list_blocks)
            
            problem_state = []
            while blocks : 
                if not list_blocks : break  
            
                if stacks == 1 : #αν η στοιβα ειναι μια, κατευθειαν προσθεσε τους κυβους με τη σειρα που προεκυψαν προηγουμενως (τυχαια)
                    problem_state.append(list_blocks)
                    break
            
                else : #αν εχουμε παραπανω στοιβες, παλι τοποθετησε τυχαια τους κυβους μεσα
                    r = random.randint(1,blocks)
                    s = list_blocks[:r]
                    problem_state.append(s)
            
                blocks -= r
                stacks -= 1
                list_blocks = list_blocks[r:]
            
            while len(problem_state) < l :
                problem_state += [[]]
            
            random.shuffle(problem_state) #ανακατεψε τις θεσεις που βρισκονται οι κυβοι
            return problem_state
        
        startSt = startState(stacks,blocks)
        
        def finalState(startSt) : #η τελικη κατασταση ειναι οι κυβοι με την σειρα με τον μικροτερο να ειναι στο τραπεζι και τους υπολοιπους απο πανω
            final = []
            for stack in startSt:
                final += stack
            final.sort()
            final = [final]
                
            for i in range(len(startSt)-1) :
                final += [[]]
            return final
        
        finalSt = finalState(startSt)
        
        class NodeBlocks : #κλαση που διαχειριζεται τον καθε κομβο
            def __init__(self, elements,parent=None) :
                self.state = elements   #κατασταση του κομβου της μορφης [['D'], ['C', 'A'], ['B', 'E']]
                self.parent = parent #γονεας
                self.cost = 0 #κοστος αρχικο
                if parent:
                    self.cost = parent.cost + 1 #αν υπαρχει γονεας στο κοστος προσθεσε 1
                print self.state
            
            def goalTest(self) : #αν η κατασταση αντιστοιχει στην τελικη τοτε βρεθηκε λυση
                if self.state == finalSt :
                    print ("Vrethike lusi!")
                    self.traceback()
                    return True
                else :
                    return False
            
            def heuristics(self) : #ευρετικος μηχανισμος
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
            
            def getSuccessors(self,heuristic) : #παιδια κομβοι του κομβου προς εξεταση
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
            
            def traceback(self): # συναρτηση βοηθητικη για παρουσιαση των καταστασεων που οδηγησαν στην επιλυση του προβληματος
                s, path_back = self, []
                while s:
                    path_back.append(s.state)
                    s = s.parent
                
                print ('Xreiastikan vimata: ', len(path_back))
                print ('-------------------------------------------------')            
                print ("Lista me komvous pou synethesan to monopati apo tin arxiki katastash mexri tin epilusi, diladi tin teliki katastasi.")
                for i in list(reversed(path_back)) :
                    print (i)
            
            def pathCost(self) : #κοστος κομβου συμφωνα με τον α*
                return self.heuristics() + self.cost
            
        aStarSearch(NodeBlocks(startSt),0) #κομβος αρχικος. Δεν εχει ευρετικο μηχανισμο για την ευρεση κομβων παιδιων

        
    elif choice==2:
        print "Water Jug has been selected"
        #---------------------------------Water jug------------------------------------------  
        
        data1=input("Litra/Galonia stin Kanata 1: ")
        data2=input("Litra/Galonia stin Kanata 2: ")
        while (data1<0 or data2<0):
            print ("Parakalw mono thetikous arithmous")
            data1=input("Litra/Galonia stin Kanata 1: ")
            data2=input("Litra/Galonia stin Kanata 2: ") 
        t = (data1,data2)#ποσοτητα νερου στην καθε κανατα
        
        def getSuccessorsWater((J1, J2)):  #επιστρεφει λιστα με παιδια καταστασεις δεδομενου μιας αρχικης καταστασης
                successors = [] 
                (C1, C2) = t #αρχικες ποσοτητες
                #J1,J2 ποσοθητες της προς εξετασην καταστασης
				#δυνατες ενεργειες/κινησεις + κοστος =1
                if(J1 < C1):  successors.append(((C1, J2),'Gemise tin kanata 1', 1))
                if(J2 < C2):  successors.append(((J1, C2),'Gemise tin kanata 2', 1))
                if J1 > 0:    successors.append(((0, J2),'Adeiase tin kanata 1', 1))
                if J2 > 0:    successors.append(((J1, 0),'Adeiase tin kanata 2', 1))
                
        
                if J1+J2 <= C1:
                    alpha=J1+J2
                    successors.append(((alpha,0),'Adeiase oli tin kanata 2 stin kanata 1',1))
                if J1+J2 <= C2:
                    alpha=J1+J2
                    successors.append(((0,alpha),'Adeiase oli tin kanata 1 stin kanata 2',1))
                if J1+J2 > C1:
                    alpha = J1+J2-C1
                    successors.append(((C1,alpha),'Gemise tin kanata 1 apo tin kanata 2',1))
                if J1+J2 > C2:
                    alpha = J1+J2-C2
                    successors.append(((alpha,C2),'Gemise tin kanata 2 apo tin kanata 1',1))
        
                return successors
         
        def waterHeurestic(state): #ευρετικος μηχανισμος
            return abs(state[0]-2)
            
        class NodeWater:
            def __init__(self, state, moves, path, cost=0, heuristic=0):
                self.state = state #κατασταση
                self.moves = moves #μονοπατι επιλυσης
                self.path = path #μονοπατι επιλυσης
                self.cost = cost #κοστος
                self.heuristic = heuristic #ευρετικος μηχανισμος

            def getSuccessors(self, heuristicFunction=None): #για καθε ενδιαμεση κατασταση επεστρεψε τα παιδια καταστασεις
                children = []
                for successor in getSuccessorsWater(self.state):
                    state = successor[0]
                    path = list(self.path)
                    moves = list(self.moves)
                    moves.append(successor[1])
                    path.append(successor[0])
                    cost = self.cost + successor[2]
                    if heuristicFunction:
                        heuristic = heuristicFunction(self.state)
                    else:
                        heuristic = 0
                    node = NodeWater(state, moves, path, cost, heuristic)
                    children.append(node)
                return children
				
            def pathCost(self): #κοστος κομβου
        		return self.cost + self.heuristic
            def goalTest(self): #ελεγχος αν η κατασταση αντιστοιχει στην τελικη 
                if self.state[0] == 2: #(2,y)
                    print
                    print "Bimata gia tin lusi"
                    for n1,n2 in zip(self.path,self.moves):
                        print n2,":",n1, "L"

                    return True
                else:
                    return False
            
        aStarSearch(NodeWater((0,0),[],[],0,0),waterHeurestic) #αρχικη κατασταση (0,0) (ποσοτητες), μηδενικο κοστος, ευρετικος μηχανισμος και κενο μονοπατι
    
    elif choice==3:
        print " n - Puzzle has been selected"
         #---------------------------------n - Puzzle------------------------------------------ 
        size=int(input("Grammes / Stiles: "))
        while (size<0):
            print ("Parakalw mono thetikous arithmous")
            size=int(input("Grammes / Stiles: "))
            
        def getvalues(self, key): #elegxei tis kiniseis
            """Utility function to gather the Free Motions at various key positions in the Matrix."""
    
            values = [1, -1, self.nsize, -self.nsize] #1,-1,3,-3
            valid = []
            for x in values:
                if 0 <= key + x < self.tsize:
                    if x == 1 and key in range(self.nsize - 1, self.tsize, 
                            self.nsize):
                        continue
                    if x == -1 and key in range(0, self.tsize, self.nsize):
                        continue
                    valid.append(x)
            return valid
  
        def getSuccessorsPuzzle(self, st):  #epistrefei tin lista me tous diadoxous stin katastasi
            """Provide the list of next possible states from current state."""
    
            pexpands = {}
            for key in range(self.tsize):
                pexpands[key] = getvalues(self, key)
            pos = st.index(0)
            moves = pexpands[pos]
            expstates = []
            for mv in moves:
                nstate = st[:]
                (nstate[pos + mv], nstate[pos]) = (nstate[pos], nstate[pos + 
                        mv])
                expstates.append(nstate)
            #print expstates
            return expstates
    
        def printst(st):
            """Print the list in a Matrix Format."""
            state = NodePuzzle(size,0,0,0,0)
            for (index, value) in enumerate(st):
                print ' %s ' % value, 
                if index in [x for x in range(state.nsize - 1, state.tsize, 
                             state.nsize)]:
                    print 
            print 
        
        def puzzleHeurestic(st):
            """Calculate the Manhattan Distances of the particular State.
               Manhattan distances are calculated as Total number of Horizontal and Vertical moves required by the values in the current state to reach their position in the Goal State.
            """
    
            mdist = 0
            for node in st:
                if node != 0:
                    state = NodePuzzle(size,0,0,0,0) #poses grammes na ehei to puzzle
                    gdist = abs(state.goal.index(node) - st.index(node))
                    (jumps, steps) = (gdist // state.nsize, gdist % state.nsize)
                    mdist += jumps + steps
            return mdist
        
        class NodePuzzle:
            def __init__(self, nsize, state, goal, path, cost=0, heuristic=0):
                self.state = state
                self.path = path
                self.cost = cost
                self.heuristic = heuristic
                self.nsize = nsize
                self.tsize = pow(self.nsize, 2)
                self.goal = range(1, self.tsize)
                self.goal.append(0)
                
                
         
            def getSuccessors(self, heuristicFunction=None):
                children = []
                for successor in getSuccessorsPuzzle(self, self.state):
                    state = successor
                    path = list(self.path)
                    #path.append(successor[1])
                    path.append(state)
                    cost = self.cost + 1#+ successor[2]
                    if heuristicFunction:
                        heuristic = heuristicFunction(self.state)
                    else:
                        heuristic = 0
                    node = NodePuzzle(self.nsize, state, self.goal, path, cost, heuristic)
                    children.append(node)
                return children
            
            def start_state(self, seed=1000):
                """Determine the Start State of the Problem."""
        
                start_st = (self.goal)[:]
                for sts in range(seed):
                    start_st = self.one_of_poss(start_st)
                return start_st
            
            def pathCost(self):
        		return self.cost + puzzleHeurestic(self.state)
            
            def goalTest(self): #testarei an vriskomaste stin katastasi stoxo i oxi
                if self.state == self.goal:
                    for n in self.path:
                        printst(n)
                    return True
                else:
                    return False
                return self.state == self.goal 
            
            def one_of_poss(self, st): #dialegei tyxaia 
                """Choose one of the possible states."""
                exp_sts = getSuccessorsPuzzle(self,st)
                rand_st = random.choice(exp_sts)
                return rand_st 
            
        state = NodePuzzle(size,0,0,0,0)
        print 'The Starting State is:'
        start = state.start_state(50) #poses fores tha anakateytei i lusi
        printst(start)
        print 'The Goal State should be:'
        printst(state.goal)
        print 'The Steps to solution are:'
        aStarSearch(NodePuzzle(size,start,state.goal,[],0,0),puzzleHeurestic)

    elif choice==4:
        print "Exit has been selected"
        loop=False
        
    else:
        # Any integer inputs other than values 1-4 we print an error message
        raw_input("Parakalw epilekste metaksu 1-4...")


        


