/**
 * @param {number[]} nums
 * @param {number} target
 * @return {boolean}
 */
var search = function(nums, target) {
//     BATTLE PLAN
// 1) Understand the problem(DONE)
// 2) Figure out how to incorporate a solution(DONE)
// 3) Code/ test the solution(ONGOING)
    
// NOTES
// Binary search, split the array into two halves with a middle. Compare target value to middle.
// To see if the target exists in the left or right portion, compare the middle value.
// the left side of the array, values should be LESS than the middle.
// right side of the array, GREATER than the middle. The reason it's SORTED in ASCENDING ORDER.
// This was for the FIRST Rotated sorted array.
// The GOAL: Figure out where the target value is if it is in the LEFT or RIGHT side of the array
// 


// SOLUTION
//     STEP ONE: define pointers
      let leftPointer = 0;
    let rightPointer = nums.length - 1;
    
// STEP TWO:  Checking if the  pointers intersect and creating midPointer
    while (leftPointer <= rightPointer) {
        let midPointer = leftPointer + Math.floor((rightPointer - leftPointer) / 2);
// STEP THREE: checking if the target is FOUND.
        if (nums[midPointer] === target) {
            return true;
        }

        // Check if the left half is sorted
        if (nums[leftPointer] < nums[midPointer]) {
            // Check if the target is in the left half
            if (nums[leftPointer] <= target && target < nums[midPointer]) {
                // If yes, adjust the right pointer
                rightPointer = midPointer - 1;
            } else {
                // Otherwise, adjust the left pointer
                leftPointer = midPointer + 1;
            }
        } 
        // Check if the right half is sorted
        else if (nums[leftPointer] > nums[midPointer]) {
            // Check if the target is in the right half
            if (nums[midPointer] < target && target <= nums[rightPointer]) {
                // If yes, adjust the left pointer
                leftPointer = midPointer + 1;
            } else {
                // Otherwise, adjust the right pointer
                rightPointer = midPointer - 1;
            }
        } 
        // Handle the case where nums[leftPointer] === nums[midPointer]
        else {
            // Increment the left pointer
            leftPointer++;
        }
    }

    return false;
};