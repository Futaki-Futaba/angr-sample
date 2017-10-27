#include <stdio.h>
#include <string.h>

void correct(void)
{
    puts("correct");
}

int main()
{
    char buf[32];
    fgets(buf, sizeof(buf), stdin);
    // authorization
    if(strcmp(buf, "flag{angr_makes_it_easy}") == 0)
    {
        correct();
    }
    return 0;
}