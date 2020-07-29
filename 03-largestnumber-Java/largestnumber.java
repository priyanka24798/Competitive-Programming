// # largestNumber: Write the function largestNumber(text) that takes a string of text and 
// # returns the largest int value that occurs within that text, or 0 if no such value occurs. 
// # You may assume that the only numbers in the text are non-negative integers and 
// # that numbers are always composed of consecutive digits (without commas, for example). For example:
// #     	largestNumber("I saw 3 dogs, 17 cats, and 14 cows!")
// # returns 17 (the int value 17, not the string "17"). And
// #     	largestNumber("One person ate two hot dogs!")
// # returns None (the value None, not the string "None").


class largestnumber {
	public int fun_largestnumber(String s){
		String[] lst = s.split(" ");
		int count = 0;
		for (int i = 0; i < lst.length; i++){
			try{
				if(Integer.parseInt(lst[i]) > count){
					count = Integer.parseInt(lst[i]);
				}
			}
			catch (Exception e){
				continue;
			}
			
			
		}
		
		return count;
	}		
	
	public static void main(String[] args){
		
	}
}
	