#define _CRT_SECURE_NO_WARNINGS

#include<stdio.h>

struct Card
{
	int num;
	Card* up;
	Card* down;
};

int main()
{
	int N;
	scanf("%d", &N);
	if (N == 1)
	{
		printf("%d", 1);
	}
	else
	{
		Card cards[1001];
		Card head, tail;
		head.num = 0;
		head.up = NULL;
		head.down = &cards[0];

		tail.num = 0;
		tail.up = &cards[N - 1];
		tail.down = NULL;

		cards[0].num = 1;
		cards[0].up = &head;
		cards[0].down = &cards[1];
		for (int i = 1; i < N - 1; i++)
		{
			cards[i].num = i + 1;
			cards[i].up = &cards[i - 1];
			cards[i].down = &cards[i + 1];
		}
		cards[N - 1].num = N;
		cards[N - 1].up = &cards[N - 2];
		cards[N - 1].down = &tail;

		int trash[1001];
		int last;
		for (int i = 0; i < N; i++)
		{
			// 맨 아래 카드의 위가 top이면 break
			if (tail.up->up == &head)
			{
				last = (*tail.up).num;
				break;
			}
			// 맨 위 카드 버리기		head 1 2 3
			trash[i] = (*head.down).num;	// 1의 숫자를 trash에 넣기
			Card* nextTop = (*head.down).down;	// 2를 nextTop에 넣기
			(*nextTop).down = head.down->down->down;	// 2의 down을 3으로 설정
			head.down = nextTop;	// head의 down을 2로 설정
			(*nextTop).up = &head;		// 2의 up을 head로 설정
			// 다음 맨 위 카드 맨 아래로 보내기
			head.down = (*nextTop).down;
			(*(*nextTop).down).up = &head;

			(*nextTop).up = tail.up;
			tail.up = nextTop;
			(*(*nextTop).up).down = nextTop;
			(*nextTop).down = &tail;
		}
		for (int i = 0; i < N - 1; i++)
		{
			printf("%d ", trash[i]);
		}
		printf("%d", last);
	}
}