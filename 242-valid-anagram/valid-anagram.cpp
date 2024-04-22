class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) return false;

        int arr[26] = {0};
        int length = s.length();

        for (int i = 0; i < length; i++) {
            char letter = s[i] - 97;
            arr[letter] += 1;
        }

        for (int i = 0; i < length; i++) {
            char letter = t[i] - 97;
            if (arr[letter] == 0) return false;
            arr[letter] -= 1;
        }

        return true;
    }
};