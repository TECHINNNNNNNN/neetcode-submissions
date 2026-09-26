class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const bucket = new Map();
        for (let i = 0; i < nums.length; i ++){
            if (bucket.has(nums[i])){
                return [bucket.get(nums[i]),i]
            }
            bucket.set(target - nums[i], i)
        }
    
    }
}
