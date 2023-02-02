// user input number of elements in vector sort it by using merge sort and find location using binary search

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void merge(vector<int> &v, int start, int mid, int end)
{
    int i = start, j = mid + 1, k = 0;
    vector<int> temp(end - start + 1);
    while (i <= mid && j <= end)
    {
        if (v[i] < v[j])
            temp[k++] = v[i++];
        else
            temp[k++] = v[j++];
    }
    while (i <= mid)
        temp[k++] = v[i++];
    while (j <= end)
        temp[k++] = v[j++];
    for (int i = start, k = 0; i <= end; i++, k++)
        v[i] = temp[k];
}

void mergeSort(vector<int> &v, int start, int end)
{
    if (start < end)
    {
        int mid = (start + end) / 2;
        mergeSort(v, start, mid);
        mergeSort(v, mid + 1, end);
        merge(v, start, mid, end);
    }
}

int binarySearch(vector<int> &v, int start, int end, int key)
{
    if (start <= end)
    {
        int mid = (start + end) / 2;
        if (v[mid] == key)
            return mid;
        else if (v[mid] > key)
            return binarySearch(v, start, mid - 1, key);
        else
            return binarySearch(v, mid + 1, end, key);
    }
    return -1;
}

int main()
{
    int n;
    cout << "Enter number of elements in vector: ";
    cin >> n;
    vector<int> v(n);
    cout << "Enter elements in vector: ";
    for (int i = 0; i < n; i++)
        cin >> v[i];
    mergeSort(v, 0, n - 1);
    cout << "Sorted vector: ";
    for (int i = 0; i < n; i++)
        cout << v[i] << " ";
    cout << endl;
    int key;
    cout << "Enter element to search: ";
    cin >> key;
    int index = binarySearch(v, 0, n - 1, key);
    if (index == -1)
        cout << "Element not found" << endl;
    else
        cout << "Element found at index: " << index << endl;
    return 0;
}
