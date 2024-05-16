/**
 * @author: Zeyu Zuo
 * @date: 2024-05-14 13:28:59
 */
#include<bits/stdc++.h>
using namespace std;
typedef long long LL;

void merge(int arr[], int start, int mid, int end){
    int i = start, j = mid + 1, k = 0;
    int *tmp = (int *)malloc((end - start + 1) * sizeof(int));
    while(i <= mid && j <= end){
        if(arr[i] < arr[j])
            tmp[k++] = arr[i++];
        else
            tmp[k++] = arr[j++];
    }
    while(i <= mid)
        tmp[k++] = arr[i++];
    while(j <= end)
        tmp[k++] = arr[j++];
    for(int i = 0; i < k; i++)
        arr[start + i] = tmp[i];
    free(tmp);
}

void merge_sort(int arr[], int start, int end){
    if(start >= end)
        return;
    int mid = (start + end) / 2;
    merge_sort(arr, start, mid);
    merge_sort(arr, mid + 1, end);
    merge(arr, start, mid, end);
}

int main(){
    int arr[] = {3, 2, 1, 4, 5, 6, 7, 8, 9};
    merge_sort(arr, 0, 8);
    for(int i = 0; i < 9; i++)
        cout << arr[i] << " ";
    return 0;
}