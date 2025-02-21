#include <iostream>
using namespace std;

int main() {
  int x;
  cin>>x;
  if (x>=0 && x<=200) {
    if (x%2==0) {
      cout<<"Even";
    } else {
      cout<<"Odd";
    }
  } else {
    cout<<"NULL";
  }
  return 0;
}