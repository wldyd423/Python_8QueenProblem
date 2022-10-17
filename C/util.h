#ifndef UTIL_H_
#define UTIL_H_

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <getopt.h>


#define DEBUG(fmt, ...)\
    do { if (DEBUG_VERBOSE) fprintf(stderr, "[DEBUG]  " fmt"\n", ##__VA_ARGS__); } while(0)


#define EXIT_FAILURE 1
extern int DEBUG_VERBOSE;


#endif





