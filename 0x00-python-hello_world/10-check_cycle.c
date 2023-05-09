#include "lists.h"
/**
 * check_cycle - checks if there is a cycle in list
 * @list: sigly linked list
 * Return: 1 if there is a cycle, else 0
 */
int check_cycle(listint_t *list)
{
	listint_t *a = list, *b = list;

	if (!list)
		return (0);
	while (a && b && b->next)
	{
		a = a->next;
		b = b->next->next;
		if (a == b)
			return (1);
	}
	return (0);
}
