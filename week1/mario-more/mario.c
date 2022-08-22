#include <cs50.h>
#include <stdio.h>

void print_space(int n) {
   for (int i = 0; i < n; i++)
      printf(" ");
}

void print_block(int n) {
   for (int i = 0; i < n; i++)
      printf("#");
}

int main(void) {
   int n = 0;

   do {
      n = get_int("Height: ");
   } while(n < 1 || n > 8);

   for (int i = 1; i <= n; i++) {
      print_space(n - i);
      print_block(i);
      printf("  ");
      print_block(i);
      printf("\n");
   }
}