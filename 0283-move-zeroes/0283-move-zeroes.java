class Solution {
    public int[] moveZeroes(int[] nums) {
        int l = 0;
        int r = 0;
        int n = nums.length;

        while (r < n) {
            if (nums[l] == 0 && nums[r] != 0) {
                int tmp = nums[r];
                nums[r] = nums[l];
                nums[l] = tmp;
                l++;
            }
            if (nums[l] != 0) {
                l++;
            }
            r++;
        }

        return nums;
    }
}
