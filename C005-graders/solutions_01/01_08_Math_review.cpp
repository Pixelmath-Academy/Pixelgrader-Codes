#include <iostream> 
#include <math.h>
using namespace std;

int main() {
  int s;
  double a,b;
  cin >> s >> a >> b;
  if (s == 1) {
    cout << sqrt(a+b);
  }
  if (s == 2) {
    cout << ceil(a+b);
  }
  if (s == 3) {
    cout << floor(a+b);
  }
  if (s == 4) {
    cout << pow(a,b);
  }
  if (s == 5) {
    cout << fabs(2*b);
  }
  return 0;
}