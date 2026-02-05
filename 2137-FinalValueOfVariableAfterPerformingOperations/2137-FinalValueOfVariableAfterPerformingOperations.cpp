// Last Updated: 2/5/2026, 9:21:51 AM
class Solution {
public:
    int finalValueAfterOperations(vector<string>& operations) {
        int result = 0 ; 
        for ( string opr : operations) result+=(opr[1] == '+' ? 1 : -1);
        return result;
    }
};