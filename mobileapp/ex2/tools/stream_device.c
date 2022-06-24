#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>

#ifdef WIN32
#include <windows.h>
#elif _POSIX_C_SOURCE >= 199309L
#include <time.h>   // for nanosleep
#else
#include <unistd.h> // for usleep
#endif

void sleep_ms(int milliseconds){ // cross-platform sleep function
#ifdef WIN32
    Sleep(milliseconds);
#elif _POSIX_C_SOURCE >= 199309L
    struct timespec ts;
    ts.tv_sec = milliseconds / 1000;
    ts.tv_nsec = (milliseconds % 1000) * 1000000;
    nanosleep(&ts, NULL);
#else
    if (milliseconds >= 1000)
      sleep(milliseconds / 1000);
    usleep((milliseconds % 1000) * 1000);
#endif
}

int main(int ac, char **av) {
    if (ac == 1) {
        fprintf(stderr, "Usage: %s <device_id>\n", av[0]);
        return 1;
    }
    srand(time(NULL));
    char *device_id = av[1];
    int chance = 600;
    int n = rand() % chance;
    bool error = n == 1;
    int iterations = 0;
    while (true) {
        if (!error) {
            printf("FRAME 1,2,3,1,3,4,1,2,3,4,2,1,2,3\n");
            n = rand() % chance;
            error = n == 1;
            printf("%d\n", chance);
        } else {
            printf("ERROR: NO FRAME\n");
        }
        sleep_ms(16);
        iterations += 1;
        // every 60 frames we make it more likely to crash
        if (iterations == 60) {
            chance -= 1;
            iterations = 0;
        }
    }
    return 0;
}