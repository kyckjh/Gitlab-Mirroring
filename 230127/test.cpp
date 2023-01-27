#include<stdio.h>
int main()
{
    int n;
    scanf("%d", &n);
    int sum = 0;
    int cnt = 1;
    while(sum < n)
    {
        sum += cnt;
        cnt++;
    }
    int sub = sum - n;
    if(cnt%2 == 0)
        printf("%d/%d", cnt - 1 - sub,  1 + sub);
    else
        printf("%d/%d",  1 + sub, cnt - 1 - sub);
}

// sum cnt n = 3
// 0   1
// 1   2
// 3   3    break -> sub = 0 -> (cnt - 1 - sub)/(1 + sub)
// 6   4
// 10  5
// 15  6
