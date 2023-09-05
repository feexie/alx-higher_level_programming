#include "lists.h"
#include <stdlib.h>
#include <stddef.h>
#include <stdio.h>

/**
 * insert_node - inserts a number into a singly linked list
 * @head: list head node
 * @number: number to store in new node
 *
 * Return: address of the new node, NULL if it failed
 *
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *x;
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (0);
	new->n = number;
	x = *head;
	if (*head == NULL || number < x->n)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	while (x)
	{
		if (x->next == NULL)
		{
			x->next = new;
			new->next = NULL;
			return (new);
		}
		else if (number >= x->n && number <= x->next->n)
		{
			new->next = x->next;
			x->next = new;
			return (new);
		}
		x = x->next;
	}
	return (NULL);
}
