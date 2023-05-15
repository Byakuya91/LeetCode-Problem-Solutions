/**
 * @param {Function} fn
 * @return {Function}
 */
var curry = function(fn) {
        // SOLUTION ONE: iterative
        let nums = [];

    return function curried(...args) {
          nums = [...nums,...args];
        
//          Checking if the arguments in a function are the same.
        if( fn.length === nums.length){
            
            const res =  fn(...nums);
            // CLEAN UP.
             nums = [];
            
            return res;
        } else{
            return curried; 
            
            
        }
//     

    };
};

/**
 * function sum(a, b) { return a + b; }
 * const csum = curry(sum);
 * csum(1)(2) // 3
 */
