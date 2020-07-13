// Write a non static method called "show_excitement" where the string
// "I am super excited for this course!" is returned exactly
// 5 times, where each sentence is separated by a single space.
// Return the string with "return".
// You can only have the string once in your code.
// Don't just copy/paste it 5 times into a single variable!


public class PythonBasics {
    public String show_excitement() {
		String word = "I am super excited for this course!";
		String word1 = "";
		for(int i = 0; i < 5; i++){
			word1= word1+word+" ";
		
		}
		return word1;
    	// your code goes her
	}
	public static void main(String[] args) {
		
	}
}