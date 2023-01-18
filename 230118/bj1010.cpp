#include <iostream>
using namespace std;

int bridge(int* N, int* M, int D, int pre)
{
	if (D + 1 == *N) 
	{
		return *M - pre;
	}
	int sum = 0;
	for (int i = pre + 1; i <= *M - *N + D + 1; i++)
	{
		sum += bridge(N, M, D + 1, i);
	}

	return sum;
}

int main()
{
	int T, N, M;
	cin >> T;
	for (int t = 1; t <= T; t++)
	{
		cin >> N >> M;
		int result = 0;
		if (N == 1) result = M;
		else
		{
			for (int i = 1; i <= M - N + 1; i++)
				result += bridge(&N, &M, 1, i);
		}
		cout << result << endl;
	}
	return 0;
}