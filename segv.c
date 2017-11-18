#include <stdio.h>
#include <stdlib.h>

int dummy_buf[0x1000];

int main(int argc, char* argv[])
{
    int limit = -1;
    int sum = 0;
    if (argc == 1) {
        puts("incorrect argc");
        return 1;
    }
    limit = atoi(argv[1]);
    printf("argv[1] is evaluated as %d\n", limit);
    for (int i = 0; i < limit; i++) {
        sum += dummy_buf[i * 0x200];
    }
    printf("%d\n", sum);
    return 0;
}