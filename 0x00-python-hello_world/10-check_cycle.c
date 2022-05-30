#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - check if singly linked list has a cycle in it
 * @list: linked list
 * Return: 0 or 1
 */

int check_cycle(listint_t *list)
{
	listint_t *first_list, *second_list;

	first_list = list;
	second_list = list;
	while (first_list != NULL && second_list != NULL)
	{
		first_list = first_list->next;
		if (second_list->next)
			second_list = second_list->next->next;
		if (first_list == second_list)
			return (1);
	}
	return (0);
}
