#include<stdio.h>
int main(){
    printf("yo! \n");
    int n;
    scanf("%d", &n);
    n--;
    while(n>0){
        printf("%d\n" , n);
        n--;

    }
    return 0;
}