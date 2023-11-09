/**
 * @param {number} x
 * @param {number} n
 * @return {number}
 */
var myPow = function(x, n) {
  
// OLD APPROACH
// //   defining the base and exponent 
//     let base = x;
    
//     let exponent = n; 
    
// //  use Math library 
    
// let result = Math.pow(base, exponent);
    
// console.log(result);
    
// NEW APPROACH
    
// STEP ONE: Create a base case. if exponent is 0, return 1
    
  if(n === 0){
      return 1;
  }
    
// STEP TWO: If exponent is negative, invert x and negate the exponent
  if(n <0) {
      
      x = 1/x;
      
      n = -n;
  }
    
// STEP THREE: intialize the result and loop through the exponents
    // Initialize result to 1
    let result = 1;
    
 while(n >0) {
//      if the exponent is odd, multiply it by x
     if (n%2 ===1){
         result *=x;
     }
     
//     STEP FOUR: square x and divide the exponent by two
     x*=x;
     n = Math.floor(n/2);
     
 }
    
   
  return result; 
    
};