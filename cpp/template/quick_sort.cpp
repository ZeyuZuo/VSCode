/**
 * @author: Zeyu Zuo
 * @date: 2024-05-14 13:35:01
 */
#include<bits/stdc++.h>
using namespace std;
typedef long long LL;

void swapInt(int* x, int* y) {
    int tmp = *x;
    *x = *y;
    *y = tmp;
}

int partition(int arr[], int start, int end){
    /**
     * 我们以arr[start]为标准
    */
    int i = start, j = end;
    while(i < j){
        while(i < j && arr[j] >= arr[start])
            j--;
        while(i < j && arr[i] <= arr[start])
            i++;
        swapInt(&arr[i], &arr[j]);
    }
    swapInt(&arr[i], &arr[start]);
    return i;
}

void quickSort(int arr[], int start, int end){
    if(start >= end)
        return;
    int idx = partition(arr, start, end);
    quickSort(arr, start, idx - 1);
    quickSort(arr, idx + 1, end);
}

int main(){
    int arr[] = {2, 5, 6, 4, 8};
    quickSort(arr, 0, 4);
    for(int i = 0; i < 5; i++)
        cout<<arr[i]<<" ";
    return 0;
}