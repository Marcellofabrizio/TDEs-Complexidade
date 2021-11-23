#include <stdio.h>
#include <stdlib.h>

int compare(const void *a, const void *b)
{
    return (*(int *)a - *(int *)b);
}

int main()
{
    int i, n, j, p, count;
    long long int E1[n], E2[n];

    scanf("%d", &n);
    for (i = 0; i < n; i++)
        scanf("%lld", &E1[i]);
    for (i = 0; i < n; i++)
        scanf("%lld", &E2[i]);
    qsort(E1, n, sizeof(int), compare);
    qsort(E2, n, sizeof(int), compare);

    p = 0;
    count = 0;

    for (i = 0; i < n; i++)
    {
        for (j = p; j < n; j++)
        {
            if (E1[j] < E2[i])
            {
                p++;
                count++;
                break;
            }
        }
    }

    printf("%d\n", count);
}
