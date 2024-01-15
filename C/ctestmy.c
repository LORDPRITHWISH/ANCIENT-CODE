#include <stdio.h>
int main()
{
	int a;
    float d;
    char ch;

	printf("Enter intiger: ");
	scanf("%d", &a);
	printf("Enter decimal: ");
	scanf("%f", &d);
    printf("Enter charecter: ");
	scanf("%c", &ch);

	printf("A : %d \n D : %f \n C : %c",
			a , d , ch);

	return 0;
}