#include <cs50.h>
#include <stdio.h>

string check_number(long int card) {
   if ((card >= 340000000000000 && card < 350000000000000) ||
       (card >= 370000000000000 && card < 380000000000000)) {
      return "AMEX\n";
   }
   else if (card >=5100000000000000 && card < 5600000000000000) {
      return "MASTERCARD\n";
   }
   else if ((card >=4000000000000 && card < 5000000000000)||
            (card >=4000000000000000 && card < 5000000000000000)) {
      return "VISA\n";
   }
   else
      return "INVALID\n";
}

int calculate_checksum(long int card) {
   // Calculate checksum
    int sum1 = 0;
    int sum2 = 0;
    long x = card;
    int total = 0;
    int mod1;
    int mod2;
    int d1;
    int d2;
    do {
        // Remove last digit and add to sum1
        mod1 = x % 10;
        x = x / 10;
        sum1 = sum1 + mod1;
        // Remove second last digit
        mod2 = x % 10;
        x = x / 10;
        // Double second last digit and add digits to sum2
        mod2 = mod2 * 2;
        d1 = mod2 % 10;
        d2 = mod2 / 10;
        sum2 = sum2 + d1 + d2;
    }
    while (x > 0);
    total = sum1 + sum2;

    // Next check Luhn Algorithm
    if (total % 10 != 0) {
        printf("INVALID\n");
        return 0;
    }
    else {
       return 1;
    }
}

int length_counter(long int card) {
    int i = 0;
    long counter = card;
    while (counter > 0)
    {
        counter = counter / 10;
        i++;
    }
    return i;
}

int main(void) {
   long int card = get_long("Number:" );
   string card_type = check_number(card);
   int length = length_counter(card);

   if (length != 13 && length != 15 && length != 16) {
        printf("INVALID\n");
        return 0;
    }

   if (calculate_checksum(card)) {
      printf("%s", card_type);
   }

}