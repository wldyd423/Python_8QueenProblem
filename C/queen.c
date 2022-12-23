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
    
    //Dispute Count counts the number of disputes. Every dispute will increment this value.
    //This value will be returned by this function.
    int disputeCount = 0;

    /*
        We search for two queens that either have same x or same y coord
        So array already took care of same y. syntax: [a,b,c,d,...] So no two queens can be
        placed in same column.

        1) Same Row. 
            From position index 0 => we search if other index have the same value.
            ex)
            [1,5,4,1,2,5,7,8]
            we start with 1
            [o1, 5, 4, !1, 2, 5, 7, 8] so we will find dispute in position 4.

        2) Diagonal
            From position index 0 => we search if pos[i]+offset = pos[i+offset]
            Kinda I am not sure of detailed implementation.

            There are two Diagonal disputes. Lower and upper.
            For diagonal values can go negative (like we search for negative values)
            Maybe I might have to filter negative values out? Not sure
    */
    for(int i = 0; i < boardLength; i++){
        for(int j = i + 1; j < boardLength; j++){
            // Same Row
            if(queenPos[i]==queenPos[j]){
                DEBUG("Found Row Dispute! pos[%d]=%d vs pos[%d]=%d",
                i, queenPos[i], j, queenPos[j]);
                disputeCount ++;
            }
            //Diagonal else if because I don't think you can be same row and diagonal at the same time
            else if(queenPos[i] + j - i == queenPos[j]){
                DEBUG("Found Lower Diagonal Dispute! pos[%d]=%d vs pos[%d]=%d",
                i, queenPos[i], j, queenPos[j]);
                disputeCount ++;
            }else if(queenPos[i] + i - j == queenPos[j]){
                DEBUG("Found Upper Diagonal Dispute! pos[%d]=%d vs pos[%d]=%d",
                i, queenPos[i], j, queenPos[j]);
                disputeCount ++;
            }
        }
    }
    //Complexity of this process... Can we do better? (Probably)

    return disputeCount;
}


/*
    Draws The Chess Board State
    Input: Queen Position array (queenPos), Length of Board (boardLength)
    All print is done through DEBUG (only activated with -v option)
*/
void drawBoard(int* queenPos, int boardLength){
    char bot[100] = ".";
    char pref[100] = "";

    // Offset adds to the pref(buffer) that hold string of queen position
    // Sample output:
    // [DEBUG]  QUEEN ALIGNMENT(queenPos): 1 5 4 1 2 5 7 8 
    int offset = 0;
    for(int i = 0; i < boardLength; i++){
        offset += sprintf(pref + offset, "%d ", queenPos[i]);
    }
    DEBUG("QUEEN ALIGNMENT(queenPos): %s", pref);


    /*
        For alignment purpose first line is drawn in this function.
    */
    for(int i = 0; i < boardLength; i++){
        sprintf(bot, "%s - .", bot);
    }

    /*
        Remaining Line:
             | Q |   |   | Q |   |   |   |   |
             . - . - . - . - . - . - . - . - .
        Is printed in pairs. Recursed as much as Board Length.
        Assumption: Board Dimension is n x n
    */
    for(int i = 0; i < boardLength; i++){
        drawLine(queenPos, boardLength, i);
    }
    DEBUG("%s", bot);
}

/*
    Draws the actual line. Found out later that I can use sprintf differently
    Maybe fixing it might be a good idea but it just works.

    ex)
        int offset = 0;
        for(...)
            if(...)
                offset += sprintf(tmp + offset, "Q |");
            else
                offset += sprintf(tmp + offset, "  |");
    
    Not sure but it seems this is the typical syntax.
*/
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