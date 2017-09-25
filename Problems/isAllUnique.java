/*
	Implement an algorithm to determine if a string has all unique characters. What if
	you can not use additional data structure.
*/

import java.util.Scanner;

class IsAllUnique {

	public static boolean isUniqueChars(String str) {	
		int checker = 0;			
		for (int i = 0; i < str.length(); ++i) {				
			int val = str.charAt(i) - 'a';
			int valPos = 1 << val; 	// example for character c i.e. 2, 1 will be shifted 2 times. (100)
			
			if ((checker & valPos) > 0)
				return false;
				
			checker = checker | valPos;		// adding new character.
		}
		return true;
	}

	public static boolean isUniqueChars2(String str) {
		boolean[] char_set = new boolean[256];
		for (int i=0; i<str.length();i++) {
			int val = str.charAt(i);
			
			if (char_set[val])	return false;
			
			char_set[val] = true;
		}
		return true;
	}

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		System.out.println("Enter a String");
		String str = input.next();

		if (isUniqueChars(str))
			System.out.println("String is unique");
		else
			System.out.println("String is not unique");
	}
}