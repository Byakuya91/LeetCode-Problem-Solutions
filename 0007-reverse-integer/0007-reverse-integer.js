/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
//    Create a flag for tracking negative number
    let isNegative = false;
    
//  checking if the number is negative
      if (x < 0) {
        isNegative = true;
        x = -x;
    }
    
// store the veryse number
let reverse = 0;
//     divide the number repeadtly by ten(mod divsion) until it hits zero.
    while (x > 0) {
        reverse = reverse * 10 + x % 10;
        x = parseInt(x / 10);
//     checking if the reverse power is greater than the range (−231, 231 − 1).
    }
    if (reverse >= Math.pow(2, 31) - 1 || reverse <= Math.pow(-2, 31)) {
        return 0;
    }
    return isNegative ? -reverse : reverse;
};
    
