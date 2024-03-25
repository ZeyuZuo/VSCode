/*
* @acwing app=acwing.cn id=507 lang=C++
*
* 505. 火柴排队
*/

// @acwing code start
/**
 * @author: Zeyu Zuo
 * @date: 2024-03-16 18:49:05
 * 
 */
#include<bits/stdc++.h>
using namespace std;
#define N 100010

int n;
int a[N],b[N],c[N],d[N];

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


int cnt = 0;

void merge(int arr[],int l,int mid,int r)
{
    vector<int> tmp;
    int i=l,j=mid+1;
    while(i<=mid && j<=r){
        if(arr[i]>arr[j]){
            tmp.push_back(arr[j]);
            cnt = (cnt+mid-i+1)%99999997;
            j++;
        }
        else{
            tmp.push_back(arr[i]);
            i++;
        }
    }
    while(i<=mid){
        tmp.push_back(arr[i]);
        i++;
    }
    while(j<=r){
        tmp.push_back(arr[j]);
        j++;
    }

    for(int i=0;i<tmp.size();i++)
        arr[l+i]=tmp[i];
}

void merge_sort(int arr[],int l,int r)
{
    if(l>=r)
        return;
    int mid = (r-l)/2+l;
    merge_sort(arr,l,mid);
    merge_sort(arr,mid+1,r);

    merge(arr,l,mid,r);
}

int main()
{
    cin>>n;
    for(int i=0;i<n;i++)
        scanf("%d",&a[i]);
    for(int i=0;i<n;i++)
        scanf("%d",&b[i]);
    
    work(a);
    work(b);

    unordered_map<int,int> maps;
    for(int i=0;i<n;i++){
        maps[a[i]]=i;
        a[i]=i;
    }
    for(int i=0;i<n;i++)
        b[i]=maps[b[i]];
    
    // 计算逆序对
    // for(int i=0;i<n;i++)
    //     cout<<b[i]<<" ";
    // cout<<endl;
    merge_sort(b,0,n-1);
    cout<<cnt;

    return 0;
}

// @acwing code end