#include "lists.h"

/**
 * insert_node - inserts a node in a sorted linked list
 * @head: first node
 * @number: node value
 *
 * Return: new node, null if it fails
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp, *new_node;

	if (!head)
		return (NULL);

	new_node = malloc(sizeof(listint_t));

	if (!new_node)
		return (NULL);

	new_node->next = NULL;
	new_node->n = number;

	if (!*head || (*head)->n >= new_node->n)
	{
		new_node->next = *head;
		*head = new_node;
	}
	else
	{
		tmp = *head;
		while (tmp->next != NULL && tmp->next->n < new_node->n)
		{
			tmp = tmp->next;
		}
		new_node->next = tmp->next;
		tmp->next = new_node;
	}
	return (new_node);

}
