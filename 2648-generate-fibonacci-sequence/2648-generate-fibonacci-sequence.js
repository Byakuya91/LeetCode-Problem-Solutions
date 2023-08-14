/**
 * @return {Generator<number>}
 */
var fibGenerator = function*() {
//     PLAN OF ATTACK
//  UNDERSTAND THE PROBLEM(DONE)
// WRITE OUT THE SOLUTION
    
// STEP ONE: create the terms n1, n2
    let n1 = 0, n2 = 1;
    
//  ADDITIONAL STEP: while loop to traverse through list of numbers
while(true){
// //     OLD CODE
//     yield n1;
//     // STEP TWO: create a temp variable to store the numbers and update n2
//     let temp = n2;
//     n2 = n1+n2
    
// //  STEP THREE: reassign n1 to equal the temp(temp holds the OLD n2 variable)
    
//     n1 = temp 
    
// NEW CODE: deconstructing
    yield n1;
    [n1,n2] = [n2, n1+n2]
    
    
    
    
}
    
    
// NOTE THE LACK OF RETURN STATEMENT BECAUSE OF THE GENERATOR FUNC

    
};

/**
 * const gen = fibGenerator();
 * gen.next().value; // 0
 * gen.next().value; // 1
 */