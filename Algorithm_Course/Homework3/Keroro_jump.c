# include<stdio.h>
# include<stdlib.h>
# include<string.h>
# include<stdbool.h>

// declare AdjListNode and using pointer to delcare AdjListNode ( point to next )
struct AdjListNode{ 
    int dest; 
    struct AdjListNode* next; 
}; 

// declare Parent_node
struct Parent_node{
	int distance; 
	bool visited;
};

// declare AdjList
struct AdjList{ 
    struct AdjListNode *head;  
}; 

// declare struct graph and also the pointer AdjList and Parent_node
// which is using to create dynamic array
struct Graph{ 
    int total_num; 
    struct AdjList* array_adj; 
	struct Parent_node* array_parent; 
}; 

// declare struct dynamic new node list 
struct AdjListNode* newAdjListNode(int dest){ 
	struct AdjListNode* newNode = 
	(struct AdjListNode*) malloc(sizeof(struct AdjListNode)); 
	newNode -> dest = dest; 
	newNode -> next = NULL; 
	return newNode; 
} 

// create struct dynamic Grpah using struct "createGraph"
struct Graph* createGraph(int total_num){ 
	struct Graph* graph = (struct Graph*) malloc(sizeof(struct Graph)); 

	graph -> total_num = total_num; 
	graph -> array_adj = (struct AdjList*) malloc(total_num * sizeof(struct AdjList)); 
	graph -> array_parent = (struct Parent_node*) malloc(total_num * sizeof(struct Parent_node)); 

	for (int i=0; i < total_num; ++i){
		graph -> array_adj[i].head = NULL;
		graph -> array_parent[i].distance = 10000;
		graph -> array_parent[i].visited = false;
	}

	return graph; 
} 

// ======================================
// here below are for stack operation
// include check if the stack is full or empty
// push the item or pop the item

// create a struct with some variales
struct Stack{ 
    int top; 
    int stack_num; 
    int* array; 
}; 
// using createStack to new a Stack dynamiclly and alloc size for variables
struct Stack* createStack(int stack_num){ 
    struct Stack* stack = (struct Stack*) malloc(sizeof(struct Stack)); 
    stack->stack_num = stack_num; 
    stack->top = -1; 
    stack->array = (int*) malloc(stack->stack_num * sizeof(int)); 
    return stack; 
} 
// check the stack_full is empty
bool stack_full(struct Stack* stack){   
	return stack->top == stack->stack_num - 1;
} 
// check the stack is empty
bool stack_empty(struct Stack* stack){   
	return stack->top == -1;  
} 
// psuh the item to the front (bottom)
void push(struct Stack* stack, int item){ 
    if(!stack_full(stack)){
		stack->top = stack->top + 1;
		stack->array[stack->top] = item; 
	}
} 
// pop the upper item
int pop(struct Stack* stack){ 
    if(stack_empty(stack)){
		return -1; 
	}else{
		int top = stack->top ;
		stack->top = stack->top -1;
		return stack->array[top]; 
	}
} 
// ======================================
// here is for topological sorting
void topological_sorting(struct Graph* graph,struct AdjListNode* current_node,int mother,struct Stack* stack){

	// for loop to find the children's children's ..... , 
	// til the current dont have children or visited
	while(current_node){

		// set current node as visit  
		int current_smaller_index = current_node -> dest;
		// printf("%d\n====================\n",current_parents_number);
		graph -> array_parent[mother].visited = true;
		
		// check if the smaller one that we didn't go through ( if not visited )
		if(graph -> array_parent[current_smaller_index].visited!=true){

			struct AdjListNode* smaller_one = graph -> array_adj[current_smaller_index].head;
			
			// run the dfs for its the grade that smaller than before
			topological_sorting(graph,smaller_one,current_smaller_index,stack) ;

		}

		//add the current node to stack
		push(stack,mother);

		// to the next one
		current_node = current_node -> next;
	}
  
}

