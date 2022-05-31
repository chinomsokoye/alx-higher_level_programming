#include <unistd.h>
#include <stdlib.h>
#include "lists.h"
#include <string.h>
#include <stdio.h>

/**
 * insert_node - inserts number into sorted singly linked list
 * @head: pointer to node
 * @next: new node number
 * Return: new node or null
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *flow = *head;
	listint_t *new = NULL;
	listint_t *tmp = NULL;

	if (!head)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (!*head || (*head)->n > number)
	{
		new->next = *head;
		return (*head = new);
	}
	else
	{
		while (flow && flow->n < number)
		{
			tmp = flow;
			flow = flow->next;
		}
		tmp->next = new;
		new->next = flow;
	}
	return (new);
}
