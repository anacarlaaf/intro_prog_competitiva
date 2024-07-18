#include <bits/stdc++.h>
using namespace std;
int main() {
    int n, x;
    cin >> n >> x;
    vector<long long int> a(n);


    for (int i=0; i<n; i++){
        cin >> a[i];
    }

    long long int qtd = 0;
    long long int soma = 0;
    unordered_map<long long int, long long int> ocos;
    ocos[0] = 1;

    for (int i=0; i<n; i++){
        soma += a[i];
        if (ocos.count(soma-x) >= 1 ) {
            qtd += ocos[soma-x];
        }
        ocos[soma]++;
    }
    cout << qtd << endl;
}