#include <stdio.h>

void f(int **pp) {
    static int b = 20;
    *pp = &b;   // 원래 포인터(p)가 가리키는 주소를 바꿈
}

int main(void) {
    int a = 10;
    int *p = &a;
    f(&p);        // p의 주소를 전달
    printf("*p: %d\n", *p);
}