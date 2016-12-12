#include <stdio.h>

int main()
{
  int i, cap, sum;
  cap = 1000;
  sum = 0;
  for (i = 1; i < cap; i++) {
    if (i % 3 == 0 || i % 5 == 0)
      sum += i;
  }
  printf("%d\n", sum);
  return 0;
}