// main function which will call "topological_sorting" to sort the graph
// than find the mimimum path one-by-one
int find_shortest_path(struct Graph* graph, int total_num,int start,int end,struct Stack* stack){

	// for loop to check each node
	for(int i=0;i<total_num;i++){
		struct AdjListNode* parents = graph -> array_adj[i].head; 

		// if not null, run dfs
		if(parents == NULL){
			graph -> array_parent[i].visited = true;
		}else{
			if(graph->array_parent[i].visited!=true){
				topological_sorting(graph,parents,i,stack);
			}
		}
	}  

	// set start node as 0
    graph -> array_parent[start].distance = 0;

	// always find and get upper node to check 
	int up_node = pop(stack) ;

	// Process vertices in topological order 
	// go through each children ( adjancy table )
	while(up_node!=-1){
		struct AdjListNode* start_node = graph -> array_adj[up_node].head; 
		if(start_node != NULL){
			while(start_node){

				// get current children
				int item = start_node -> dest;

				// if the current children (next one) is bigger than self.distance[up_node] + 1
				// we than make current children smaller to that value
				if (graph -> array_parent[item].distance > graph -> array_parent[up_node].distance + 1){
					graph -> array_parent[item].distance = graph -> array_parent[up_node].distance + 1;
				} 
					
				start_node = start_node -> next;
			}
		}

		// always find and get upper node to check 
		up_node = pop(stack) ;

	}
  
	// if the answer is infinity, we refine the answer to at least "1" step
    if(graph -> array_parent[end].distance == 10000){
		graph -> array_parent[end].distance = 1 ;
	}

	// return minimum value
	return graph -> array_parent[end].distance;
}

// create a edge by adjancy matrix using exsited graph
void addEdge(struct Graph* graph, int src, int dest){ 
	// Add an edge from src to dest. A new node is 
	// added to the adjacency list of src. The node 
	// is added at the begining 
	struct AdjListNode* newNode = newAdjListNode(dest); 
	newNode -> next = graph -> array_adj[src].head; 
	graph -> array_adj[src].head = newNode; 
} 
// find adjancy matrix
int create_adjancy_table(int n,int *all_woods,int adjancy_table[n][n]){

	// create a n*n adjancy table
    for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			
			if (i != j){
				int current_i_back = *(all_woods+2*i+1);
				int current_j_front = *(all_woods+2*j+0);
				int current_j_back = *(all_woods+2*j+1);
				if((current_j_front < current_i_back) && (current_i_back < current_j_back)){
					adjancy_table[i][j] = 1;
				}    
			}
		}
	}       

	return adjancy_table[n][n];
}

// main function to run
int main(){

	// declare some variables
	int n = 0 , minimum = 0;
	
	scanf("%d",&n);
	// int *record = (int*) malloc(sizeof(int) * n*m);

	// use pointer to declare 2d array by using one pointer to create n*m array
	int *all_woods = (int*) malloc(sizeof(int) * n*2);

	// use memset to dynamic declare 2d array for adjancy table
	int adjancy_table[n][n];
	memset( adjancy_table, 0, n*n*sizeof(int) );
	
	// enter  data
	for(int i=0 ; i<n ; i++){
		scanf("%d %d", all_woods+i*2+0 , all_woods+i*2+1);
	}

	// create adjancy table dynamically
	adjancy_table[n][n] = create_adjancy_table(n,all_woods,adjancy_table);

	// create graph for each grade's student and create stack for topological sort
	struct Graph* graph = createGraph(n); 
	struct Stack* stack = createStack(20); 

	// use adjancy_table to create graph
    for(int x=0;x<n;x++){
		for(int y=0;y<n;y++){
			if(adjancy_table[x][y] == 1){
				addEdge(graph, x, y); 
			}
		}
	}

	// using graph to get minimum path and print
	int min_path = 0;
    min_path = find_shortest_path(graph,n,0,n-1,stack);

	printf("%d",min_path);

	return 0;
}
