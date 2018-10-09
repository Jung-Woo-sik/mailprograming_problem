#include <stdio.h>

// Given an integer, check if it is a palindrome.

int IsPalindrome(int input) {
	if(input < 0 || (input % 10 == 0 && input != 0)) {
		return 0;
	}
	int revertedHalf = 0;
	while(input > revertedHalf) {
		revertedHalf = revertedHalf * 10 + input % 10;
		input /= 10;
	}
	return input == revertedHalf || input == revertedHalf/10;
}

int main(){
	if (IsPalindrome(12421)){
		printf("TRUE");
	}
	else{
		printf("FALSE");
	}

	return 0;
}
