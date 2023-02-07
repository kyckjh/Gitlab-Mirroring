#include<stdio.h>
int main()
{
    int K, N;
    scanf("%d %d", &K, &N);
    long long lines[10001] = { 0, };
    for (int k = 0; k < K; k++)
    {
        scanf("%d", &lines[k]);
    }
    long long max = 0;
    for (int k = 0; k < K; k++)
    {
        if (max < lines[k])
            max = lines[k];
    }
    long long sum = 0;
    long long tmm = 1;
    long long tmm2 = max;
    long long mid = (tmm + tmm2) / 2;
    while (tmm < tmm2)
    {
        sum = 0;
        for (int i = 0; i < K; i++)
        {
            sum += lines[i] / mid;
        }
        if (sum >= N)
        {
            tmm = mid+1;
        }
        else
        {
            tmm2 = mid-1;
        }
        mid = (tmm + tmm2) / 2;
    }
    sum = 0;
    for (int i = 0; i < K; i++)
    {
        sum += lines[i] / mid;
    }
    if (sum >= N)
    {
        printf("%d", mid);
    }
    else
    {
        printf("%d", mid - 1);
    }
    return 0;
}