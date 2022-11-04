class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        vector<int> returning;
        
        for (int i = 0; i < nums.size(); i++) {
            for (int j = 1; j < nums.size() and i != j; j++) {
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