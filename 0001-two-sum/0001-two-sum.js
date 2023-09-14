/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let hashTable = {};
    
    for(let i=0;i<nums.length;i++){
        doesItGiveTarget = target - nums[i];
        if(hashTable[doesItGiveTarget] !== undefined)
            {
                return [hashTable[doesItGiveTarget],i]
            }
        hashTable[nums[i]]=i
    }
    return []
};
