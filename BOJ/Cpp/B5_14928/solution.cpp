#include <iostream>
using namespace std;

int main() {
    string N;
    cin >> N;

    const int MOD = 20000303;
    long long remainder = 0;

    for (char c : N) {
        remainder = (remainder * 10 + (c - '0')) % MOD;
    }

    cout << remainder << "\n";
    return 0;
}