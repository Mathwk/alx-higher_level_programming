#include "lists.h"
/**
 * insert_node - inserts number at a node in assending order
 * @head: list to be altered
 * @number: number to be added
 * Return: pointer to node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node, *insert;

	insert = malloc(sizeof(listint_t));
	if (insert == NULL)
		return (NULL);
	insert->n = number;
	node = *head;
	if (node == NULL || node->n >= number)
	{
		insert->next = node;
		*head = insert;
		return (insert);
	}
	while (node && node->next && node->next->n < number)
		node = node->next;
	insert->next = node->next;
	node->next = insert;
	return (insert);
}
