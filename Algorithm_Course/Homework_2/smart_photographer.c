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
	int dfs_path; 
	int dfs_count;
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
		graph -> array_parent[i].dfs_path = 1;
		graph -> array_parent[i].dfs_count = 0;
		graph -> array_parent[i].visited = false;
	}

	return graph; 
} 

// create a edge by adjancy matrix using exsited graph
void addEdge(struct Graph* graph, int src, int dest){ 
	// Add an edge from src to dest. A new node is 
	// added to the adjacency list of src. The node 
	// is added at the begining 
	struct AdjListNode* newNode = newAdjListNode(dest); 
	newNode -> next = graph -> array_adj[src].head; 
	graph -> array_adj[src].head = newNode; 
	graph -> array_parent[src].dfs_count = graph -> array_parent[src].dfs_count + 1;
	// printf("DEST : %d",newNode->dest);
} 

// this is the dfs function to get current max path number
void dfs(struct Graph* graph, struct AdjListNode* next,int mother){ 
	
	//  if next is not null 
	while(next){

		// set current node as visit  
		int current_smaller_index = next -> dest;
		// printf("%d\n====================\n",current_parents_number);
		graph -> array_parent[mother].visited = true;
		
		// check if the smaller one that we didn't go through ( if not visited )
		if(graph -> array_parent[current_smaller_index].visited!=true){

			struct AdjListNode* smaller_one = graph -> array_adj[current_smaller_index].head;
			
			// run the dfs for its the grade that smaller than before
			dfs(graph,smaller_one,current_smaller_index) ;
		}

		// store the max of the paths  
		if(graph -> array_parent[mother].dfs_path <= graph -> array_parent[current_smaller_index].dfs_path + 1 ){
			graph -> array_parent[mother].dfs_path = graph -> array_parent[current_smaller_index].dfs_path + 1;
		}else{
			graph -> array_parent[mother].dfs_path = graph -> array_parent[mother].dfs_path;
		}	

		// to the next one
		next = next -> next;
	}
	
}

// function to fin max path
int find_max_path(struct Graph* graph, int total_num){

	// declare the variables
	int maximum = 0 ;

	// for loop to check each node
	for(int i=0;i<total_num;i++){
		struct AdjListNode* parents = graph -> array_adj[i].head; 

		// if not null, run dfs
		if(parents == NULL){
			graph -> array_parent[i].visited = true;
		}else{
			if(graph->array_parent[i].visited!=true){
				dfs(graph,parents,i);
			}
		}
	}   
    
	// compare and find the maximum of all self.dp[i]  
    for(int i=0;i<total_num;i++){
		if(graph->array_parent[i].dfs_path>=maximum){
			maximum = graph->array_parent[i].dfs_path;
		}
	}

    return maximum ;
        
}
int partition(int *all_students,int low,int high){ 

    // like the algrithm, we comare if the first 
    // number is bigger or smaller than the piviot
    // if current number is smaller, then
    // put the number to the front part
    // if bigger, don't move the number
    
    // this is the index number to make smaller element 
    // swtich to the front
    int i = ( low-1 ) ;

    // we set the piviot as the last element in array
    int pivot = *(all_students+high) ; 

	// declare replacement
	int rep_first = 0;
    int rep_second = 0;

    // compare numbers using for loop
    for(int j=low; j<=high-1 ; j++){
        
        // as we mentioned above,
        // compare the two number of the current one and the piviot
        if(*(all_students+j) <= pivot){ 
          
            i = i+1 ;

            rep_first = *(all_students+i) ; 
			*(all_students+i) = *(all_students+j) ; 
			*(all_students+j) = rep_first ; 
		}
	}

	// after seperate smaller part and bigger part
	// we move piviot to the middle
	rep_second = *(all_students+i+1) ; 
	*(all_students+i+1) = *(all_students+high) ; 
	*(all_students+high) = rep_second ; 

    // return the place that the piviot is
    return ( i+1 );
}

// Function to do Quick sort 
void quickSort(int *all_students,int low,int high){
	
	int piviot;

    if(low < high){ 
        
        // like teacher's slide, partition by the piviot
        piviot = partition(all_students, low, high) ;

        // Separately sort elements before 
        // piviot place's number and after piviot place's numbe
        quickSort(all_students, low, piviot-1)  ;
        quickSort(all_students, piviot+1, high)  ;
	}
}

// check status
int check_status(int *all_students,int x,int y,int m){

    //declare current status
    int status = 1;

    for(int i=0;i<m;i++){
        int current_a = *(all_students+x*m+i);
		int current_b = *(all_students+y*m+i);
		// printf("\ncurrent x : %d\n",current_a);
		// printf("current y : %d\n===========",current_b);
        if(status !=0 ){
            if(current_a < current_b){
                status = status*1;
			}else{
                status = status*0;
			}
		}else{
            break;
		}
	}

    return status;
}

// find adjancy matrix
int create_adjancy_table(int m, int n,int *all_students,int adjancy_table[n][n]){
	// declare status
	int status = 0;

	// create a n*n table
    for(int x=0;x<n;x++){
		for(int y=0;y<n;y++){

            if(x != y ){
				
				status = 0;
                // if status = 1, the elements in x are all smaller than another one
                // if status = 0, the elements in x are not all smaller than another one
                status = check_status(all_students,x,y,m);

                if(status == 1 ){
                    adjancy_table[x][y] = 1;
					// printf("Hi");
				}
			}
		}
	}

	return adjancy_table[n][n];
}

// main function to run
int main(){

	// declare some variables
	int n = 0 , m = 0 , maximum = 0;
	
	scanf("%d %d",&n,&m);
	// int *record = (int*) malloc(sizeof(int) * n*m);

	// use pointer to declare 2d array by using one pointer to create n*m array
	int *all_students = (int*) malloc(sizeof(int) * n*m);
	int per_col = m-1;

	// use memset to dynamic declare 2d array for adjancy table
	int adjancy_table[n][n];
	memset( adjancy_table, 0, n*n*sizeof(int) );

	// use memset to dynamic declare 2d array for edge
	int edge[n];
	memset( edge, 0, n*sizeof(int) );
	
	// enter  data
	for(int i=0 ; i<n*m ; i++){
		scanf("%d", all_students+i);
	}

	// seperate from input and results
	// printf("\n=========================\n");

	// quick sort for each grade's students
	for(int i=0 ; i<n ; i++){
		quickSort(all_students,i*m,i*m+m-1);
	}

	// for(int i=0;i<n;i++){
	// 	for(int j=0;j<m;j++){
	// 		printf("%d,",*(all_students+i*m+j));
	// 	}
	// 	printf("\n===============\n");
	// }

	// printf("=====================\n");

	// create adjancy table dynamically
	adjancy_table[n][n] = create_adjancy_table(m,n,all_students,adjancy_table);

	// print adjancy table for checking
	// for(int i=0;i<n;i++){
	// 	for(int j=0;j<n;j++){
	// 		printf("%d,",adjancy_table[i][j]);
	// 	}
	// }

	// seperate from input and results
	// printf("=========================");

	// create graph for each grade's student
	struct Graph* graph = createGraph(n); 

	// use adjancy_table to create graph
    for(int x=0;x<n;x++){
		for(int y=0;y<n;y++){
			if(adjancy_table[x][y] == 1){
				addEdge(graph, x, y); 
			}
		}
	} 

	// get the maximum value of longest path
	maximum = find_max_path(graph,n);

	// print maximum
	printf("\n%d",maximum);

	return 0;
}
