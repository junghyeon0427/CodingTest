#include <stdio.h>
void Kolakoski(int num, int arr[]);

int main()
{
    int testCase;
    scanf("%d", &testCase);
    for (int i=0; i<testCase; i++)
    {
        int num;
        int arr[1003];
        // 초기 테이블 arr
        arr[1] = 1;
        arr[2] = 2;
        arr[3] = 2;
        scanf("%d", &num);
        Kolakoski(num, arr);
    }
    return 0;
}

void Kolakoski(int num, int arr[])
{
    int count = 0;
    int i = 4;
    int j = 3;
    while (i <= num)
    {
        // 2를 채우는 경우
        if (count % 2 == 1)
        {   
            // 2를 2번 채우는 경우
            if (arr[j] == 2)
            {
                arr[i] = 2;
                arr[i+1] = 2;
                i += 2;
                j += 1;
            }
            // 2를 1번 채우는 경우
            else
            {
                arr[i] = 2;
                j += 1;
                i += 1;
            }
        }
        // 1을 채우는 경우
        else
        {
            // 1을 2번 채우는 경우
            if (arr[j] == 2)
            {
                arr[i] = 1;
                arr[i+1] = 1;
                i += 2;
                j += 1;
            }
            // 1을 1번 채우는 경우          
            else
            {
                arr[i] = 1;
                j += 1;
                i += 1;
            }
        }
        count++;
    }
    printf("%d\n", arr[num]);
}v
