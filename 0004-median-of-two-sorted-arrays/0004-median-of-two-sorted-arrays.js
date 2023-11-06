/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function(nums1, nums2) {
//     NOTES
// 1) Figure out a way to merge both arrays together and maintain how sorted they are
// 2) Figuring out the mediam, even lengh arrays you need to take the average of the middle element to find the median. ODD it's the middle element.
    
    
// ATTEMPTING THE PROBLEM

// STEP ONE: define an empty array to hold both arrays and pointers
   let merged_arr = [];
    
//    pointers
     let i = 0, j = 0;
    
// STEP TWO Combine the merged arrays while maintaining their sort
    while (i < nums1.length && j < nums2.length){
//  checking values of nums1 and nums2 before adding to merge_arr
    if(nums1[i] < nums2[j]){
          merged_arr.push(nums1[i]);
        i++;
         
        
    } else {
         merged_arr.push(nums2[j]);
        j++;
        
    }
        
    }
    
 // STEP THREE Append any remaining elements from nums1 and nums2
//     NOTE concat creates a new array.
    merged_arr = merged_arr.concat(nums1.slice(i), nums2.slice(j));
    
// STEP FOUR calculate the median
    
    const totalLen = merged_arr.length;
    
    
//     If the array is ODD length
    if (totalLen % 2 === 1) {
    return merged_arr[Math.floor(totalLen / 2)];
// EVEN length array
} else {
    const mid1 = totalLen / 2;
    const mid2 = mid1 - 1;
    return (merged_arr[mid1] + merged_arr[mid2]) / 2;
}
    
    
    
    
    
    
    
    
};