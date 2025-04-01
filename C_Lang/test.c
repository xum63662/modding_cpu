#include<math.h>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

double R = 1000;
double C = 0.000047;
double V = 5;
double L = 0;
float X  = 0;
double Vc,VR,I,five_t,t;
FILE *fp;
FILE *cfg;

char count;
#define JUMP 0.000001

const float e = 2.71828;
void RC_up(double);
void RC_down(float);


double get_line(FILE *file){
    char buf[50] = {0};
    memset(buf, 0, sizeof(buf));
    fgets(buf, sizeof(buf), file);
    double temp = atof(buf);
    printf("%.9f\n",temp);
    return temp;
}



int main(int argc,char *argv[]){
    char buff[70] = {0};
    char buff1[70] = {0};
    memset(buff, 0, sizeof(buff));
    memset(buff1, 0, sizeof(buff1));
    strcat(buff,argv[1]);
    strcat(buff,"\\");
    printf("%s\n",buff);
    strcpy(buff1,buff);
    strcat(buff1,"setting.cfg");
    cfg = fopen(buff1,"r+");
    char buf[100] = {0};
    if(cfg == NULL) perror("Error");
    else{
        R = get_line(cfg);
        C = get_line(cfg);
        L = get_line(cfg);
        V = get_line(cfg);
    }
    fclose(cfg);
    strcpy(buff1,buff);
    strcat(buff1,"C_Lang\\test.txt");
    fp = fopen(buff1,"w+");
    t = R * C;
    five_t = 5 * t;    
    double i=0,j=0;
    printf("RxC=t\n%fx%f=%f\n",R,C,five_t);
    while(1){//RC 充電
        RC_up(i);
        fprintf(fp,"%.12f,%.12f\n",i,Vc);
        if(Vc == V)count++;
        printf("time[%f] = Vc = %f | VR = %f | I = %f \n",i,Vc,VR,I);
        if(count >= 20)break;
        i = i+JUMP;
    }
    fclose(fp);
    strcpy(buff1,buff);
    strcat(buff1,"C_Lang\\test2.txt");
    fp = fopen(buff1,"w+");
    count = 0;
    while(1){//RC 放電
        RC_down(j);
        fprintf(fp,"%.12f,%.12f\n",j,Vc);
        if(Vc == 0 || VR == 0 || I == 0)count++;
        printf("time[%f] = Vc = %f | VR = %f | I = %f \n",j,Vc,VR,I);
        if(count >= 20)break;
        j+=JUMP;
    }
    fclose(fp);
    return 1;
}

void RC_up(double i){
    double ls = pow(e,-(i/(R*C)));
    if(i <= JUMP){
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