#include <stdio.h>
#include "global.h"

void print2() {
    printf("context 1: %d\n", my_value);
}

void set2(int value) {
    my_value = value;
}
