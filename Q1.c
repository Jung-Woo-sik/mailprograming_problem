#include <stdio.h>
#include <math.h>


#define MAX(X,Y) ((X) > (Y) ? (X) : (Y))
// Given an integer array, find the lagest consecutive sum of elements.

int solution(int arr[]){
	int sum = arr[0];
	int sum_current =arr[0];
	int i;
//	printf("%d\n",sizeof(arr)/sizeof(arr[0]));
	for (i=1 ; i <(int)sizeof(arr)/sizeof(arr[0]) ; i++){
		sum_current = MAX(sum_current + arr[i] , arr[i]);
		sum = MAX(sum_current, sum);
//		printf("%d\n",sum);
	}

	return sum;
}

int main(){
	int arr [] = {2,4,-2,-3,8};
//	printf("%d\n",sizeof(arr));
	printf("%d\n",solution(arr));
	return 0;
}
