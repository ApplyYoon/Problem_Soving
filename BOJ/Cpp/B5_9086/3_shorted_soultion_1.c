
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
        char *cur = str;
        while (*cur != '\0')
            cur++;
        printf("%c%c\n", str[0], *(cur-1));
    }
    return 0;
}