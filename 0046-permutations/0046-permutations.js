/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permute = function(nums) {
//     PLAN OF ATTACK
    
    
    // STEP ONE: Define the result array to store permutations
    let permResult = [];
    
    //STEP TWO: Base case for recursion: if there's only one element, return it
    if (nums.length === 1) {
        return [nums.slice()]; // Return a copy of nums as a single-element array
    }
    
    // STEP THREE: Iterate through each value of nums using a for loop
    for (let i = 0; i < nums.length; i++) {
        // Remove the first value from nums and store it in the variable n
        let n = nums.shift();
        
        // STEP FOUR: Recursive call to permute with the modified nums (one less element since it was shifted)
        let perms = permute(nums.slice());
        
        //STEP FIVE: Iterate through remaining permutations and add the shifted value back to each permutation
        for (let perm of perms) {
            perm.push(n); // Add the shifted value back to the permutation
        }
        
        // STEP SIX: Concatenate the updated permutations to permResult
        permResult.push(...perms);
        
        //STEP SEVEN:  Add the shifted value back to nums for the next iteration of the loop
        nums.push(n);
    }
    
    // Return the final permResult containing all permutations
    return permResult;
};

// Example usage
// const nums = [1, 2, 3];
// const result = permute(nums);
// console.log(result); // Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
