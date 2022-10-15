#ifndef UTIL_H_
#define UTIL_H

#include <stdlib.h>
#include <string.h>
#include <getopt.h>
#define EXIT_FAILURE 1

int DEBUG_VERBOSE = 0;

#define DEBUG(fmt, ...)\
    do { if (DEBUG_VERBOSE) fprintf(stderr, "[DEBUG]  " fmt, ##__VA_ARGS__); } while(0)

#endif





