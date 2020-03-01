"""
L 1 3
5 4 3
4 2 20
2 1 11
L A 2
4 3 5
3 2 4
L B 1
1 3 10
L 2 1
1 4 1
Q 4 1
E

L A 2
1 2 15
2 8 20
L B 1
1 3 20
L C 1
3 8 4
L 1 2
1 4 33
4 8 3
L 2 3
1 5 17
5 8 20
8 9 1
L 3 1
1 6 1
L 4 1
6 8 27
Q 1 8
Q 1 9
Q 8 9
Q 9 8
Q 9 9
E
"""
class Graph(): 
  
    def __init__(self, total_num): 

        # define some variables, 
        # like total number of array,
        # adjancy list of the elements that the current list connect to,
        self.total_num = total_num
        self.adj = [[] for i in range(total_num)]

    # define edge and add to the list
    def add_edge(self,start,end,station,time): 
        
        # create adjancy table for specific point "start", and add information 
        # like the next station, station (line) name, and during time
        self.adj[start].append([end,station,time])

    def find_min_path(self,start,end) :
        
        # use this to stack the nodes one-by-one by the directed graph 
        # though its name is topological , but we dont use topological, instead we use stack to store its children
        self.topological_sort_stack = []
        check_list = []
    
        # Visited array to know if the node  
        # has been visited previously or not  
        self.vis = [False] * self.total_num 

        # set up initial value for topological shortest path, and set for every node
        distance = [float("Inf")] * self.total_num 
        current_path_line = [[] for i in range(self.total_num)]
        in_degree = [[] for i in range(self.total_num)]
        check_list = [0] * self.total_num 

        if start < len(distance) :

            # set 0 distance for node "start"
            distance[start] = 0
            # in_degree[start] = [0]
            self.topological_sort_stack.append(start)
            # go through each item in topological_sort_stack
            while self.topological_sort_stack :
                
                # pop up the upest node
                current_node = self.topological_sort_stack.pop()            
                check_list[current_node] += 1
                # print(current_node)
                # print(self.topological_sort_stack,"\n===============")

                if current_node != end :
                    # go through each adjancy list node
                    for i in range(len(self.adj[current_node])) :

                        # initialize history value
                        history = 0
                    
                        # print(check_list[current_node],"!!",current_node)
                        if check_list[self.adj[current_node][i][0]] <= 2 :

                            # if current path is not none
                            if len(current_path_line[current_node]) != 0 :

                                # check in node bigger than one , go compare each history line
                                for in_node_each in in_degree[current_node] :
                                                    
                                    # transfer from bus to bus
                                    if in_node_each[0].isdigit() and self.adj[current_node][i][1].isdigit() and int(in_node_each[0]) != int(self.adj[current_node][i][1]) :
                                        history = int(self.adj[current_node][i][2]) + in_node_each[1] + 5
                                        if distance[self.adj[current_node][i][0]] >= int(self.adj[current_node][i][2]) + in_node_each[1] + 5 :
                                            distance[self.adj[current_node][i][0]] = int(self.adj[current_node][i][2]) + in_node_each[1] + 5  
                                            current_path_line[self.adj[current_node][i][0]] = list()
                                            current_path_line[self.adj[current_node][i][0]].append([distance[self.adj[current_node][i][0]],self.adj[current_node][i][1]])

                                    # transfer from bus to train
                                    elif in_node_each[0].isdigit() and self.adj[current_node][i][1].isalpha() :
                                        history = int(self.adj[current_node][i][2]) + in_node_each[1] + 10
                                        if distance[self.adj[current_node][i][0]] >= int(self.adj[current_node][i][2]) + in_node_each[1] +  10 :
                                            distance[self.adj[current_node][i][0]] = int(self.adj[current_node][i][2]) + in_node_each[1] + 10
                                            current_path_line[self.adj[current_node][i][0]] = list()
                                            current_path_line[self.adj[current_node][i][0]].append([distance[self.adj[current_node][i][0]],self.adj[current_node][i][1]])

                                    # transfer train bus to bus
                                    elif in_node_each[0].isalpha() and self.adj[current_node][i][1].isdigit() :
                                        history = int(self.adj[current_node][i][2]) + in_node_each[1] + 5
                                        if distance[self.adj[current_node][i][0]] >= int(self.adj[current_node][i][2]) + in_node_each[1] + 5 :
                                            distance[self.adj[current_node][i][0]] = int(self.adj[current_node][i][2]) + in_node_each[1] + 5
                                            current_path_line[self.adj[current_node][i][0]] = list()
                                            current_path_line[self.adj[current_node][i][0]].append([distance[self.adj[current_node][i][0]],self.adj[current_node][i][1]])

                                    # transfer from train to train
                                    elif in_node_each[0].isalpha() and self.adj[current_node][i][1].isalpha()  and str(in_node_each[0]) != str(self.adj[current_node][i][1]) :
                                        history = int(self.adj[current_node][i][2]) + in_node_each[1] + 10
                                        if distance[self.adj[current_node][i][0]] >= int(self.adj[current_node][i][2]) + in_node_each[1] + 10 :
                                            distance[self.adj[current_node][i][0]] = int(self.adj[current_node][i][2]) + in_node_each[1] + 10    
                                            current_path_line[self.adj[current_node][i][0]] = list()
                                            current_path_line[self.adj[current_node][i][0]].append([distance[self.adj[current_node][i][0]],self.adj[current_node][i][1]])
                                            
                                    # stay in same line
                                    elif str(in_node_each[0]) == str(self.adj[current_node][i][1]) :
                                        history = int(self.adj[current_node][i][2]) + in_node_each[1]
                                        if distance[self.adj[current_node][i][0]] >= int(self.adj[current_node][i][2]) + in_node_each[1] :
                                            distance[self.adj[current_node][i][0]] = int(self.adj[current_node][i][2]) + in_node_each[1]
                                            current_path_line[self.adj[current_node][i][0]] = list()
                                            current_path_line[self.adj[current_node][i][0]].append([distance[self.adj[current_node][i][0]],self.adj[current_node][i][1]])
                                
                                # record next child's in degree
                                # in_degree[current_node] = [[self.adj[current_node][i][1],history]]
                                in_degree[self.adj[current_node][i][0]].append([self.adj[current_node][i][1],history])
                                
                                if current_node != end :
                                    self.topological_sort_stack.append(self.adj[current_node][i][0])

                            # for first time record the path for the line we go through
                            else :

                                history = int(self.adj[current_node][i][2]) + distance[current_node]
                                if distance[self.adj[current_node][i][0]] >= int(self.adj[current_node][i][2]) + distance[current_node] :
                                    distance[self.adj[current_node][i][0]] = int(self.adj[current_node][i][2]) + distance[current_node]  
                                    current_path_line[self.adj[current_node][i][0]].append([distance[self.adj[current_node][i][0]],self.adj[current_node][i][1]])
                                
                                in_degree[self.adj[current_node][i][0]].append([self.adj[current_node][i][1],history])

                            
                                if current_node != end :
                                    self.topological_sort_stack.append(self.adj[current_node][i][0])
                        # # print(current_path_line)
                        # print("===================")

                else :
                    pass
                # print(self.topological_sort_stack)
            # print out the result
            if end >= len(distance) and end == start :
                print(0)
            elif end >= len(distance) and end != start :
                print(-1)
            elif distance[end] == float("inf") :
                distance[end] = -1
                print(distance[end])
            else :
                print(distance[end])
            #     print(current_path_line)
            # print("=============================")
        else :
            if end == start :
                print(0)
            else :
                print(-1)
        
            
