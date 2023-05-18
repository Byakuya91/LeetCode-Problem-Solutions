
var TimeLimitedCache = function() {
    this.cache = new Map(); // Initialize the cache object
    
};

/** 
 * @param {number} key
 * @param {number} value
 * @param {number} time until expiration in ms
 * @return {boolean} if un-expired key already existed
 */
TimeLimitedCache.prototype.set = function(key, value, duration) {
//   grabbing the key within the hashmap
    const alreadyExists = this.cache.get(key);
    
    if(alreadyExists){
//         clear the timeout
        clearTimeout(alreadyExists.timeoutId);   
        
    }  
    
//     utilize setTimeOut
    const timeoutId = setTimeout(() => {
//         remove the key passed in
        this.cache.delete(key);         
        
    }, duration);
    //     Adding the key
       this.cache.set(key,{
         value,timeoutId
       });
    
    
    return Boolean(alreadyExists)
    
};

/** 
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function(key) {
//     grabbing the key that exists within the hashmap
    if(this.cache.has(key)){
        
        return this.cache.get(key).value 
    } else{
        return -1 
    }
    
};

/** 
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function() {
    return this.cache.size;
    
};

/**
 * Your TimeLimitedCache object will be instantiated and called as such:
 * var obj = new TimeLimitedCache()
 * obj.set(1, 42, 1000); // false
 * obj.get(1) // 42
 * obj.count() // 1
 */