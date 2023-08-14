/**
 * @param {Function} fn
 * @return {Array}
 */
// PLAN OF ATTACK
// 1) UNDERSTAND THE PROBLEM(DONE)
// 2) CODE OUT A SOLUTION(DONE, utilizing reducer method for arrays.)


// Define the groupBy method on the Array prototype
Array.prototype.groupBy = function(fn) {
    // Use the reduce method to accumulate values into a result object
    return this.reduce((res, item) => {
        // Apply the provided grouping function to get the key
        const key = fn(item);

        // Check if the key does not exist in the result object
        if (!res.hasOwnProperty(key)) {
            // If the key does not exist, initialize an empty array for it
            res[key] = [];
        }

        // Push the current item into the array associated with the key
        res[key].push(item);

        // Return the updated result object for the next iteration
        return res;
    }, {}); // Initialize the accumulator with an empty object
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */