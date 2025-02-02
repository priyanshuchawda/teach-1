#include<stdio.h>
int main(){
    float num1 , num2;
    int case1;
    scanf("%f", &num1);
    scanf("%f", &num2);
    scanf("%d", &case1);

    switch(case1){
        case 1:
            printf("%f" , num1+num2 ,"\n");
            break;
        case 2:
            printf("%f" , num1-num2 ,"\n");
            break;
    }
    return 0;
}