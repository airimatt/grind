class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        
        string lcp = strs[0];
        
        for (int i = 1; i < strs.size(); i++) {
            if (lcp.length() == 0) {
                return "";
            }
            if (lcp.length() > strs[i].length()) {
                lcp = lcp.substr(0, strs[i].length());
            }
            for (int j = 0; j < strs[i].length(); j++) {
                if (strs[i][j] != lcp[j]) {
                    lcp = lcp.substr(0, j);
                }
            }
        }
        
        return lcp;
    }
};