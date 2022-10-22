#include <iostream>
#include <string>
#include <vector>
#include <set>

using namespace std;


int main() {
    int n, h_tmp;

    cin >> n;
    int *h_arr = new int [n];

    for (int i=0; i<n; i++)
        cin >> h_arr[i];

    vector<int> h(h_arr, h_arr+n);
    long long ans = 0;

    vector<int> with_h(n+1);
    for (int i=0; i<n; i++) with_h[h[i]] = i+1;
    set<int> present;
	for (int cur_h = n; cur_h; --cur_h) {
		auto it = present.insert(with_h[cur_h]).first;
		if (next(it) != end(present)) 
            ans += *next(it)-*it+1;
	} // the cow at position with_h[cur_h] can throw to the next cow after it

    cout << ans;
}