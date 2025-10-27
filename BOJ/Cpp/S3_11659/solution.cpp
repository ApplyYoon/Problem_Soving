#include <iostream>
#include <vector>
using namespace std;

int main(void) {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M;
    cin >> N >> M;

    vector<int> prefix(N + 1, 0); // 인덱스 1부터 시작

    for (int i = 1; i <= N; i++) {
        int x;
        cin >> x;
        prefix[i] = prefix[i - 1] + x;
    }

    while (M--) {
        int i, j;
        cin >> i >> j;
        cout << prefix[j] - prefix[i - 1] << '\n';
    }

    return 0;
}