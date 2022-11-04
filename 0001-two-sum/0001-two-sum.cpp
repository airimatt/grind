class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        vector<int> returning;
        
        for (int i = 0; i < nums.size() - 1; i++) {
            for (int j = i + 1; j < nums.size(); j++) {
                if (nums.at(i) + nums.at(j) == target) {
                        returning.push_back(i);
                        returning.push_back(j);
                        return returning;
                }
            }
        }
        
        return returning;
    }
};