#include <math.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    if (argc != 3) {
        fprintf(stderr, "Usage: %s <number> <number>\n", argv[0]);
        return 1;
    }
    double num1 = atof(argv[1]);
    double num2 = atof(argv[2]);
    double result = sqrt(num1/num2);
    printf("%.2f\n", result);
    return 0;
}
