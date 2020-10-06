#include <iostream>
using namespace std;
int main()
{
    int T;
    cin >> T;

    while (T--)
    {
        int n;
        cin >> n;

        int arr[n];
        for (int i = 0; i < n; i++) //Store elements in an array
        {
            cin >> arr[i];
        }

        for (int i = 1; i < n; i++)
        {
            cout << (arr[i - 1] | arr[i]) << " "; //New element is OR of consecutive elements.
        }
        cout << arr[n - 1];

        cout << endl;
    }

    return 0;
}