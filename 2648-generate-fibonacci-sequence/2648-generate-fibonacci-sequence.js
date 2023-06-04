/**
 * @return {Generator<number>}
 */
var fibGenerator = function*() {
//     create two variables to hold fibno numbers
    let n1 = 0, n2 = 1;
    
 while(true){
//      Using a yield to return a value in a generator function
      yield n1;
     [n1,n2] = [n2, n1+n2];
     
//      OLD CODE
    //  //  update the fibonnaci numbers with a temporary variable and n2 and n1
    // let temp = n2;
    // n2 = n1+n2
    // // Note, the temp is storing the OLD n2 value 
    // n1 = temp     
     
 }
    
    
};

/**
 * const gen = fibGenerator();
 * gen.next().value; // 0
 * gen.next().value; // 1
 */