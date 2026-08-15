class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    threeSum(nums) {
        let result = []
        nums.sort((a, b) => a - b)

        for (let i = 0; i < nums.length; i ++){
            const pivot = nums[i]

            if (i > 0 && pivot === nums[i - 1]){
                continue
            }

            let l = i + 1
            let r = nums.length - 1


            while (l < r){
                if (nums[l] + nums[r] < -pivot){
                    l += 1
                } else if (nums[l] + nums[r] > -pivot){
                    r -= 1
                } else if (nums[l] + nums[r] === -pivot){
                    result.push([pivot, nums[l], nums[r]])
                    l += 1
                    while (l < nums.length && nums[l] === nums[l - 1]){
                        l += 1
                    }
                    r -= 1
                }
            }
        }


        return result
    }
}
