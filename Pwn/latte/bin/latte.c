#include <stdio.h>

int main()
{
    long floor = 0;
    char coffee[32];

    setbuf(stdout, NULL);
    setbuf(stdin, NULL);
    setbuf(stderr, NULL);

    puts("Please pour me some coffee:");
    gets(coffee);

    puts("\nThanks!\n");

    if (floor == 0xcafebabe)
    {
        puts("Thanks for your latte! You deserve for the flag!");
        system("cat flag.txt");
    }
}
