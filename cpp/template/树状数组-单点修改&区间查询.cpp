/**
 * @author: Zeyu Zuo
 * @date: 2024-04-01 22:07:41
 */
#include<bits/stdc++.h>
using namespace std;
typedef long long LL;

#define N 1000010

LL arr[N]={0};
LL trr[N]={0};

LL n,q; // 数组长度和询问个数

LL lowbit(LL x){return x&(-x);}

/*
// Θ(n) 建树
void init() 
{
    for (int i = 1; i <= n; ++i) {
        trr[i] += arr[i];
        int j = i + lowbit(i);
        if (j <= n) 
            trr[j] += trr[i];
    }
}

// Θ(n) 建树
void init() 
{
    // sum为前缀和数组
    for (int i = 1; i <= n; ++i) {
        trr[i] = sum[i] - sum[i - lowbit(i)];
    }
}

*/


void add(LL i, LL x)
{
    while(i<=n){
        arr[i]+=x;
        i+=lowbit(i);
    }
}

LL getSum(LL i)
{
    LL sum=0;
    while(i>0){
        sum+=arr[i];
        i-=lowbit(i);
    }
    return sum;
}

int main()
{
    cin>>n>>q;
    LL tmp;
    // nlogn的建数组时间
    for(LL i=1;i<=n;i++){
        scanf("%lld",&tmp);
        add(i,tmp);
    }

    LL x,y;
    while(q--){
        scanf("%lld%lld%lld",&tmp,&x,&y);
        if(tmp==1)
            add(x,y);
        else if(tmp==2){
            LL sum=getSum(y)-getSum(x-1);
            cout<<sum<<endl;
        }
    }

    return 0;
}