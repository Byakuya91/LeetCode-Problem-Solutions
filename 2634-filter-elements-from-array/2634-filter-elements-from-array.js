/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
//  declarative SOLUTION 
    // arr.filter(fn)
    
//     imperative SOLUTION
    
//  create an empty array
    const res = [];
    
//     go through every result IN the array
    for(let i = 0; i < arr.length; i++){
        // conditional: check if a value exists and filter
          if(fn(arr[i],i)){
              res.push(arr[i]) ;
          }
           
           
           }
        
       return res;   
        
    };
        
