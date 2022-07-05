#include <iostream>
using namespace std;

int main() {
    long long int i;
    cin >> i;

    while(true) {
        cout << i << " ";
        if(i == 1) break;
        if(i%2 == 0) i /= 2;
        else i = i*3+1;
    }
    cout << "\n";
    return 0;
}