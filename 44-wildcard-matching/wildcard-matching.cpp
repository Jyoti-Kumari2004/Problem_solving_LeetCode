class Solution {
public:
    bool isMatch(string s, string p) {
        int n = s.size();
        int m = p.size();

        vector<bool> prev(m + 1, false), curr(m + 1, false);

        // base case: empty string vs empty pattern
        prev[0] = true;

        // first row: empty string vs pattern
        for (int j = 1; j <= m; j++) {
            prev[j] = prev[j - 1] && p[j - 1] == '*';
        }

        for (int i = 1; i <= n; i++) {
            curr[0] = false;  // non-empty string can't match empty pattern

            for (int j = 1; j <= m; j++) {
                if (p[j - 1] == s[i - 1] || p[j - 1] == '?') {
                    curr[j] = prev[j - 1];
                } else if (p[j - 1] == '*') {
                    curr[j] = prev[j] || curr[j - 1];
                } else {
                    curr[j] = false;
                }
            }
            prev = curr;
        }

        return prev[m];
    }
};
