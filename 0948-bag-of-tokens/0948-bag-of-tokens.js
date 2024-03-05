/**
 * @param {number[]} tokens
 * @param {number} power
 * @return {number}
 */
var bagOfTokensScore = function(tokens, power) {
    // 1) Understand the problem(DONE)
    // 2) Visualize and code the solution(DONE)
    // 3) Sort the list and implement a greedy solution to gain the most power to obtain the most number of coins.
    
    // STEP ONE: Initialize res and score and sort the tokens
    let res = score = 0;
    tokens.sort((a, b) => a - b);
  
    // STEP TWO: Initialize pointers, left and right.
    let left = 0;
    let right = tokens.length - 1;


    // STEP THREE: Iterate through tokens list
    // The pointers have not crossed one another
    while (left <= right) {
        // Playing the max token face up
        if (power >= tokens[left]) {
            // Removing power from the score
            power -= tokens[left];
            // Update left pointer and score
            left++;
            score++;
            // Maximize the score
            res = Math.max(res, score);
        } else if (score > 0) {
            // Not enough power, play token with largest power
            power += tokens[right];
            // Update the pointers and score
            right--;
            score--;
        } else {
            // To avoid an infinite loop 
            break; 
        }
    }
    
    // Return max possible score
    return res;
};
