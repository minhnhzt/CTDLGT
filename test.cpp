#include <iostream>
using namespace std;

int main(){
    int n;
    cin >> n;
    int f[n];
    f[0] = 1;
    f[1] = 1;
    if (n < 2){
        cout << 1;
    }
    else{
        for(int i = 2; i < n; i++){
            f[i] = f[i-1] + f[i-2];
            cout << f[i] << " ";
        }
    }
}

