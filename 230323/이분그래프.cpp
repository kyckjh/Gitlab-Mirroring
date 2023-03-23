#include <iostream>
using namespace std;

int visited[20001] = { 0 };
struct node
{
	int n;
	node* next;
};

struct graph
{
	int gV, gE;
	node *adjList[20001];
};

struct queue
{
	int front, rear, size;
	int elem[2000001];
};

void initGraph(graph *gp, int n, int m)
{
	gp->gV = n;
	gp->gE = m;
	for (int i = 0; i < 20001; i++) gp->adjList[i] = NULL;
}

void insertEdge(graph *gp, int from, int to)
{
	node *newNode = new node;
	newNode->n = to;
	newNode->next = gp->adjList[from];
	gp->adjList[from] = newNode;
}

void initqueue(queue *q)
{
	q->front = 0;
	q->rear = 0;
	q->size = 0;
	for (int i = 0; i < 2000001; i++) q->elem[i] = 0;
}

void enqueue(queue *q, int num)
{
	q->elem[q->rear++] = num;
	q->size++;
}

int dequeue(queue *q)
{
	int result = q->elem[q->front++];
	q->size--;
	return result;
}

bool bfs(graph* gp)
{
	queue q;
	initqueue(&q);
	enqueue(&q, 1);
	while (q.size != 0)
	{
		int v = dequeue(&q);


	}
	return true;
}

int main()
{
	int T;
	cin >> T;
	for (int t = 0; t < T; t++)
	{
		int V, E;
		cin >> V >> E;
		graph *G = new graph;
		for (int i = 0; i < E; i++)
		{
			int a, b;
			cin >> a >> b;
			insertEdge(G, a, b);
			insertEdge(G, b, a);
		}
		/*int** graph = new int*[V + 1];
		for (int i = 0; i < V + 1; i++) 
		{
			graph[i] = new int[V + 1];
		}
		for (int i = 0; i < V + 1; i++)
		{
			for (int j = 0; j < V + 1; j++)
			{
				graph[i][j] = 0;
			}
		}
		for (int i = 0; i < E; i++)
		{
			int a, b;
			cin >> a >> b;
			graph[a][b] = 1;
			graph[b][a] = 1;
		}*/
		if (bfs(G))
		{
			cout << "YES" << '\n';
		}
		else
		{
			cout << "NO" << '\n';
		}
		delete[] G;
	}
	return 0;
}