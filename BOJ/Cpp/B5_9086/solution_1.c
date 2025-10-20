// train pointer

#include <stdio.h>
#include <string.h>

int main(void) {
    int n;
    char str[1001];

    scanf("%d", &n);
    getchar();

    for (int i = 0; i < n; i++) {
        fgets(str, sizeof(str), stdin);

        str[strcspn(str, "\n")] = '\0';

        char firstChar = str[0], lastChar;
        char *cur = str;
        while (*cur != '\0')
        {
            lastChar = *cur;
            // printf("last Char %c\n", lastChar);
            cur++;
        }
        printf("%c%c\n", firstChar, lastChar);
    }
    return 0;
}