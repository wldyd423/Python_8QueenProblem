#include "queen.h"
#include "util.h"
int DEBUG_VERBOSE;

void hello(){
    printf("%s", MANDATORY);
}

void printBlankBoard(int n){
    char tmp[100] = "|";
    for(int i = 0 ; i < n ; i++){
        sprintf(tmp, "%s   |", tmp);
    }
    sprintf(tmp, "%s\n", tmp);
    char bot[100] = ".";
    for(int i = 0; i < n; i++){
        sprintf(bot, "%s - .", bot);
    }
    sprintf(bot, "%s\n", bot);

    for(int i = 0; i < n; i++){
        DEBUG("%s", bot);
        DEBUG("%s", tmp);
    }
    DEBUG("%s", bot);
}