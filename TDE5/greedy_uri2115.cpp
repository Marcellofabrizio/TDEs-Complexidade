#include <bits/stdc++.h>
using namespace std;

int main()
{
    int N;
    while (scanf("%d", &N) != EOF)
    {

        vector<pair<int, int>> processes;
        int d, p;

        for (int i = 0; i < N; i++)
        {
            scanf("%d %d", &d, &p);
            processes.push_back(make_pair(d, p));
        }
        sort(processes.begin(), processes.end());

        int result = 0;

        for (int i = 0; i < N; i++)
        {
            if(result - processes[i].first < 0)
                result = processes[i].first + processes[i].second;

            else
                result += processes[i].second;
        }

        cout << result << endl;
    }

    return 0;
}
