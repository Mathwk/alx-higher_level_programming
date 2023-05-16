#include "lists.h"

/**
 * rev_linked - singly linked list reversing
 * @head: pointer to linked list
 *
 * Return: pointer to the reversed linked list
 */
listint_t *rev_linked(listint_t **head)
{
	listint_t *node = *head;
	listint_t *next;
	listint_t *prev = NULL;

	while (node)
	{
		next = node->next;
		node->next = prev;
		prev = node;
		node = next;
	}
	*head = prev;
	return (*head);
}
/**
 * is_palindrome - palindrome checker
 * @head: pointer to the linked list
 *
 * Return: 1 if it is and 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp;
	listint_t *rev;
	listint_t *mid;
	size_t n, i;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	tmp = *head;
	for (n = 0; tmp; n++)
		tmp = tmp->next;

	tmp = *head;
	for (i = 0; i < (n / 2) - 1; i++)
		tmp = tmp->next;

	if ((n % 2) == 0 && tmp->n != tmp->next->n)
		return (0);

	tmp = tmp->next->next;
	rev = rev_linked(&tmp);
	mid = rev;

	tmp = *head;
	while (rev)
	{
		if (tmp->n != rev->n)
			return (0);
		tmp = tmp->next;
		rev = rev->next;
	}
	rev_linked(&mid);

	return (1);
}
