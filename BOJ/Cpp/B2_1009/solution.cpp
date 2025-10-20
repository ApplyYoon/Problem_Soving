#include <iostream>
#include <vector>

using namespace std;

int main(void) {
    int T, a, b;
    cin >> T;
    
    while (T--) {
        cin >> a >> b;

        a %= 10; 
        if (a == 0) {
            cout << 10 << endl;
            continue;
        }

        vector<int> pat;
        int curr = a;

        while (find(pat.begin(), pat.end(), curr) == pat.end()) {
            pat.push_back(curr);
            curr = (curr * a) % 10;
        }

        int idx = (b - 1) % pat.size();
        cout << pat[idx] << endl;
    }

    return 0;
}