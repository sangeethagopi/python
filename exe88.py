#include<stdio.h>
int main()
{
    int n,k,a[100],i,sum=0;
    scanf("%d\t%d",&n,&k);
    for(i=0;i<n;i++)
        scanf("%d",&a[i]);
    for(i=0;i<k;i++)
        sum=sum+k[i];
    printf("%d",sum);
}
