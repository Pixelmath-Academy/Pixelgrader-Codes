#include <iostream>
using namespace std;

int main () {
  double n;
  cin >> n;
  int i = n;
  if (n < 0) {
    i = i - 1;
  }
  cout << i;
  return 0;
}
