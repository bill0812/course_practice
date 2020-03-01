import numpy as np
import time

class Graph(): 
  
    def __init__(self, total_num): 

        # define some variables, 
        # like total number of array,
        # adjancy list of the elements that the current list connect to,
        # current max and final max
        self.total_num = total_num 
        self.adj = [[] for i in range(total_num)] 
        self.current_max = 1
        self.max = 1

        # Dp array  
        self.dp_path = [1] * (total_num)  

        # Visited array to know if the node  
        # has been visited previously or not  
        self.vis = [False] * (total_num) 

    # define edge and add to the list
    def add_edge(self, x, y): 
        
        self.adj[x].append(y) 

    # use recursive function to find the child of the child... of the child,
    # and find the maximum path
    def find_max_path(self,x,seen=None,path=None) :
        
        # Here are code for recursive code, but is not dynamic programming.
        # dynamic programming is more efficient than others
        ''' 
        count = self.childcount(self.adj[x])
        # print("current : ",x,"\n====")
        # print("It's childs : ",self.adj[x],"\n====")
        if count == 0 :
            if self.current_max > self.max :
                self.max = self.current_max
            # print("current max : ",self.current_max,"\n====")
            self.current_max = 1
        else :
            for i in (self.adj[x]) :
                self.current_max = self.current_max + 1
                self.find_max_path(i)
        if seen is None: seen = []
        if path is None: path = [x]
        seen.append(x)
        paths = []
        for current_node in self.adj[x]:
            if current_node not in seen:
                current_node_path = path + [current_node]
                paths.append(tuple(current_node_path))
                paths.extend(self.find_max_path(current_node, seen[:], current_node_path))
        '''

        # here use dynamic programming to record each node if they are visited, 
        # and also record the path maximun
        # ======================================================================
        # call dfs for every unvisited vertex  
        for i in range(0,self.total_num):   
            if not self.vis[i]:  
                self.dfs(i)  
        
        maximum = 0 
        
        # compare and find the maximum of all self.dp[i]  
        for i in range(0,self.total_num):   
            maximum = max(maximum, self.dp_path[i])  
        
        return maximum 

    # call dfs, deep-first search, which mentioned in class
    # here we use 'visit' and  'dp_path' to record information
    # avoid to do the same operation again, that's why dynamic program
    def dfs(self,current_node):  
   
        # set current node as visit  
        self.vis[current_node] = True 
        
        # traverse for all its children  
        for i in range(0, len(self.adj[current_node])):   
        
            # if not visited  
            if not self.vis[self.adj[current_node][i]]: 

                # run the dfs for its children
                self.dfs(self.adj[current_node][i])  
        
            # store the max of the paths  
            self.dp_path[current_node] = max(self.dp_path[current_node], 1 + self.dp_path[self.adj[current_node][i]]) 

def partition(arr,low,high): 

    # like the algrithm, we comare if the first 
    # number is bigger or smaller than the piviot
    # if current number is smaller, then
    # put the number to the front part
    # if bigger, don't move the number
    
    # this is the index number to make smaller element 
    # swtich to the front
    i = ( low-1 )  

    # we set the piviot as the last element in array
    pivot = arr[high]      
    
    # compare numbers using for loop
    for j in range(low , high): 
        
        # as we mentioned above,
        # compare the two number of the current one and the piviot
        if   arr[j] <= pivot: 
          
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
    
    # after seperate smaller part and bigger part
    # we move piviot to the middle
    arr[i+1],arr[high] = arr[high],arr[i+1] 

    # return the place that the piviot is
    return ( i+1 ) 
  
# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high: 
        
        # like teacher's slide, partition by the piviot
        piviot = partition(arr,low,high) 

        # Separately sort elements before 
        # piviot place's number and after piviot place's numbe
        quickSort(arr, low, piviot-1) 
        quickSort(arr, piviot+1, high) 

# sort each
def sort_each(arr_1,n_total) :

    # sort each line of students
    for i in range(n_total) :
        n = len(arr_1[i]) 
        quickSort(arr_1[i],0,n-1) 

    return arr_1

# find adjancy matrix
def create_adjancy_table(n_total,arr_1,adjancy_table) :

    # create a n*n table
    for x in range(n_total) :
        for y in range(n_total) :

            if x != y :
                # if status = 1, the elements in x are all smaller than another one
                # if status = 0, the elements in x are not all smaller than another one
                status = check_status(arr_1[x],arr_1[y])

                if status == 1 :
                    adjancy_table[x][y] = 1
    
    return adjancy_table

# check status
def check_status(array_x,array_y) :

    # declare current status
    status = 1

    for i in range(len(array_x)) :
        # print(array_x[i],array_y[i])
        if status !=0 :
            if array_x[i] <  array_y[i] :
                status = status*1
            else :
                status = status*0
        else :
            break

    # print("status : ",status)
    # print("=====================")

    return status
  
if __name__ == "__main__" :

    # input data
    input_data = input("input numbers and students numbers : ")
    input_data_each = list(map(int, input_data.split()))
    n_total = input_data_each[0]
    n_students = input_data_each[1]

    arr_1 = list()

    # print("Initialized Matrix : ")
    # print("=======================")
    
    for i in range(n_total) :

        each_height = input("input student's height : ")
        arr_1.append(list(map(int, each_height.split())))

        # print("Finish Enter " + str(i) + " row !")
        # print("=================================")

    # print("Start Processing :\n=================================")
    
    # create a dictionary to count in_node and out_node
    # adjancy_table = np.zeros((n_total,n_total))

    # use list instead of numpy
    adjancy_table = [[0 for col in range(n_total)] for row in range(n_total)]

    # quick sort find sorting list
    arr_1 = sort_each(arr_1,n_total)
    # print(arr_1)
    
    # find adjancy matrix
    adjancy_table = create_adjancy_table(n_total,arr_1,adjancy_table) 
    # print(adjancy_table)

    # create graph
    G = Graph(n_total)

    # use adjancy_table to create graph
    for x in range(n_total) :
        for y in range(n_total) :
            if adjancy_table[x][y] == 1 :
                G.add_edge(x,y)

    # use root to find max root
    current_max = 0
    root_choice = list()

    # count zero
    for x in range(n_total) :

        # count zero to get root
        count_zero = 0
        for y in range(n_total) :
            
            if adjancy_table[y][x] == 0 :
                count_zero = count_zero + 1

        # get the start root, and find max path
        if count_zero == n_total :
            root_choice.append(x)

    print("Adjancy table : ",G.adj)
                
    # go through each possible root
    max_len = 0
    for i in range(len(root_choice)) :
        max_len = G.find_max_path(root_choice[i])
        # if all_path :
        #     max_len = max(len(p) for p in all_path)
        if max_len > current_max :
            current_max = max_len

    # print result
    print("Maximum Grades is : ",current_max)
