class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> ans;

        if (strs.size() == 1) {
            vector<string> to_add;
            to_add.push_back(strs.at(0));
            ans.push_back(to_add);
            return ans;
        }

        unordered_map<string, vector<string>> mymap;

        int size = strs.size();
        for (int i = 0; i < size; i++) {
            string original = strs.at(i);
            string sorted = original;
            sort((&sorted)->begin(), (&sorted)->end());
            if (mymap.find(sorted) == mymap.end()) {
                vector<string> to_add;
                to_add.push_back(original);
                mymap.insert(make_pair(sorted, to_add));
            } else {
                mymap.at(sorted).push_back(original);
            }
        }

        for (auto i = mymap.begin(); i != mymap.end(); i++) {
            ans.push_back(i->second);
        }

        return ans;
    }
};