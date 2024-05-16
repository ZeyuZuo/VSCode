/**
 * @author: Zeyu Zuo
 * @date: 2024-05-14 16:52:18
 */
#include<bits/stdc++.h>
using namespace std;
typedef long long LL;

unordered_map<char,int> s_map;
unordered_map<char,int> t_map;

int main(){
    string s="abcd";
    string t="bdeca";
    for(int i=0;i<s.length();i++){
        auto it = s_map.find(s[i]);
        if(it == s_map.end()){
            s_map[s[i]] = 1;
        }else{
            it->second++;
        }
    }
    for(int i=0;i<t.length();i++){
        auto it = t_map.find(t[i]);
        if(it == t_map.end()){
            t_map[t[i]] = 1;
        }else{
            it->second++;
        }
    }
    for(auto it = t_map.begin();it!=t_map.end();it++){
        char tmp = it->first;
        auto it2 = s_map.find(tmp);
        if(it2 == s_map.end()){
            cout<<tmp;
            return 0;
        }else{
            if(it2->second!=it->second){
                cout<<tmp;
                return 0;
            }
        }
    }
    return 0;
}