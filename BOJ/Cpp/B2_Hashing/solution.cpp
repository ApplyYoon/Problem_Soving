#include <iostream>

using namespace std;

int main(){
    const long long M=1234567891LL;
    int L; string s;

    cin>>L>>s;

    long long h=0,r=1;
    for(char c: s){
        long long a=c-'a'+1;
        h=(h+a*r)%M;
        r=r*31%M;
    }
    
    cout<<h<<"\n";
}