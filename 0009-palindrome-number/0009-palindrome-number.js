/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function (x) {
    
//     EDGE CASES

//   if X is negative ( not a palindrome )
  
  if (x < 0) {
    return false;
  }

// if X is less than ten ( always a palindrome )
  if (x < 10) {
    return true;
  }

//  if X has 0 at its last digit and X is not 0 itself ( not a palindrome ) e.g. 10, 130 whose reverse will be 01, 031 respectively
  if (x % 10 === 0 && x !== 0) {
    return false;
  }

//  Palindrone calculation
    
    
//    converting to string and creating two pointers at the start/ end of the string. 
  const str = String(x);
  let i = 0, j = str.length - 1;
    
    
// STRING CONVERSIOn
    
// looping with the pointers
  while (i < j) {
//       if the first and last digit are NOT the same, it's not a Palindrone.
    if (str[i] !== str[j]) {
      return false;
    }
// updating the pointers
    i++;
    j--;
  }
// if the loop exits, it is a palindrone. 
  return true;
};