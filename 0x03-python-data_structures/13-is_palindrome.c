#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - check if singly linked list is a palindrome
 * @head: point to linked list
 * Return: 0 or 1
 */

int is_palindrome(listint_t **head)
{
	int len = 0, i = 0;
	listint_t *temp;
	int sn[10000];

	temp = *head;
	if ((*head) == NULL)
		return (1);
	while (temp != NULL)
	{
		len++;
		temp = temp->next;
	}
	if (len == 1)
		return (1);
	temp = *head;
	while (temp != NULL)
	{
		sn[i] = temp->n;
		temp = temp->next;
		i++;
	}
	i = 0;
	while (i <= len / 2)
	{
		if (sn[i] != sn[len - i - 1])
			return (0);
		i++;
	}
	return (1);
}
