#include <iostream>

using namespace std;

int main()
{
  int n;
  cin >> n;

  for(int i = 1; i <= n; i++) {
   long long j = ((i*i) * ((i*i) -1))/2;
   long long k = 4 * ((i-1) * (i-2));
   cout << j - k << endl;
  };
  return 0;
};
