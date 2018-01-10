#include <stdio.h>
#include <stdlib.h>
#include <strings.h>

static int debug=1; 
#define DEBUG(ss) if (debug) printf ss

static void swap(int *a, int *b)
{
	int t;
	t=*a;
	*a=*b;
	*b=t;
}
void printArr(int arr[], int size, char *str)
{
	int i;

	printf("%s= ", str);
	for (i=0; i < size; i++)
		printf("%2d", arr[i]);
	printf("\n");
}



void buildHeap(int a[], int N)
{

	int p, l, r;
	int start, root;

	start=N-1;
	root = 0;
	DEBUG(("buildHeap->: n(%d) start(%d)\n",N, start));
	while (start > 1) {
		DEBUG(("."));
		root=a[0];
		// If Odd number then it is left node only
		// if even then right node, also left node exist
		if (start & 0x1){
			p=start>>1;
			l=start;
			r= start+1>N-1?start:start+1;
		} else {
			p=(start>>1) - 1;
			r = start;
			l = start-1;
		}
		
		if (a[p]<a[l])
			swap(&a[p], &a[l]);
		if (a[p]<a[r])
			swap(&a[p], &a[r]);
		
		if (root < a[p]) { //Keep going
			buildHeap(a, p+1);
		}
		start--;
	} //while
}


void heapSort(int a[], int N)
{
	int start, end, heapsize;
	int i,j,k;
	
	buildHeap(a, N);

	for (i=N-1; i>0; i--){
		swap(&a[0],&a[i]);
		heapsize=i;
		buildHeap(a, heapsize);
		DEBUG(("heap(%d) ",heapsize));
		printArr(a, N, "Inter= ");
	}	
}



void main()
{

	int arr[]={6,5,3,1,8,2,4};
	int tt[]={6,5,4};
	int size= sizeof(arr)/sizeof(int);
	
	printArr(tt,3,"tt");
	swap(&tt[0],&tt[2]);
	printArr(tt,3,"tt-swap");

	printArr(arr, size, "Original");
	heapSort(arr, size);
	printArr(arr, size, "Sorted");

}
