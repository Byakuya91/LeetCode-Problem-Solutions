/**
 * @param {number} n
 * @return {boolean}
 */
var isHappy = function(n) {
    //STEP ONE Define a helper function to calculate the sum of the squares of digits
    const getDigitSquareSum = (num) => {
    // Initialize a variable to store the sum
    let sum = 0;

    // Continue the loop as long as num is greater than 0
    while (num > 0) {
        // Extract the last digit of the number
        const digit = num % 10;

        // Add the square of the digit to the sum
        sum += digit * digit;

        // Remove the last digit from the number
        num = Math.floor(num / 10);
    }

    // Return the final sum of the squares of digits
    return sum;
};
//     STEP TWO: create a HashSet and monitor the set
    // Use a HashSet to detect cycles
    const seen = new Set();
//     if the number isn't one and is NOT in the set.
    while (n !== 1 && !seen.has(n)) {
        // Add the current number to the set
        seen.add(n);
        // Calculate the sum of the squares of digits
        n = getDigitSquareSum(n);
    }

    // If n is 1, it's a happy number; otherwise, it's not
    return n === 1;
};

// Example usage:
console.log(isHappy(19)); // Output: true
console.log(isHappy(2));  // Output: false
