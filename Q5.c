#include <stdio.h>

// Given an integer array and integer N, find the Nth largest element in the array.
void swap(int arr[],int x ,int y);
int partition(int arr[],int first,int last);
int quickselect(int arr[],int first,int last, int k);
int quickselection(int arr[],int k);

void swap(int arr[], int x, int y) {
	int tmp = arr[x];
	arr[x] = arr[y];
	arr[y] = tmp;
}

int partition(int arr[], int first, int last) {
	int pivot_spot = first;
	for (int i = first; i < last; i++) {
		if (arr[i] > arr[last]) {
			swap(arr, i, pivot_spot);
			pivot_spot++;
		}
	}
	swap(arr, pivot_spot, last);
	return pivot_spot;
}

int quickselect(int arr[], int first, int last, int k) {
	if (first <= last) {
		int pivot = partition(arr, first, last);
		if (pivot == k) {
			return arr[k];
		}
		if (pivot > k) {
			return quickselect(arr, first, pivot - 1, k);
		}
		return quickselect(arr, pivot + 1, last, k);
	}
	return 0;
}
int quickselection(int arr[], int k) {
	return quickselect(arr, 0, 4, k - 1); //arr length 
}


int main(){
	int arr[] = {2,4,-2,-3,8};
	int num = 1;
//	printf("%d\n",sizeof(arr)/sizeof(arr[0]));	
	printf("%d\n",quickselection(arr,num));

	return 0;
}
