
#include <iostream>
using namespace std;
//Since the test cases are very large number ,better to use unsigned int.
int main()
{
  unsigned int tests;
  cin >> tests;
  while (tests--)
  {
    unsigned long long last;
    cin >> last;

    unsigned long long sum = 0;
    //First Fibonacci numbers
    unsigned long long a = 1;
    unsigned long long b = 2;

    // until we reach the limit
    while (b <= last)
    {
      // even 
      if (b % 2 == 0)
        sum += b;

      // next Fibonacci number
      auto next = a + b;
      a = b;
      b = next;
    }

    cout << sum <<endl;
  }
  return 0;
}
