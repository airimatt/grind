class Solution {
public:
    bool isValid(string s) {
        
        stack<char> temp;
        
        for (unsigned int i = 0; i < s.length(); i++) {
            if (s.at(i) == '(' or s.at(i) == '{' or s.at(i) == '[') {
                temp.push(s.at(i));
            } else {
                if (! temp.empty()) {
                    if (s.at(i) == ')' and temp.top() == '(') {
                        temp.pop();
                    } else if (s.at(i) == '}' and temp.top() == '{') {
                        temp.pop();
                    } else if (s.at(i) == ']' and temp.top() == '[') {
                        temp.pop();
                    } else {
                        return false;
                    }
                } else {
                    return false;
                }
            }
        }
        
        if (temp.empty()) {
            return true;
        }
        return false;
    }
};