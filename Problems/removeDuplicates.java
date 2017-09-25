/*
	Design an algorithm and write code to remove the duplicate characters in a string
	without using any additional buffer. 
	NOTE: One or two additional variables are fine.
	An extra copy of the array is not.
	FOLLOW UP
	Write the test cases for this method.
*/
import java.util.Scanner;

class RemoveDuplicates {

	public static int removeDuplicates(char[] char_set) {
		if (char_set == null) return 0;
		int len = char_set.length;
		if (len < 2) return 1;
		int tail = 1;
		for (int i=1; i<len; i++) {
			int j;
			for (j=0; j<tail; j++){
				if (char_set[j] == char_set[i])	break;
			}
			if (j == tail) {
				char_set[tail++] = char_set[i];
			}
		}

		return tail;
	}

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);

		System.out.println("Enter a String");
		String str = input.next();

		char[] char_set = str.toCharArray();
		int end = removeDuplicates(char_set);

		for (int i=0; i<end; i++) {
			System.out.println(char_set[i]);
		}


	}
}