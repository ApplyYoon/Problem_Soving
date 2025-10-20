#include <stdio.h>

int main(void) {
    int a = 10, b = 20;
    int *p = &a;
    int **pp = &p;

    // TODO: 이중 포인터를 이용해서 p가 b를 가리키게 만드세요.

    printf("%d\n", *p); // 출력: 20
    return 0;
}