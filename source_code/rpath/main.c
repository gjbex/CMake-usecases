#include <stdio.h>
#include "global.h"
#include "context1.h"
#include "context2.h"

int main() {
    print1();
    print2();
    printf("set1\n");
    set1(1);
    print1();
    print2();
    printf("set2\n");
    set2(2);
    print1();
    print2();
    return 0;
}
