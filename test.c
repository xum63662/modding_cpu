#include<stdio.h>
#include<string.h>

FILE *fp;
    int i = 0;
int main(){
    fp = fopen("setting.cfg","r");
    char buf[100] = {0};
    if(fp == NULL) perror("Error");
    else{
        for(i= 0;i<4;i++){
            memset(buf, 0, sizeof(buf));
            fgets(buf, sizeof(buf), fp);
            printf("%s", buf);
        }
    }
    fclose(fp);


    return 0;
}