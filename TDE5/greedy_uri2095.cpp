
#include <bits/stdc++.h>
using namespace std;

int main()
{

    int i, n, j, p, count;
    cin >> n;

    long long int E1[n];
    long long int E2[n];

    for (i = 0; i < n; i++)
    {
        cin >> E1[i];
    }

    for (i = 0; i < n; i++)
    {
        cin >> E2[i];
    }

    sort(E1, E1 + n);
    sort(E2, E2 + n);

    p = 0;
    count = 0;

    for (i = 0; i < n; i++)
    {
        for (j = p; j < n; j++)
        {
            if (E1[j] < E2[i])
            {
                count++;
                p++;
                break;
            }
        }
    }

    cout << count << endl;

    return 0;
}