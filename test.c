
#include <stdio.h>
#include <math.h>

int main()
{
      int count = 0;
      double n = 8;

      int inner_j = 0;
      int inner_k = 0;
      int inner_i = 0;

      int i, j, k;

      for (j = 1; j <= n; j = j * 2)
            for (i = j; i > 1; i = i / 2)
                  count++;
      // printf("Inner i %d\n", inner_i);
      // printf("Inner k %d\n", inner_k);
      // printf("Inner j %d\n", inner_j);

      printf("Count %d\n", count);
      return 0;
}
