#include<stdio.h>
int main(){
	int n , m;
	int i,j,k,l;
	int *record = 0;
	int *picture = 0;
	int max = 0 , temp = 0;
	
	scanf("%d %d",&n,&m);
	record = calloc( n*m , sizeof(int) );
	picture = calloc( n*m , sizeof(int) );
		
	for(i=0 ; i<n ; i++){
		for(j=0 ; j<m ; j++){
			scanf( "%d" , picture+i*m+j );
		}
	}
	
	max = 0;
	temp = 0;
	for(i=0 ; i<n ; i++){
		for(j=0 ; j<m ; j++){
			if(record[i*m+j] == 0){
				temp = func(picture , i , j , n , m , record);
				//printf("%d ",temp);
				if(max < temp){
					max = temp;
				}
			}
		}
	}
	printf("%d\n" , max);
	
	return 0;
}
int func(int *picture , int i , int j , int n , int m , int *record){
	int num=1;
	record[i*m+j] = 1;
	if( i>0 ){
		if( record[(i-1)*m+j] == 0 ){
			if( picture[i*m+j] == picture[(i-1)*m+j] ){
				num += func(picture , i-1 , j , n , m , record);
			}
		}
	}
	if( j>0 ){
		if( record[i*m+j-1] == 0 ){
			if( picture[i*m+j] == picture[i*m+j-1] ){
				num += func(picture , i , j-1 , n , m , record);
			}
		}
	}
	if( i<n-1 ){
		if( record[(i+1)*m+j] == 0 ){
			if( picture[i*m+j] == picture[(i+1)*m+j] ){
				num += func(picture , i+1 , j , n , m , record);
			}
		}
	}
	if( j<m-1 ){
		if( record[i*m+j+1] == 0 ){
			if( picture[i*m+j] == picture[i*m+j+1] ){
				num += func(picture , i , j+1 , n , m , record);
			}
		}
	}
	return num;
	
}