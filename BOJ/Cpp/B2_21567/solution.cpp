#include <iostream>
#include <string>
using namespace std;

int main() {
    int a, b, c;
    cin >> a >> b >> c;

    long long product = 1LL * a * b * c;
    string s = to_string(product);

    int cnt[10] = {0};
    for (char ch : s)
        cnt[ch - '0']++;

    for (int i = 0; i < 10; i++)
        cout << cnt[i] << '\n';
}