class Solution {
public:
    int search(vector<int>& nums, int target) {
        
        int start = 0;
        int middle = (nums.size() - 1) / 2;
        int end = nums.size() - 1;
        
        while (start <= end) {
            if (target == nums.at(middle)) {
                return middle;
             } else if (target < nums.at(middle)) {
                end = middle - 1;
            } else {
                start = middle + 1;
            }
            middle = end - ((end - start) / 2);
        }
        
        return -1;
        
    }
};