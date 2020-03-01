# include <stdio.h> 
# include <stdlib.h>

// use algorithm that teacher mentioned in class.
// use suffix max and global max to record current max sum
int findmax(int* input_array, int n) 
{ 
    int global_max = 0, suffix_max = 0;
    for (int i = 0 ; i < n; i++) { 
        if(suffix_max + *(input_array+i) > global_max){
            suffix_max = suffix_max + *(input_array+i);
            global_max = suffix_max;
        }else if(suffix_max + *(input_array+i) > 0){
            suffix_max = suffix_max + *(input_array+i);
        }else{
            suffix_max = 0;
        }
        
    } 
    return global_max; 
} 
  
/* Driver program to test maxCircularSum() */
int main() { 

    // malloc memory dynamicly and use pointer to read data
    int size = 100000;
    int number =0;
    int* input_array = (int*) malloc(sizeof(int) * size);

    // declare variable 'length' and for-loop variable 'i'
    // also declare one-way-maximum and circular-maximum
    int length = 0;
    int one_way_maximum = 0;
    int circular_maximum = 0;

    // sacnf number one by one.
    while(scanf("%d" , &number) != EOF){
        *(input_array + length) = number;
        length++;
    }
    
    one_way_maximum = findmax(input_array, length);

    // change original mind which is about non circular
    // Cuz its a kind of loop , so make it to an negative one
    // then we know the sum of all inputs
    // then we convert the original inputs to negative one
    // compute max sequence . Finally , we have to add it back to the sum.
    // which means that, if we map the negative input's max sequence to original one, the numbers
    // cause the original input's sum smaller. (minimize the original input)
    // so we have to add it back.
    int sum_array = 0;
    for(int i = 0 ; i < length ; i++){
        sum_array += *(input_array+i); 
        *(input_array+i) = -*(input_array+i);
    }

    // compare two maximum sum ( one-way and circlular )
    if((sum_array + findmax(input_array,length)) > one_way_maximum){
        printf("%d" , (sum_array + findmax(input_array,length)));
    }else{
        printf("%d" , one_way_maximum);
    }

    return 0; 
} 