class Graph(): 
  
    def __init__(self, total_num): 

        # define some variables, 
        # like total number of array,
        # adjancy list of the elements that the current list connect to,
        # current max and final max
        self.total_num = total_num 
        self.adj = [[] for i in range(total_num)] 

        # Visited array to know if the node  
        # has been visited previously or not  
        self.vis = [False] * total_num 

        # use this to stack the nodes one-by-one by the directed graph
        self.topological_sort_stack = []

        # set up initial value for topological shortest path, and set for every node
        self.distance = [float("Inf")] * total_num 

    # define edge and add to the list
    def add_edge(self,x,y): 

        self.adj[x].append(y)

    # A recursive function used by topological sorting 
    def topological_sorting(self,current_node): 
        
        # set up the current node as visited
        self.vis[current_node] = True

        # for loop to find the children's children's ..... , 
        # til the current dont have children or visited
        for item in self.adj[current_node] : 
            if self.vis[item] == False: 
                self.topological_sorting(item) 
  
        # add the current node to stack
        self.topological_sort_stack.append(current_node) 
    
    # main fucntion for finding short path 
    # return specific node's shortest path
    def find_shortest_path(self, start, end): 
        
        # using for loop to check all node and topological sorting from the "i" node
        # finishing "i" node, we then find if there is any node "i++" that isn't visited
        for i in range(self.total_num): 
            if self.vis[i] == False: 
                self.topological_sorting(start) 
        
        # set start node as 0
        self.distance[start] = 0
  
        # Process vertices in topological order 
        while self.topological_sort_stack : 
  
            # always find and get upper node to check 
            up_node = self.topological_sort_stack.pop() 
  
            # go through each children ( adjancy table )
            for item in self.adj[up_node]: 

                # if the current children (next one) is bigger than self.distance[up_node] + 1
                # we than make current children smaller to that value
                if (self.distance[item] > self.distance[up_node] + 1) : 
                    self.distance[item] = self.distance[up_node] + 1

        # if the answer is infinity, we refine the answer to at least "1" step
        if self.distance[end] == float("inf") :
            self.distance[end] = 1
        else :
            pass

        return self.distance[end]

# =====================================            
if __name__ == "__main__" :

    # input_woods = input("input numbers of woods : ")
    input_woods = input()
    all_woods = [[0]*2 for i in range(int(input_woods))]
    end_wood = 0
    
    # input each wood
    for i in range(int(input_woods)) :
        # input_wood = input("input start and end : ")
        input_wood = input()
        start = list(map(int, input_wood.split()))[0]
        end = list(map(int, input_wood.split()))[1]
        all_woods[i][0] = start
        all_woods[i][1] = end
    
    # create a adjancy table and record largest destination
    adjancy_table = [[0 for col in range(int(input_woods))] for row in range(int(input_woods))]

    for i in range(int(input_woods)) :
        if all_woods[i][1] > end_wood :
            end_wood = i

        for j in range(int(input_woods)) :
            if i != j :
                if (all_woods[j][0] < all_woods[i][1] < all_woods[j][1]) :
                    adjancy_table[i][j] = 1
            else :
                pass

    for i in range(int(input_woods)) :
        print(adjancy_table[i],"\n")

    # create graph
    G = Graph(int(input_woods))

    # use adjancy_table to create graph
    for x in range(int(input_woods)) :
        for y in range(int(input_woods)) :
            if adjancy_table[x][y] == 1 :
                G.add_edge(x,y)

    # for x in range(int(input_woods)) :
    #    print(adjancy_table[x])
        
    # using graph to get minimum path and print
    min_path = G.find_shortest_path(0,int(input_woods)-1)
    print(min_path)