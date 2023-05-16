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
	listint_t *slow = *head, *fast = *head, *temp = *head, *dup = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		fast = fast->next->next;
		if (!fast)
		{
			dup = slow->next;
			break;
		}
		if (!fast->next)
		{
			dup = slow->next->next;
			break;
		}
		slow = slow->next;
	}

	rev_linked(&dup);

	while (dup && temp)
	{
		if (temp->n == dup->n)
		{
			dup = dup->next;
			temp = temp->next;
		}
		else
			return (0);
	}

	if (!dup)
		return (1);
	return (0);
}
