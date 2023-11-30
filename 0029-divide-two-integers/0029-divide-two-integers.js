/**
 * @param {number} dividend
 * @param {number} divisor
 * @return {number}
 */
var divide = function(dividend, divisor) {
    // STEP ONE: Check for overflow case where dividend is -2^31 and divisor is -1
    if (dividend === -Math.pow(2, 31) && divisor === -1) {
        return Math.pow(2, 31) - 1;
    }

    //STEP TWO: Perform the division using Math.floor to truncate towards zero
    let result = Math.trunc(dividend / divisor);

    // STEP THREE: Return the result after type casting to int
    return result;
};
