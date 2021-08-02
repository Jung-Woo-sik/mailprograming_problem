#include <stdio.h>

//Given an integer array, move all the 0s to the right of the array without changing the order of non-zero elements.

void swap(int arr[], int a, int b) {
	if (a == b) return;
	int temp = arr[a];
	arr[a] = arr[b];
	arr[b] = temp;
}

void solve(int input[]) {
	int position = 0;  
	for (int i = 0; i < 5; i++) { //array length 
		if (input[i] != 0) {
			swap(input, i, position);
			position++;
		}   
	}   
}


int main(){
	int  arr[] = {0,5,0,-1,3};
	int i;
	solve(arr);
	for (i=0; i<5 ; i++){
		printf("%d\t",arr[i]);
	}
	printf("\n");
	return 0;
}
