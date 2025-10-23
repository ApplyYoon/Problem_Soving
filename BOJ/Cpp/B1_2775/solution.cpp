#include <iostream>

using namespace std;

int main(void) {
    int T, k, n;
    int arr[15][15] = {};

    for (int i = 1 ; i <= 14; i++) {
        arr[0][i] = i;
    }

    for (int i = 1; i <= 14; i++) {        
        for (int j = 1; j <= 14; j++) {    
            arr[i][j] = arr[i][j-1] + arr[i-1][j];
        }
    }

    cin >> T;
    for (; T > 0; T--) {
        cin >> k >> n;
        cout << arr[k][n] << endl;
    }
    return 0;
}