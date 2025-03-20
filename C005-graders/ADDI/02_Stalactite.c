#include <stdio.h>

int max=0, sum=0;
void put(char board[max][2*(sum)], int start, int num);

int main(){
    int q, k;
    scanf("%d", &q);
    int start[q+1]; start[0] = 0;
    int nums[q];
    for(int i=0; i<q; i++ ){
        scanf("%d", &k);
        start[i+1] = start[i]+2*k;
        nums[i] = k;
        if(k>max) max = k;
        sum += k;
    }
    char board[max][2*(sum)];

    for(int i=0; i<max;i++){
        for(int j=0; j<2*sum; j++){
            board[i][j] = ' ';
        }
    }

    for(int i=0; i<q; i++){
        put(board, start[i], nums[i]);
    }
    
    for(int i=0; i<max;i++){
        for(int j=0; j<2*sum; j++){
            printf("%c", board[i][j]);
        }
        printf("\n");
    }
    return 0;
}

void put(char board[max][2*(sum)], int start, int num){
    for(int i=1; i<=num; i++){
        for(int j=1; j<=2*num; j++){
            if(i==j) board[i-1][j+start-1] = '\\';
            if(i+j == 2*num+1 && i<j) board[i-1][j+start-1] = '/';
        }
    }
}