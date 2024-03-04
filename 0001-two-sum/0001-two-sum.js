/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
//     Understand the problem(DONE)
// Figure out a solution 
// BRUTE FORCE: check EVERY combination of the target for each value in the list.
//   Solution: use a Hashmap to store values as keys, and indices as values.
//  Iterate through the array and check if the difference between the target value and the array value sums up to the target.  So if the target is 4, and 3 is the first value in the array. 4-3 = 1.  3+1 = 4. Yes, add that to the Hashmap.
    
//  
    
// STEP ONE: create a Hashmap with  val: indice 
    let prevMap = {} 
    
// STEP TWO: iterate through nums
  for(let i = 0; i < nums.length; i++){
//       define value  and diff
       let n = nums[i];
      let diff = target - n;
      
      
//  checking if values exist in prevMap     
if (prevMap.hasOwnProperty(diff)) {
            // Return the indices when a solution is found
            return [prevMap[diff], i];
        }
//         add the value inside the Map if it does not exist 
        prevMap[n] = i;      
      

  }
    
 // Return null if no solution is found
    return null;         
}; 