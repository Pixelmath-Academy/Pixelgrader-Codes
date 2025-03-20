#include <stdio.h>

void set_dice_face(char board[3][12],int start, int num) {
    if (num == 1) {
        board[1][start+1] = '*';
    } else if (num == 2) {
        board[1][start+2] = '*'; 
        board[1][start] = '*';
    } else if (num == 3) {
        board[0][start+1] = '*'; 
        board[1][start+1] = '*'; 
        board[2][start+1] = '*';
    } else if (num == 4) {
        board[0][start]= '*'; 
        board[0][start+2]= '*';
        board[2][start] = '*';
        board[2][start+2] = '*'; 
    } else if (num == 5) {
        board[0][start]= '*'; 
        board[0][start+2]= '*'; 
        board[1][start+1] = '*'; 
        board[2][start] = '*';   
        board[2][start+2] = '*'; 
    } else if (num == 6) {
        board[0][start] = '*';   
        board[0][start+2]= '*'; 
        board[1][start]= '*';  
        board[1][start+2] = '*'; 
        board[2][start]= '*'; 
        board[2][start+2] = '*';
    }
}

int main(){
    char board[3][12]; 
    int start[] ={0,4,8};
    int num;
    scanf("%d", &num);
    
    int h = num/ 100, t = (num % 100)/10, u = num% 10;  
    if (h > 6|| h < 1||t > 6 ||t < 1 || u > 6 || u < 1) {
        printf("error\n");
        return 0;
    }

    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 12; j++) {
            if (j == 3 || j == 7) {
                board[i][j] ='|';
            } else {
                board[i][j] = ' ';
            }
        }
    }

    set_dice_face(board,start[0],h);
    set_dice_face(board,start[1],t); 
    set_dice_face(board,start[2],u);

    for (int i = 0; i <3; i++) {
        for (int j = 0; j < 12; j++) {
            printf("%c",board[i][j]);
        }
        printf("\n");
    }

    return 0;
}