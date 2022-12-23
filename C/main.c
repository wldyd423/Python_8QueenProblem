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
    int count;
    count = findDispute(queenState, 8);

    printf("[OUTPUT] The Dispute Count is: %d\n", count);
    // printBlankBoard(16);



    /*
    
    TODO: Now implement actual Queens Problem.

    1) We create random board states. Main function will do this
    I am not sure if passing multiple arrays in C across functions would be a fun experience.

    Receive parameters for argv -n size of board (defualt 8) -b number of boards (default idk)

    So we make b amount of n length boards all allocated randomly. 


    2) Now we score these board states using findDispute(). Rank the boards 
    (make an ranking array where 0th element holds address of best board? Not sure)
    We use genetic model where best performing model will have higher chance of reproduction

    Maybe I should do this in python :(


    3) We recurse this process until we get findDispute value of 0 (a solution?)
    Genetic Solution as far as I know isn't the optimal solution. I don't remember

    
    */


    return 0;
}