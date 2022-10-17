//Mandatory
#include "queen.h"
#include "util.h"
int DEBUG_VERBOSE = 0;

int main(int argc, char* argv[]){
    hello();
    int c;
    while((c = getopt(argc, argv, "a:b:v")) != -1){
        switch(c){
            case 'a':
                hello();
                break;
            case 'b':
                hello();
                hello();
                break;
            case 'v':
                DEBUG_VERBOSE = 1;
                break;
            default:
                fprintf(stderr, "Usage: %s [-a something] [-b anotherthing]\n", argv[0]);
                exit(EXIT_FAILURE);
        }
    }

    //printBlankBoard(8);

    int queenState[8] = {1,5,4,1,2,5,7,8};

    findDispute(queenState, 8);
    // printBlankBoard(16);
    return 0;
}