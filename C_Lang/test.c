#include<math.h>
#include<stdio.h>
#include<stdlib.h>

int R = 1000;
float C = 0.000047;
float V = 5;
float Vc,VR,I,five_t,t;
FILE *fp;

char count;
#define JUMP 0.006

const float e = 2.71828;
void RC_up(float);
void RC_down(float);
int main(){
    fp = fopen("test.txt","w+");
    t = R * C;
    five_t = 5 * t;    
    float i=0,j=0;
    while(1){//RC 充電
        RC_up(i);
        fprintf(fp,"%.3f,%.3f\n",i,Vc);
        if(Vc == V)count++;
        printf("time[%f] = Vc = %f | VR = %f | I = %f \n",i,Vc,VR,I);
        if(count >= 20)break;
        i = i+JUMP;
    }
    fclose(fp);
    fp = fopen("test2.txt","w+");
    count = 0;
    while(1){//RC 放電
        RC_down(j);
        fprintf(fp,"%.3f,%.3f\n",j,Vc);
        if(Vc == 0 || VR == 0 || I == 0)count++;
        printf("time[%f] = Vc = %f | VR = %f | I = %f \n",j,Vc,VR,I);
        if(count >= 20)break;
        j+=JUMP;
    }
    fclose(fp);
    return 1;
}

void RC_up(float i){
    float ls = pow(e,-(i/(R*C)));
    if(i <= 0){
        Vc=0;
        VR = V;
        I = V/R;
    }else if(i >= five_t){
        Vc = V;
        VR = 0;
        I = 0;
    }else{
        
        Vc = V * (1-ls);
        VR = V * ls;
        I = (V/R) * ls;
    }
}

void RC_down(float y){
    float ls = pow(e,-(y/(R*C)));
    if(y <= 0){
        Vc = V;
        VR = -V;
        I = -V/R;
    }else if(y >= five_t){
        Vc =0;
        VR = 0;
        I = 0;
        count+=1;
    }else{
        Vc = V* ls;
        VR = -V*ls;
        I = -(V/R)*ls;
    }
}