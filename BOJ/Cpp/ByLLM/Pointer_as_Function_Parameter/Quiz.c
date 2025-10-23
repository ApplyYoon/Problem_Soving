#include <stdio.h>

void swap(int *x, int *y) {
    // TODO: 포인터를 이용한 값 교환
    
}

int main(void) {
    int a = 3, b = 7;
    swap(&a, &b);
    printf("%d %d\n", a, b); // 출력: 7 3
    return 0;
}