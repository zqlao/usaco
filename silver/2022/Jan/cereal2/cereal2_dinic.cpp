//#include<bits/stdc++.h>
#include <vector>
#include <queue>
#include <iostream>

#define inf 200604300
using namespace std;

struct node{
	int p, vid, w;
};

vector<node> tu[300110];
int v[1400010], vsz;
int dis[300110], las[300110];
int a, b, fir[300110], sec[300110], jl[300110], gs;
int p_beg, p_end;
bool vis[300110], in[300100], ty[300100];
bool er[300110];
vector<int> hh[300110];

void add(int x, int y, int V, int W){
	tu[x].push_back({y, vsz, W}), v[vsz] = V, vsz++;
	tu[y].push_back({x, vsz, -W}),v[vsz] = 0, vsz++;
}


bool get_dis(){
	for(int i=p_beg; i<=p_end; i++) ty[i]=in[i]=las[i]=0, dis[i]=-0x3f3f3f3f;
	queue<int>q;
	q.push(p_beg); dis[p_beg]=0;
	while(!q.empty()){
		int x=q.front();
		in[x]=false;
		q.pop();
		for(int i=0; i<tu[x].size(); i++){
			int p=tu[x][i].p, vid=tu[x][i].vid, w=tu[x][i].w;
			if(!v[vid]) continue;
			if(dis[p] < dis[x]+w){
				dis[p] = dis[x]+w;
				if(!in[p]) q.push(p), in[p]=true;
			}
		}
	}
	return dis[p_end]>-inf/10;
}


int dinic(int x, int flow){
	if(x==p_end) return flow;
	int res = flow;
	ty[x] = true;
	for(int i=0; i<tu[x].size(); i++){
		las[x] = i;
		int p = tu[x][i].p, vid = tu[x][i].vid, w = tu[x][i].w;
		if(!v[vid] || dis[p] != dis[x]+w || ty[p]) continue;
		int now = dinic(p, min(res, v[vid]));
		v[vid] -= now, v[vid^1] += now;
		res -= now;
		if (!res) break;
	}
	return flow-res;
}


int main(){
	//scanf("%d%d",&a,&b);
    cin >> a >> b;
	p_beg=0,p_end=a+b+1;
	for(int i=1;i<=a;i++){
		int f, s;
        cin >> f >> s;
        fir[i] = f, sec[i] = s;
        //scanf("%d%d",&fir[i],&sec[i]);
		hh[fir[i]].push_back(i);
		add(i,a+fir[i],1,2),add(i,a+sec[i],1,1);
		add(p_beg,i,1,0);
	}
	for(int i=1;i<=b;i++) add(i+a,p_end,1,0);
	int flow=0;
	while(get_dis()){
		int now=dinic(p_beg,inf);
		while(now) flow+=now,now=dinic(p_beg,inf);
	}
	printf("%d\n",a-flow);
	queue<int>q;
	for(int x=1;x<=a;x++){
		for(int i=0;i<tu[x].size();i++){
			int p=tu[x][i].p,vid=tu[x][i].vid;
			if(p>a&&p<=a+b){
				if(!v[vid]){
					vis[x]=true;
					p-=a;
					if(fir[x]==p) printf("%d\n",x),q.push(fir[x]);
					if(sec[x]==p) er[x]=true;
					break;
				}
			}
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
		if(!vis[i]) printf("%d\n",i);
	}
	return 0;
}
