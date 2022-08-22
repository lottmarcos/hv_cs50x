#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int dumbUser (int argc, string argv)
{
   if (argc != 2)
   {
      printf("Usage: ./substitution key\n");
      return 1;
   }
   if (strlen(argv) != 26)
   {
      printf("Key must contain 26 characters.\n");
      return 1;
   }
   else
   {
            for (int i = 0; i < strlen(argv) ; i++) // checking each element of string
            {

                if (! isalpha(argv[i])) // if contain non-alphabet
                {
                    printf("Key must contain 26 characters.\n");
                    return 1;
                }

                for (int j = i + 1 ; j < strlen(argv) ; j++) // checking to the next element
                {

                    if (toupper(argv[j]) == toupper(argv[i])) // checking repeated element
                    {
                        printf("Key must not contain repeated alphabets.\n");
                        return 1;
                    }
                }
            }
      return 0;
   }
}

void makechange(char pos, string key) // passing p[i] and upper/lower(alpha array)
{
    string alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"; // alphabet array

    for (int i = 0; i < strlen(alpha); i++) // accessing each element in alpha array
    {
        if (islower(pos)) // p[i] is lower
        {
            if (pos == tolower(alpha[i]))
            {
                printf("%c", tolower(key[i]));
            }
        }
        else // for UPPERCASE // p[i] is upper
        {
            if (pos == toupper(alpha[i]))
            {
                printf("%c", toupper(key[i]));
            }
        }
    }
}

int main(int argc, string argv[])
{
   string key = argv[1];

   if (dumbUser(argc, key))
   {
      return 1;
   }

   string s = get_string("plaintext: ");
   char c;
    printf("ciphertext: ");

    for (int i = 0; i < strlen(s); i++)
    {
        if (isalpha(s[i])) // checking p[i] is alphabet
        {
            c = s[i];
            if (islower(s[i]))
            {
                makechange(tolower(c), key); // passing p[i] in lower-case
            }
            else
            {
                makechange(toupper(c), key); // passing p[i] in UPPER-CASE
            }
        }
        else
        {
            printf("%c", s[i]);
        }
    }

    printf("\n");
}

