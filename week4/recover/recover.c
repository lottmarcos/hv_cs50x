#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

const int BLOCK_SIZE = 512;

int main(int argc, char *argv[])
{
   // Check command-line arguments
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE\n");
        return 1;
    }

    // Open files and determine scaling factor
    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

   unsigned char buffer[BLOCK_SIZE];
   int count = 0;
   FILE *output = NULL;
   char *filename = malloc(8 * sizeof(char));

   while (fread(buffer, sizeof(char), BLOCK_SIZE, input))
   {
      if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
         {
            sprintf(filename, "%03i.jpg", count);
            output = fopen(filename, "w");
            count++;
         }
         if (output != NULL)
            fwrite(buffer, sizeof(char), BLOCK_SIZE, output);
   }


   free(filename);
   fclose(output);
   fclose(input);

   return 0;

}