#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <math.h>

int main(void)
{
   int letters = 0, words = 1, sentences = 0;

   string s = get_string("Text: ");
//count words
    for (int i = 0; i < strlen(s); i++)
    {
       if ((s[i] >= 'a' && s[i] <= 'z') || (s[i] >= 'A' && s[i] <= 'Z'))
       {
           letters++;
       }
       else if (s[i] == ' ')
       {
           words++;
       }
       else if (s[i] == '.' || s[i] == '!' || s[i] == '?')
       {
           sentences++;
       }
    }

    float index = 0.0588 * (100 * (float) letters / (float) words) - 0.296 * (100 * (float) sentences / (float) words) - 15.8;
    if (index < 16 && index >= 0)
    {
        printf("Grade %i\n", (int) round(index));
    }
    else if (index >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Before Grade 1\n");
    }


}