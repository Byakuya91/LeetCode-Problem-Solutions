/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
var strStr = function(haystack, needle) {
    
//     STEP ONE: Understand the problem(DONE)
// STEP TWO: code a solution  
    
// SOLUTION PROPOSAL:
// 1) Start a loop to iterate through each character of the haystack string.(DONE)
// 2)Within the loop, check if the current character matches the first character of the needle string(DONE)
// 3)If it matches, then check the subsequent characters to see if they match the remaining characters of the needle string(DONE)
// 4)If all characters of the needle string are found consecutively in the haystack, return the index at which the match starts.
// 5)If the loop completes without finding a match, return -1
    
    
// 

//     STEP ONE start a loop and iterate
    for (let i = 0; i < haystack.length; i++) {
    // Access the current character of the haystack string
    let currentChar = haystack[i];
    
    // Do something with the current character (e.g., compare it with the needle string)
    // console.log(currentChar);
//       STEP TWO: check if currentChar's first char matches needle's first char
         if(currentChar === needle[0]){
//             flag if the first chars of needle and haystack do match
              let charMatch = true;
             
             
//  loop through the remaining string 
           for(let j = 0; j <needle.length; j++){
                // Access the corresponding character from the haystack string
                let nextChar = haystack[i + j];
               
                // Access the corresponding character from the needle string
                let needleChar = needle[j];
              
               
//   checking if the characters do NOT MATCH
               if(nextChar !== needleChar) {
                    // Break out of the loop
                   charMatch = false;
                    break;
                   
               }
               
           }
        
             // If all characters match, return the index
            if (charMatch) {
                return i;
            }
             
             
         }
        
        
}

    
    // If the loop completes without finding a match, return -1
    return -1; 
    
};