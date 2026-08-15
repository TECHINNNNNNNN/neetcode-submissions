class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        let tmpDict = {}

        for (let i = 0; i < nums.length; i ++){
            if (!Object.hasOwn(tmpDict, nums[i])){
                tmpDict[target - nums[i]] = i
            } else{
                return [tmpDict[nums[i]], i]
            }
        }
    }
}
