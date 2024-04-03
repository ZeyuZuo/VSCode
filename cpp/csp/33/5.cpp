/**
 * @author: Zeyu Zuo
 * @date: 2024-04-03 19:34:55
 */
#include<bits/stdc++.h>
using namespace std;
typedef long long LL;
#define N 500010

typedef struct son {
	int who;
	struct son* next;
}Son;

typedef struct folder {
	int data;
	int parent;
	Son* sons;
}Folder;

Folder folders[N];

void merge(int j)
{
	Son* p = folders[j].sons->next;
	if (p == NULL)
		return;
	Son* newSon = (Son*)malloc(sizeof(Son));
	newSon->who = -1;
	newSon->next = NULL;

	Son* q = newSon;
	while (p)
	{
		folders[j].data += folders[p->who].data;
		Son* pp = folders[p->who].sons->next;
		while (pp)
		{
			folders[pp->who].parent = j;
			Son* son = (Son*)malloc(sizeof(Son));
			son->who = pp->who;
			son->next = NULL;
			q->next = son;
			q = q->next;

			pp = pp->next;
		}
		p = p->next;
	}

	folders[j].sons = newSon;
}

int count(int j)
{
	int sum = 1;
	while (j != 1)
	{
		sum++;
		j = folders[j].parent;
	}
	return sum;
}

int main()
{
	int tmp;
	int n, m;
	cin >> n >> m;
	for (int i = 1; i <= n; i++)
	{
		folders[i].sons = (Son*)malloc(sizeof(Son));
		folders[i].sons->next = NULL;
		folders[i].sons->who = -1;
	}
	for (int i = 2; i <= n; i++)
	{
		scanf("%d", &tmp);
		folders[i].parent = tmp;
		Son* son = (Son*)malloc(sizeof(Son));
		son->who = i;
		son->next = NULL;
		Son* x = folders[tmp].sons;
		while (x->next)
			x = x->next;
		x->next = son;
	}
	for (int i = 1; i <= n; i++)
	{
		scanf("%d", &tmp);
		folders[i].data = tmp;
	}
	int op, j;
	while (m--)
	{
		scanf("%d%d", &op, &j);
		if (op == 1)
		{
			merge(j);
			int sum = 0;
			Son* son = folders[j].sons->next;
			while (son!=NULL)
			{
				son = son->next;
				sum++;
			}
			cout << sum << " " << folders[j].data << endl;
		}
		else
		{
			int path = count(j);
			cout << path << endl;
		}
	}
	return 0;
}