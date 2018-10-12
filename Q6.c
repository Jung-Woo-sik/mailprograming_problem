#include <stdio.h>

//Given an array of positive integers, find the smallest positive integer that cannot be created by adding elements in the array.

int solution(int num[]){
	int small = 1;
	int i;
	for (i = 0; i<4; i++){ //array length
		if (num[i] <= small){
			small = small +num[i];
		}
		else {
			return small;
		}
	}
}

int main(){
	int arr[] = {1,2,3,8};
	printf("%d\n",solution(arr));
	return 0;
}
