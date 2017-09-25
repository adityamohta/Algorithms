/*
	Write code to reverse a C-Style String. 
	(C-String means that “abcd” is represented as
	five characters, including the null character.)
*/

#include <stdio.h>

void reverse(char *str) {
	char* end = str;
	char tmp;
	if (str) {
		// to traverse to last character in string.
		while (*end) {
			// printf("%p\n", end);
			++end;
		}
		--end;
		while (str < end) {
			tmp = *str;
			*str++ = *end;
			*end-- = tmp;
		}
	}
}

int main(){
	char str[10];
	printf("%s", "Enter string to reverse : ");
	scanf("%s", str);
	reverse(str);
	printf("%s\n", str);
	return 0;
}