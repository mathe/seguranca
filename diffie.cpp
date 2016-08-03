#include <stdio.h>
#include <stdlib.h>

typedef long long int ll;

const ll M = 1000000007LL;
const ll B = 1009LL;

ll explog(ll base,ll exp){
    if(!exp) return 1LL;
    if(exp & 1LL) return explog(base,exp-1LL)*base%M;
    ll a = explog(base,exp >> 1LL);
    return (a*a)%M;
}   

ll bob(ll b,ll ca){
    return explog(ca,b);
}

ll alice(ll a,ll cb){
    return explog(cb,a);
}

void diffie(ll a,ll b){
    printf("Chave utilizada por Bob:%lld\n",bob(b,explog(B,a)));
    printf("Chave utilizada por Alice:%lld\n",alice(a,explog(B,b)));
}

int main(void){
    ll Alice,Bob;
    printf("Insira a chave de Alice:\n");
    scanf("%lld",&Alice);
    printf("Insira a chave de Bob:\n");
    scanf("%lld",&Bob);
    diffie(Alice,Bob);    
    return 0;
}
