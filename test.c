
#include <stdio.h>
#include <math.h>

int main()
{
      int count = 0;
      double n = 10;

      int inner_j = 0;
      int inner_k = 0;
      int inner_i = 0;

      int i, j, k;

      // for (j = 1; j <= n; j = j * 2)
      // for (i = j; i > 1; i = i / 2)
      // count++;

      for (i = 0; i < n; i++)
      {
            for (j = i + 1; j < n; j++)
            {
                  for (k = 0; k < n; k++)
                  {
                        // Ops. Fundamentais
                        count++;
                  }
            }
      }
      // for (i = 0; i < n; i++)
      // {

      //       for (k = n - 1; k >= i; k--)
      //       {
      //             count++;
      //       }

      //       for (k = i + 1; k < n; k++)
      //       {
      //             for (j = n - 1; j >= i; j--)
      //             {
      //                   count++;
      //             }
      //       }
      // }
      // printf("Inner i %d\n", inner_i);
      // printf("Inner k %d\n", inner_k);
      // printf("Inner j %d\n", inner_j);

      printf("Count %d\n", count);
      return 0;
}
