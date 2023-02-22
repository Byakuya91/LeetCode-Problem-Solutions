class Solution {
    public int lengthOfLastWord(String s) {
        // POA
        // 1) Understand the Problem
        // 2) Come up with a unique solution that you DID NOT do in Python and before
        // 3) Test the solution
        
        // Solve the problem without removing white space.
        
        // PROPOSED solution: Using a flag and a length counter, increment from the LAST and use a flag to stop
        // when you encounter a space and returning the last length of the char(SUCCESS)
        
        // THING I needed to look up: 1) How to check if char is a letter and get the char index. 
        
        //THINGS I needed to improve on: Syntax, remember semicolons and curly braces, 
        
        // STEP ONE: create a counter to tally the length of the string and a flag
        
        int len = 0;
        
            
        boolean char_flag = false;
            
      // STEP TWO: iterate through the list 
            
        for(int i = s.length() -1; i >=0;i--){
            
            // STEP THREE: conditional checks to check each individual character and then utilize the flag to tally the length 
            if(Character.isLetter(s.charAt(i))) {
                // the first char from the string from the last string is encountered
                // set the flag to true
                char_flag = true ;
                len++;
                
                
            }
            
           else {
               
               // when the first space is encountered from the first space after the characters(from the last string)
               // return the length of the last word
               if (char_flag == true){
                   return len;
                   
               }
               
               
               
           }
           
        } 
        
     return len;     
    }
}