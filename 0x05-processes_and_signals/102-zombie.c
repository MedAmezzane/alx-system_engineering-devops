#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - creates an infinite loop to make the program hang
 * Return: always 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - creates 5 zombie processes
 * Return: always 0
 */
int main(void)
{
	int i;
	pid_t zombie;

	for (i = 0; i < 5; i++)
	{
		/*Create a zombie process*/
		zombie = fork();

		if (zombie == -1)
		{
			perror("fork");
			exit(EXIT_FAILURE);
		}

		if (!zombie)
			return (0);

		/*Print the PID of the zombie process*/
		printf("Zombie process created, PID: %d\n", zombie);
	}

	/*Enter an infinite loop to keep the program running*/
	infinite_while();

	return (0);
}
