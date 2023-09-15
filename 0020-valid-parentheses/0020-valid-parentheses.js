/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    
    //Logic use stack push and pop method
    
//pseusodocode
    // Create a hashtable or object
    const hashTable = {
        '(':')',
        '{':'}',
        '[':']'    
    }
    // Initialize an empty stack
    
    let stack = []
    //Loop through an array
    if(s.length%2!==0)
        return false
    for(let i=0;i<s.length;i++)
    
   
        {
             //Push if the element is openning parentheses
            
     if(s[i]==='(' || s[i]=== '{' || s[i]==='[')
    {
        stack.push(s[i])
    }
          //if it is closing parenthesis pop 
           else if(s[i]===')' || s[i]=== '}' || s[i]===']')
            {
             //compare with the object or hashtable of itself
                let poped= hashTable[stack.pop()];
                if(poped !== s[i])
                    {
   
                        return false
                    }
                
                
            }
 
  
        }
    return !stack.length
 
    

    
};