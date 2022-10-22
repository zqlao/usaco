//#include<bits/stdc++.h>
#include <iostream>
#include <vector>
#include <queue>
#include <cstring>

#define inf 200604300
using namespace std;

vector<int>tu[300110];
int match[300100];
int v[1400010],vsz;
int d[300110],las[300110];
int a,b,fir[300110],sec[300110],jl[300110],gs;
bool vis[100100],hv[300100];
bool er[300110];
vector<int>hh[300110];

bool dfs(int x){
	for(int i=0;i<tu[x].size();i++){
		int p=tu[x][i];
		if(!vis[p]){
			vis[p]=true;
			if(!match[p]||dfs(match[p])){
				match[p]=x;
				return true;
			}
		}
	}
	return false;
}


int main(){
	cin >> a >> b;
    //scanf("%d%d",&a,&b);
	for(int i=1; i<=a; i++){
		//scanf("%d%d",&fir[i],&sec[i]);
        int f, s;
        cin >> f >> s;
        fir[i] = f, sec[i] = s;
		hh[fir[i]].push_back(i);
		tu[i].push_back(fir[i]),tu[i].push_back(sec[i]);
	}
	int gs=0;
	for(int i=1;i<=a;i++){
		memset(vis,0,sizeof(vis)),gs+=dfs(i);
	}
	queue<int>q;
	printf("%d\n",a-gs);
	for(int i=1;i<=b;i++){
		if(fir[match[i]]==i){
			hv[match[i]]=true;
			printf("%d\n",match[i]);
			q.push(i);
		}
		if(sec[match[i]]==i){
			er[match[i]]=true;
			hv[match[i]]=true;
		}
	}
	while(!q.empty()){
		int x=q.front();
		q.pop();
		for(int i=0;i<hh[x].size();i++){
			int p=hh[x][i];
			if(er[p]){
				printf("%d\n",p);
				er[p]=false;
				q.push(sec[p]);
			}
		}
	}
	for(int i=1;i<=a;i++){
		if(!hv[i]) printf("%d\n",i);
	}
	return 0;
}


