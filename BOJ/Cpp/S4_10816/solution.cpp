#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;
    vector<int> cards(N);
    for (int i = 0; i < N; ++i)
        cin >> cards[i];

    sort(cards.begin(), cards.end());

    int M;
    cin >> M;
    vector<int> targets(M);
    for (int i = 0; i < M; ++i)
        cin >> targets[i];

    for (int x : targets) {
        int cnt = upper_bound(cards.begin(), cards.end(), x)
                - lower_bound(cards.begin(), cards.end(), x);
        cout << cnt << ' ';
    }
}