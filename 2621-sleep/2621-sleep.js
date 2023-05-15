/**
 * @param {number} millis
 */
async function sleep(millis) {
    
//     SOLUTION TWO: Async and Await
       await new Promise((resolve, reject) => {
           setTimeout(resolve, millis)
           
           
       })
    
    
    
    
    
    
    
    
    
    
    //     SOLUTION ONE: Callback 
    
    
    
//     // Callback function
    
//     function callback(resolve,reject){
//          setTimeout(resolve, millis);
//     }
    
    
    
    

//     return new Promise(callback)
    
    

    
    
    
    
    
}

/** 
 * let t = Date.now()
 * sleep(100).then(() => console.log(Date.now() - t)) // 100
 */