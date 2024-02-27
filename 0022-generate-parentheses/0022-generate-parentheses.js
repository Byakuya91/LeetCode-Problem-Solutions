/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function(n) {
//     STEPS
//     1) Understanding the problem(DONE)
// 2) Understanding DFS(DONE)
// 3) Implement solution(ONGOING)
    
    
// STEP ONE: define an array to store the result
    const res = [];
    
//     STEP TWO: DFS function with three parameters: left parenthesis count, right parenthesis count AND string formed by parenthesis
    
    function dfs_parenthesis(left_p_count, right_p_count,s) {
//         SUB_STEP ONE: define BASE case
//          Base case: if the length of the string is equal to n * 2
        // it means we have formed a complete and valid combination
     if(s.length === n * 2){
//          push the valid combinations into the result
         res.push(s);
//         head back to the current branch of the recursion
         return; 
     }
        
// Adding an open "(" to the string
    if(left_p_count < n ){
        dfs_parenthesis(left_p_count +1, right_p_count,s +  '(')
    }
        
// Adding a closing ")" to the string
    if (right_p_count < left_p_count) {
            dfs_parenthesis(left_p_count, right_p_count + 1, s + ')');
        }
         
     

    }
    
// STEP THREE: run function
dfs_parenthesis(0,0, '');
return res;
    
    
};