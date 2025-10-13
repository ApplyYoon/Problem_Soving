#include <iostream>

using namespace std;

int main(void) {
    string str;
    cin >> str;

    if (str == "NLCS") {
        cout << "North London Collegiate School\n";
    }
    else if (str == "BHA") {
        cout << "Branksome Hall Asia\n";
    }
    else if (str == "KIS") {
        cout << "Korea International School";
    }
    else if (str == "SJA") {
        cout << "St. Johnsbury Academy\n";
    }
    
    return 0;
}