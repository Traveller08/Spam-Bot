#include <bits/stdc++.h>
using namespace std;
#define ll long long int
ll st[10000]={},arr[10000]={};
void build_tree(ll si,ll ss,ll se)
{
   if(ss==se)st[si]=arr[ss];
   ll mid=(ss+se)/2;
   build_tree(2*si,ss,mid);
   build_tree(2*si+1,mid+1,se);
   st[si]=min(st[2*si],st[2*si+1]);
}
ll query(ll si,ll se,ll ss,ll qs,ll qe)
{
    if(qs>se || qe<ss) return 100000000000;
    if(ss>=qs && se<=qe)return st[si];
    ll mid=(ss+se)/2;
    ll l=query(2*si,ss,mid,qs,qe);
    ll r=query(2*si+1,mid+1,se,qs,qe);

    return min(l,r);
}
int main()
{

    return 0;
}