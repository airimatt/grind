class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        
        int i = 0;
        int j = numbers.size() - 1;
        int sum = 0;
        
        while (i < j) {
            sum = numbers.at(i) + numbers.at(j);
            if (sum == target) {
                return vector<int> {(i + 1), (j + 1)};
            } else if (sum < target) {
                i++;
            } else {
                j--;
            }
        }
        
        return vector<int> {1, 1};
    }
};