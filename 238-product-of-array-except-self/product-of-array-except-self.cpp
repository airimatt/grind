class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {

        vector<int> res;
        res.push_back(1);

        int size = nums.size();
        for (int i = 0; i < size - 1; i++) {
            res.push_back(nums[i] * res[i]);
        }

        int post = 1;
        for (int i = size - 1; i >= 0; i--) {
            res[i] *= post;
            post *= nums[i]; 
        }

        return res;
    }
};