# include <stdio.h>

int main(){
    int cnt = 0;
    for(int i = 0; i < 1000; i++){
        if(i % 3 == 0 || i % 5 == 0){
            cnt += i;
        }
    }
    printf("%d", cnt);
    return 0;
}