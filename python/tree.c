#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>

#define RED "\x1b[31m"
#define GREEN "\x1b[32m"
#define YELLOW "\x1b[33m"
#define BLUE "\x1b[34m"
#define MAGENTA "\x1b[35m"
#define CYAN "\x1b[36m"
#define RESET "\x1B[37m"

#ifdef _unix_
#include <unistd.h>
#elif defined _WIN32
#include <windows.h>
#define sleep(x) Sleep(1000 * (x))
#define RED ""
#define GREEN ""
#define YELLOW ""
#define BLUE ""
#define MAGENTA ""
#define CYAN ""
#define RESET ""
#endif

void clrscr()
{
    system("@cls||clear");
}

void printRandLeaf()
{
    char leaftypes[5] = {'.', '*', '+', 'o', 'O'};
    int temp = rand() % 4;

    if (temp == 1)
    {
        printRandColorOrnaments();
        printf("%c ", leaftypes[rand() % 5]);
        printf(RESET);
    }
    else
    {
        printRandColorLeaves();
        printf("%c ", leaftypes[1]);
        printf(RESET);
    }
}

void printRandSpace()
{
    char spacetypes[3] = {' ', '*', '+'};
    int temp = rand() % 10;

    if (temp == 1)

        printf("%c", spacetypes[rand() % 3]);

    else
        printf("%c", spacetypes[0]);
}

void printRandColorOrnaments()
{
    int temp = rand() % 7;

    switch (temp)
    {
    case 0:
        printf(RESET);
        break;
    case 1:
        printf(YELLOW);
        break;
    case 2:
        printf(BLUE);
        break;
    case 3:
        printf(CYAN);
        break;
    case 4:
        printf(YELLOW);
        break;
    case 5:
        printf(MAGENTA);
        break;
    default:
        printf(RED);
        break;
    }
}

void printRandColorLeaves()
{
    int temp = rand() % 3;

    switch (temp)
    {
    case 0:
        printf(RESET);
        break;

    default:
        printf(GREEN);
        break;
    }
}

void triangle(int f, int n, int toth)
{
    int i, j, k = 2 * toth - 2;

    for (i = 0; i < f - 1; i++)
        k--;

    for (i = f - 1; i < n; i++)
    {

        printf("*");

        for (j = 0; j < k; j++)
            printRandSpace();

        k = k - 1;

        for (j = 0; j <= i; j++)
            printRandLeaf();

        for (j = 0; j < k + 1; j++)
            printRandSpace();

        printf("*");

        printf("\n");
    }
}

void printTree(int h)
{
    int start = 1, stop = 0, diff = 3, i;

    for (i = 0; i < (h * 2) - 8; i++)
        printf(" ");

    printf("Merry Christmas!\n");

    for (i = 0; i < (h * 4); i++)
        printf("*");

    printf("\n");

    while (stop < h + 1)
    {
        stop = start + diff;
        triangle(start, stop, h);
        diff++;
        start = stop - 2;
    }
}

void printLog(int n)
{
    int i, j, k = 2 * n - 4;

    for (i = 1; i <= 4; i++)
    {
        printf("*");

        for (j = 0; j < k; j++)
            printRandSpace();

	printf("\x1b[47m");
        for (j = 1; j <= 6; j++)
            printf("#");
	printf("\x1b[m");

        for (j = 0; j < k; j++)
            printRandSpace();

        printf("*");

        printf("\n");
    }

    for (j = 0; j < (k * 2) + 8; j++)
        printf("*");

    printf("\n");
}

int main()
{
    srand(time(NULL));
    int ht = 20;
    printf(RESET);

    while (1)
    {
        clrscr();

        printTree(ht);

        printLog(ht);

        sleep(1);
    }

    return 0;
}