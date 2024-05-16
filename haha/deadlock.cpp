#include<iostream>
#include<thread>
#include<windows.h>

using namespace std;

bool lock1 = false;
bool lock2 = false;

void lock(bool *lock){
    *lock = true;
}

void function1(){
    lock(&lock1);
    printf("lock1 has been acquired\n");
    Sleep(1000);
    while(lock2){
        printf("waiting for lock2\n");
        Sleep(1000);
    }
}

void function2(){
    lock(&lock2);
    printf("lock2 has been acquired\n");
    Sleep(1000);
    while(lock1){
        printf("waiting for lock1\n");
        Sleep(1000);
    }
}

int main(){
    thread t1(function1);
    thread t2(function2);
    t1.join();
    t2.join();
    return 0;
}