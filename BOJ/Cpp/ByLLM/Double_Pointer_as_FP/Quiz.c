#include <stdio.h>

void change_pointer(int **pp) {
    // TODO: 이중 포인터를 이용해서
    //       포인터가 b를 가리키게 만드세요.
}

int main(void) {
    int a = 10, b = 20;
    int *p = &a;

    printf("Before: *p = %d\n", *p);

    change_pointer(&p);  // p의 주소 전달

    printf("After: *p = %d\n", *p);  // 출력: 20
    return 0;
}