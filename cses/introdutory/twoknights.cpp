#include <iostream>

using namespace std;

int main()
{
  long long int n, i, j, k;
  cin >> n;

  for(i = 1; i <= n; i++) {
   j = ((i*i) * ((i*i) -1))/2;
   k = 4 * ((i-1) * (i-2));
   cout << j - k << endl;
  };
  return 0;
};
