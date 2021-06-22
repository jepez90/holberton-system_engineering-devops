#include <unistd.h>
#include <stdio.h>

int infinite_while(void);


/**
 * main - prgogram that print operation with parameters pased for the user.
 *
 * Return: Always 0.
 */
int main(void)
{
	pid_t pid, i;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if (pid == 0)
		{
			return (0);
		}
		else
		{
			printf("Zombie process created, PID: %d\n", pid);
		}
	}
	return (infinite_while());
}


/**
 * infinite_while - function that geneerate an infinity loop
 *
 * Return: Always 0.
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
