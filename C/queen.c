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
    char bot[100] = ".";
    for(int i = 0; i < n; i++){
        sprintf(bot, "%s - .", bot);
    }

    for(int i = 0; i < n; i++){
        DEBUG("%s", bot);
        DEBUG("%s", tmp);
    }
    DEBUG("%s", bot);
}

int findDispute(int* queenPos, int boardLength){
    DEBUG("findDispute(): Looking for disputes...");
    DEBUG("detected boardLength: %d", boardLength);
    drawBoard(queenPos, boardLength);
    
}
void drawBoard(int* queenPos, int boardLength){
    char bot[100] = ".";
    char pref[100] = "";
    for(int i = 0; i < boardLength; i++){
        sprintf(pref, "%d %s", queenPos[i], pref);
        DEBUG("%s", pref);
    }
    DEBUG("%s", pref);
    // for(int i = 0; i < boardLength; i++){
    //     sprintf(pref, " %d %s", queenPos[i], pref);
    // }
    // DEBUG("%s", pref);
    for(int i = 0; i < boardLength; i++){
        sprintf(bot, "%s - .", bot);
    }

    for(int i = 0; i < boardLength; i++){
        drawLine(queenPos, boardLength, i);
    }
    DEBUG("%s", bot);
}
void drawLine(int* queenPos, int boardLength, int pos){
    char tmp[100] = "|";
    char bot[100] = ".";
    for(int i = 0; i < boardLength; i++){
        sprintf(bot, "%s - .", bot);
    }
    for(int i = 0; i < boardLength; i++){
        if(queenPos[i] == pos + 1){
            sprintf(tmp, "%s Q |", tmp);
        }else{
            sprintf(tmp, "%s   |", tmp);
        }
    }
    DEBUG("%s", bot);
    DEBUG("%s", tmp);
}