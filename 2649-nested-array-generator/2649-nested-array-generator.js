/**
 * @param {Array} arr
 * @return {Generator}
 */
var inorderTraversal = function*(arr) {
    
//     Checking if it is an array
    for (const n of arr){
        if (Array.isArray(n)){
//             recursive using a wildcard Yield * to make sure each of the arrays aren't skipped.
            yield* inorderTraversal(n);
            
            
            
        } else{
            yield n;
            
        }
    }
    
};

/**
 * const gen = inorderTraversal([1, [2, 3]]);
 * gen.next().value; // 1
 * gen.next().value; // 2
 * gen.next().value; // 3
 */