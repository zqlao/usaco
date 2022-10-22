#include <iostream>
#include <map>
#include <vector>
#include <bits/stdc++.h>
#include <fstream>

using namespace std;

int main() {
    // ifstream fin("3.in");
    string s, t;
    cin >> s;
    cin >> t;
    // fin >> s;
    // fin >> t;

    int n;
    cin >> n;
    // fin >> n;
    string rlt;
    char yy = 'Y', nn = 'N';
    string allch = "abcdefghijklmnopqr";

    if (s!=t) {
        map<pair<char,char>, bool> eq;

        for (int i=0; i<allch.size(); i++) {
            for (int j=i+1; j<allch.size(); j++) {
                string sub_s;
                for (int k=0; k<s.size(); k++) 
                    if (s[k]==allch[i] || s[k]==allch[j])
                        sub_s += s[k];
                string sub_t;
                for (int k=0; k<t.size(); k++) 
                    if ((t[k]==allch[i]) || (t[k]==allch[j])) 
                        sub_t += t[k];
                eq[pair(allch[i], allch[j])] = sub_s==sub_t;
            }
        }

        for (int i=0; i<n; i++) {
            string query;
            cin >> query;
            // fin >> query;
            bool status=true;
            // if (i==51) {
                // cout << "stop" << endl;
            // }
            if (query.size()==1) {
                int n1 = count(s.begin(), s.end(), query[0]);
                int n2 = count(t.begin(), t.end(), query[0]);
                status = n1==n2;
            } else {
                for (int ii=0; ii<query.size(); ii++) {
                    for (int jj=ii+1; jj<query.size(); jj++) {
                        status = eq[pair(query[ii], query[jj])];
                        if (status==false) break; 
                    }
                    if (status==false) break;
                }
            }
            if (status==true) rlt += 'Y';
            else rlt += 'N';
        }

    } else {
        for (int i=0; i<n; i++)
            rlt += yy;
        cout << endl;
    }
    // cout << rlt << endl;
    cout << rlt;

    // string rlt_truth;
    // ifstream ftruth("2.out");
    // ftruth >> rlt_truth;
    // for (int i=0; i<rlt.size(); i++)
    //     if (rlt[i]!=rlt_truth[i]) cout << i << " ";
    // if (rlt==rlt_truth) cout << "equal" << endl;
    // else cout << "not equal" << endl;
    // return 0;
}