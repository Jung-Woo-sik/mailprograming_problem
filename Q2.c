#include <stdio.h>

// Fibonacci sequence starts with 0 and 1 where each fibonacci number is a sum of two previous fibonacci numbers. Given an integer N, find the sum of all even fibonacci numbers.

int evenfibosum(int n){
	int sum = 0;
	int x = 1;
	int y = 2;

	while ( x <= n){
		if (x % 2 == 0 ){
			sum += x;
		}
		int z = x + y;
		x = y;
		y = z;
	}
	return sum;
}


int main(){
	printf("%d\n",evenfibosum(12));	
	return 0;
}
