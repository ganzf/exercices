#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>
#include <math.h>
#include <stdint.h>

int main(void) {
    time_t t = time(NULL);
    uint64_t rounded = t / 10;
    time_t base = rounded * 10;
    // Constant seed every 10 seconds
    srand(base);
    int showIos = rand() % 100;
    int showAndroid = rand() % 100;
    if (showIos > 10) {
        printf("%s\n", "ios uuid-1-ios IphoneX");
    }
    if (showAndroid > 10) {
        printf("%s\n", "android uuid-1-android GalaxyS20");
    }
    return 0;
}