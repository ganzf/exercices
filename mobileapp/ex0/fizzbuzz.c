#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

void fizzbuzz(int limit, char *first, char *second) {
  for (int tmp = 1; tmp <= limit; tmp++) {
    bool divideBy3 = tmp % 3 == 0;
    bool divideBy5 = tmp % 5 == 0;
    bool doesNotDivide = divideBy3 == false && divideBy5 == false;
    if (divideBy3 == true) {
      printf("%s", first);
    }
    if (divideBy5 == true) {
      printf("%s", second);
    }
    if (doesNotDivide) {
      printf("%i", tmp);
    }
    printf("\n");
  }
}

int main(int argc, char **argv) {
  if (argc <= 1) {
    return 1;
  }
  int number = atoi(argv[1]);
  fizzbuzz(number, "fizz", "buzz");
  return 0;
}
