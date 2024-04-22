class Solution {
public:
    int longestConsecutive(vector<int>& nums) {

        int size = nums.size();

        unordered_set<int> myset(nums.begin(), nums.end());

        int Max = 0;

        for (int i = 0; i < size; i++) {
            if (myset.find(nums[i] - 1) == myset.end()) {
                int tempMax = 1;
                while (myset.find(nums[i] + tempMax) != myset.end()) {
                    tempMax++;
                }
                Max = max(Max, tempMax);
            }
        }
        return Max;
    }
};