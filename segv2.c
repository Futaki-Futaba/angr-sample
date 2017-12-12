#include <stdio.h>
#include <stdlib.h>

int buf[4] = {0, 1, 2, 3};

int main(int argc, char* argv[])
{
    int pos = -1;
    if (argc == 1) {
        puts("incorrect argc");
        return 1;
    }
    pos = atoi(argv[1]);
    printf("argv[1] is evaluated as %d\n", pos);
    printf("%d\n", buf[pos]);
    return 0;
}