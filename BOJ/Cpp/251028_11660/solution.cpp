#include <iostream>
#include <vector>

using namespace std;

int main(void) {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N, M, x;
    cin >> N >> M;

    vector<vector<int>> DP(N + 1, vector<int>(N + 1, 0));
    vector<vector<int>> Answer(N + 1, vector<int>(N + 1, 0));
    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= N; j++) {
            cin >> Answer[i][j];

            DP[i][j] = DP[i][j-1] + DP[i-1][j] - DP[i-1][j-1] + Answer[i][j];
        }
    }

    for (int i = 0; i < M; i++) {
        int x1, x2, y1, y2;
        cin >> x1 >> y1 >> x2 >> y2;

        int result = DP[x2][y2] - DP[x1-1][y2] - DP[x2][y1-1] + DP[x1-1][y1-1];

        cout << result << "\n";
    }

    return 0;
}