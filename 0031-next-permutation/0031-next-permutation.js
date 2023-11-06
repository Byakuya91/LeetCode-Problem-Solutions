/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var nextPermutation = function(nums) {
    
    
    
    
    // Find the first pair (i, i+1) where nums[i] < nums[i+1]
    let i = nums.length - 2;
    while (i >= 0 && nums[i] >= nums[i + 1]) {
        i--;
    }

    if (i >= 0) {
        // Find the smallest element in the right subarray that is greater than nums[i]
        let j = nums.length - 1;
        while (j > i && nums[j] <= nums[i]) {
            j--;
        }

        // Swap nums[i] and nums[j]
        [nums[i], nums[j]] = [nums[j], nums[i]];
    }

    // Reverse the right subarray to obtain the next lexicographically greater permutation
    reverse(nums, i + 1);
};

function reverse(nums, start) {
    let end = nums.length - 1;
    while (start < end) {
        [nums[start], nums[end]] = [nums[end], nums[start]];
        start++;
        end--;
    }
}

// Example usage
const nums = [1, 2, 3];
nextPermutation(nums);
console.log(nums);  // Output: [1, 3, 2]
