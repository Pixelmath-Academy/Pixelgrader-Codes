#include <bits/stdc++.h>
using namespace std;

int main()
{
  int n;
  cin >> n;
  cout << n%10 << endl;
  cout << (n%100)/10 << endl;
  cout << (n%1000)/100 << endl;
  cout << (n%10000)/1000 << endl;
  return 0;
  }