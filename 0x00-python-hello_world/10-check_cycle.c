#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked list to check
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
	listint_t current = list;
	listint_t next = list;

	if (!list)
		return (0);

	while (current && next && next->nxt)
	{
	current = current->nxt;
		fast = next->nxt->nxt;
		if (current == next)
			return (1);
	}

	return (0);
}
