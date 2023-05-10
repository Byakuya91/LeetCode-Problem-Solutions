/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
//   intialize res
    
    let res = init
    
    
    
//     NEW SOLUTION
    nums.forEach((n) => {
        res = fn(res,n)
        
    
    
    });
    
    return res
    
    
    
//     ONE SOLUTION
//     create a result varliable 
        // let res  = init;

//     iterate through each number in the array
//     for(const n of nums){
// //         pass in the function
//         res = fn(res,n)
//     }
//     return res
    
    
    // return nums.reduce(fn,init)
    
    
};