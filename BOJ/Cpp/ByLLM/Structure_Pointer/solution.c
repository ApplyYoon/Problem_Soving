/*
문제:
학생 정보를 구조체로 정의하고, 구조체 포인터를 통해 데이터를 수정하세요.
*/

#include <stdio.h>

typedef struct {
    char name[20];
    int age;
} Student;

int main(void) {
    Student s1 = {"Alice", 19};
    Student *sp;

    // TODO: sp가 s1을 가리키도록 하고,
    // 포인터로 age를 20으로 수정하세요.
    
    sp = &s1;
    s1.age = 20;
    
    printf("%s %d\n", s1.name, s1.age); // 출력: Alice 20
    return 0;
}