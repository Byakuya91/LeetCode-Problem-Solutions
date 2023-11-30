/**
 * @param {number} x
 * @param {number} y
 * @param {number} bound
 * @return {number[]}
 */
/**
 * @param {number} x
 * @param {number} y
 * @param {number} bound
 * @return {number[]}
 */
var powerfulIntegers = function(x, y, bound) {
//     STEP ONE: create a new set
    let result = new Set();

    //STEP TWO Iterate through powers of x and y
    for (let i = 0; Math.pow(x, i) <= bound; i++) {
        for (let j = 0; Math.pow(y, j) <= bound; j++) {
            let powerfulInt = Math.pow(x, i) + Math.pow(y, j);

            //SUB-STEP 1: Check if it is less than or equal to the bound
            if (powerfulInt <= bound) {
                result.add(powerfulInt);
            } else {
                break; // No need to continue if exceeding the bound
            }

            // SUB-STEP TWO: If y is 1, further powers of y will not change the result
            if (y === 1) break;
        }

        // SUB-STEP THREE: If x is 1, further powers of x will not change the result
        if (x === 1) break;
    }
//    STEP THREE: convert SET to ARRAY.
    return Array.from(result);
};

// Example Usage:
// const result1 = powerfulIntegers(2, 3, 10);
// console.log(result1);  // Output: [2,3,4,5,7,9,10]

// const result2 = powerfulIntegers(3, 5, 15);
// console.log(result2);  // Output: [2,4,6,8,10,14]



