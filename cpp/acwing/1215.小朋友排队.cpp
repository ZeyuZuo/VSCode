/*
* @acwing app=acwing.cn id=1217 lang=C++
*
* 1215. 小朋友排队
*/

// @acwing code start
/**
 * @author: Zeyu Zuo
 * @date: 2024-03-25 16:11:24
 */
#include<bits/stdc++.h>
using namespace std;

#define N 100010
int n;
long long ans=0;
long long b[N]={0};
int a[N],c[N];


void work(int arr[])
{
    for(int i=0;i<n;i++)
        c[i]=i;
    sort(c,c+n,[&](int i,int j){
        return arr[i]<arr[j];
    });
    for(int i=0;i<n;i++)
        arr[c[i]]=i;
}

void merge(int arr[],int l,int mid,int r)
{
    vector<int> tmp;
    int i=l,j=mid+1;
    int s=0;
    while(i<=mid&&j<=r){
        if(arr[i]>arr[j]){
            tmp.push_back(arr[j]);
            b[arr[j]]=b[arr[j]]+(mid-i+1);
            s++;
            j++;
        }
        else{
            tmp.push_back(arr[i]);
            b[arr[i]]+=s;
            i++;
        }
    }
    while(i<=mid){
        tmp.push_back(arr[i]);
        b[arr[i]]+=s;
        i++;
    }
    while(j<=r){
        tmp.push_back(arr[j++]);
    }
}

void merge_sort(int arr[],int l,int r)
{
    if(l>=r)
        return;
    int mid=(l+r)/2;
    merge_sort(arr,l,mid);
    merge_sort(arr,mid+1,r);

    merge(arr,l,mid,r);
}

int main()
{
    cin>>n;
    for(int i=0;i<n;i++)
        scanf("%d",&a[i]);
    work(a);
    // for(int i=0;i<n;i++)
    //     cout<<a[i]<<" ";
    // cout<<endl;
    merge_sort(a,0,n-1);

    for(int i=0;i<n;i++){
        ans+=(b[i]+1)*b[i]/2;
        cout<<b[i]<<" ";
    }
    cout<<endl;

    cout<<ans;
    return 0;
}

// @acwing code end