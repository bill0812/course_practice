from heapq import *
class Graph(): 
  
    def __init__(self, total_num): 

        # define some variables, 
        # like total number of array,
        # adjancy list of the elements that the current list connect to,
        self.total_num = total_num
        self.adj = [[] for i in range(total_num)]
        self.in_node = [0 for i in range(total_num)]

    # define edge and add to the list
    def add_edge(self,start,end,station,time): 
        
        # create adjancy table for specific point "start", and add information 
        # like the next station, station (line) name, and during time
        self.adj[start].append([end,station,time])
        self.in_node[end] += 1

    def find_min_path(self,start,end) :
        
        # use this to stack the nodes one-by-one by the directed graph 
        # though its name is topological , but we dont use topological, instead we use stack to store its children
        self.history_stack = []
    
        # Visited array to know if the node  
        # has been visited previously or not  
        self.vis = [False] * self.total_num 

        # set up initial value for some variables, and set for every node
        distance = [float("Inf")] * self.total_num
        current_path_line = [[] for i in range(self.total_num)]
        check_list = [0] * self.total_num 
        if start < self.total_num :
            
            # set current distance of start node
            distance[start] = 0

            for i in range(len(self.adj[start])) :
                
                next_station = self.adj[start][i][0]
                spending_time = self.adj[start][i][2]
                current_line = self.adj[start][i][1]
                distance[next_station] = spending_time
                check_list[start] += 1
                heapify(self.history_stack)
                heappush(self.history_stack, (spending_time, current_line, next_station))
            
            while self.history_stack :
                
                # print(self.history_stack,"\n================")
                spending_time_prev, current_line_prev, next_station_prev = heappop(self.history_stack)
                # print(spending_time_prev, current_line_prev, next_station_prev,"hi")

                # check whether it's cycle
                check_list[next_station_prev] += 1

                if check_list[next_station_prev] <= self.in_node[next_station_prev] :
                    for i in range(len(self.adj[next_station_prev])) :
                        
                        # get current info
                        next_station = self.adj[next_station_prev][i][0]
                        spending_time = self.adj[next_station_prev][i][2]
                        current_line = self.adj[next_station_prev][i][1]

                        if spending_time_prev > distance[next_station] or spending_time > distance[next_station]:
                            pass
                        else :
                            added_time = 0
                            if check_list[next_station] <= self.in_node[next_station] :
                                # transfer from bus to bus
                                if current_line_prev.isdigit() and current_line.isdigit() and int(current_line_prev) != int(current_line) :
                                    added_time = spending_time_prev + spending_time + 5
                                    
                                # transfer from bus to train
                                elif current_line_prev.isdigit() and current_line.isalpha() :
                                    added_time = spending_time_prev + spending_time + 10

                                # transfer from train to bus
                                elif current_line_prev.isalpha() and current_line.isdigit() :
                                    added_time = spending_time_prev + spending_time + 5
                                    
                                # transfer from train to train
                                elif current_line_prev.isalpha() and current_line.isalpha()  and str(current_line_prev) != str(current_line) :
                                    added_time = spending_time_prev + spending_time + 10

                                # stay in same line
                                elif str(current_line_prev) == str(current_line) :
                                    added_time = spending_time_prev + spending_time
                                
                                # if current distance is bigger, then replace
                                if distance[next_station] > added_time :
                                    distance[next_station] = added_time
                                
                                # push history data to min heap tree
                                heapify(self.history_stack)
                                heappush(self.history_stack, (added_time, current_line, next_station))
        else :
            pass
            
        if end == start :
            print(0)
        elif end >= self.total_num and end != start :
            print(-1)
        elif distance[end] == float("inf") :
            distance[end] = -1
            print(distance[end])
        else :
            print(distance[end])
            
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
    
    for each in test_list :
        graph.find_min_path(each[0],each[1])