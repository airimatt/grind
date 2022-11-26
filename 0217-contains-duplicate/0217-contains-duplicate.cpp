class Solution {
public:
    
    bool containsDuplicate(vector<int>& nums) {
        
        set<int> dup;                
        
        for (unsigned int i = 0; i < nums.size(); i++) {
            if (dup.find(nums.at(i)) == dup.end()) {
                dup.insert(nums.at(i));
            } else {
                return true;
            }
        }
        
        return false;
    }
};