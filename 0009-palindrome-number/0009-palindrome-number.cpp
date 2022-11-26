class Solution {
public:
    bool isPalindrome(int x) {
        
        if (x < 0) {
            return false;
        }
        
        string num = "";
        
        while (x > 0) {
            num += to_string(x % 10);
            x /= 10;
        }
        
        int front = 0;
        int back = num.length() - 1;
        
        for (int i = 0; i < num.length() / 2; i++) {
            if (num.at(front) != num.at(back)) {
                return false;
            }
            front++;
            back--;
        }
        
        return true;
    }
};