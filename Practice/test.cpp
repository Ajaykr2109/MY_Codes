#include <iostream>
using namespace std;
int main()
{
    int n;
    cin >> n;
    if (n >= 3 && n <= 106)
    {
        int arr[n];
        for (int i = 0; i < n; i++)
        {
           
            cin >> arr[i];
        }
        int count = 0;
        for (int i = 0; i < n; i++)
        {
            if (arr[i] > 1)
            {
                count++;
            }
        }
        cout << count;
    }
    else
    {
        cout << "Invalid Input";
    }
    return 0;
}
