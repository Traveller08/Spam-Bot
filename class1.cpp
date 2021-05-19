#include<bits/stdc++.h>
using namespace std;
long long int binexpo(int x,int num) {
    if (num==0) {
        return 1;
    }
    if (num%2==0) {
        int temp=binexpo(x,num/2);
        return temp*temp;
    }
    else if (num%2==1) {
        return x*binexpo(x,num-1);
    }
    return 1;
}
int main(){
    int x=5;
    int num=3;
    int ans=binexpo(x,num);
    cout<<ans<<endl;
    return 0;
}