#include<stdio.h>
#define NMAX 10
#define IMAX 100
struct Interval {
    long start;
    long end;
    long change;
};

typedef struct Interval Interval;

long find_location(long seed, int n, int intervals_count[], Interval intervals[][IMAX]) {
    long tmp = seed;
    for (int j = 0; j < n; j++) {
        for (int i = 0; i < intervals_count[j]; i++) {
            if (intervals[j][i].start <= tmp && tmp <= intervals[j][i].end) {
                tmp += intervals[j][i].change;
                break;
            }
        }
    }
    return tmp;
}

void print_long_array(int n, long arr[]) {
    for (int i = 0; i < n; i++) {
        printf("%ld ", arr[i]);
    }
    printf("\n");
}

void print_int_array(int n, int arr[]) {
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int main() {
    FILE *fp = fopen("intervals.txt", "r");
    int intervals_count[NMAX];
    Interval intervals[NMAX][IMAX];
    long int seeds[NMAX];
    long int ranges[NMAX];
    int seeds_count;
    fscanf(fp, "%d", &seeds_count);
    for (int i = 0; i < seeds_count; i++) {
        fscanf(fp, "%ld %ld", seeds + i, ranges + i);
    }
    //print_long_array(seeds_count, seeds);
    //print_long_array(seeds_count, ranges);
    int n;
    fscanf(fp, "%d", &n);
    for (int i = 0; i < n; i++) {
        fscanf(fp, "%d", &intervals_count[i]);
        for (int j = 0; j < intervals_count[i]; j++) {
            fscanf(fp, "%ld %ld %ld", &intervals[i][j].start, &intervals[i][j].end, &intervals[i][j].change);
        }
    }

    //print_int_array(n, intervals_count);

    fclose(fp);

    long min_location = 9223372036854775807;

    for (int i = 0; i < seeds_count; i++) {
        printf("starting seed %ld with range %ld\n", seeds[i], ranges[i]);
        int percentage = 0;
        for (long j = seeds[i]; j < seeds[i] + ranges[i]; j++) {
            long loc = find_location(j, n, intervals_count, intervals);
            /*
            if (loc < min_location) {
                min_location = loc;
            }
            
            if ((j - seeds[i]) * 100 / ranges[i] > percentage) {
                percentage += 1;
                printf("%d\n", percentage);
            }
            */
        }
        printf("done range: %ld\n", min_location);
    }
    printf("%ld\n", min_location);

}