# =======================================
if __name__ == "__main__" : 

    # declare some variables
    first_state, line_station, line_list, query_dict, query_list_start ,test_list = "L", list(), list(), dict(), list(), list()
    
    # input data till "E" comes up
    while(first_state != "E") :
        input_data = input()
        first_state = input_data.split(' ')[0]
        if first_state != "E"  and  first_state == "L" :
            station_name = input_data.split(' ')[1]
            for i in range(int(input_data.split(' ')[2])) :
                start, end, time = map(int, input().split(' '))
                line_station.append(start)
                line_station.append(end)
                line_list.append([station_name,start,end,time])
        elif first_state != "E"  and  first_state == "Q" :
            test_list.append([int(input_data.split(' ')[1])-1,int(input_data.split(' ')[2])-1])
            if int(input_data.split(' ')[1])-1 in query_list_start : 
                query_dict[int(input_data.split(' ')[1])-1].append(int(input_data.split(' ')[2])-1)
            else :
                query_dict[int(input_data.split(' ')[1])-1] = list()
                query_dict[int(input_data.split(' ')[1])-1].append(int(input_data.split(' ')[2])-1)
                query_list_start.append(int(input_data.split(' ')[1])-1)
        else :
            pass 
    
    # find count of the sattion and create graph
    all_station = max(line_station)
    graph = Graph(all_station)
    
    # add edge (adjancy list)
    for i in range(len(line_list)) :
        station, start, end, time = line_list[i][0], line_list[i][1], line_list[i][2], line_list[i][3]
        graph.add_edge(start-1,end-1,station,time)

    # for i in graph.adj :
    #     print(i)

    # print result
    # for start, end in query_dict.items() :
    #     print(start,end)
    #     graph.find_min_path(start,end)
        # print("=================== end ==============================")
    
    for each in test_list :
        graph.find_min_path(each[0],each[1])