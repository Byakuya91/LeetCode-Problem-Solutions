/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */

var search = function(nums, target) {
    
//     STEP ONE: Plan the problem
// 1) Understand the task
// 2) Understand Binary Search and how it works.
//     Checking if the MIDDLE element is the target value which is an index.
//3) Implemented it
    
    
// STEP TWO: Implementation
    
//     1) define left and right pointers for Binary Search.
    let left_point = 0;
    let right_point =  nums.length-1;
    
// 2) Finding the Middle index in the array
    while(left_point <= right_point){
//         Calculating the mid index
        let mid = Math.floor((left_point + right_point)/ 2);
        
//     If the target value equals the middle index
        if(nums[mid] === target){
            return mid; 
            
        }
        
// 3) Check if the left half is SORTED
     if(nums[left_point] <= nums[mid]){
//       check if the target is in the left half
         if(nums[left_point] <= target && target < nums[mid]){
//               decrement left pointer
             right_point = mid -1;
                        
         } else{
//              increment the left pointer. 
             left_point = mid+1;
             
         }
  } else{
      
      // 4) Check if the right half is SORTED 
       if (nums[mid] < target && target <= nums[right_point]) {
//     Update the pointers 
                left_point = mid + 1;
            } else {
                right_point = mid - 1;
            }
        
      
  }
        
        
           
        
    }
// Target is NOT found in the array.
   
return -1;
    
};