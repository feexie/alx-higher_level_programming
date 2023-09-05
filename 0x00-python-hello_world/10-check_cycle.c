#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 *
 * @list: list to check
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 *
 */
int check_cycle(listint_t *list)
{
	listint_t *x;

	if (list == NULL)
		return (0);
	while (list)
	{
		x = list;
		list = list->next;
		if (x <= list)
			return (1);
	}
	return (0);
}
