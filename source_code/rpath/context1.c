#include <stdio.h>
#include "global.h"

void print1() {
    printf("context 1: %d\n", my_value);
}

void set1(int value) {
    my_value = value;
}
