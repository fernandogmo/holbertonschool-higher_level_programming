#include <stdlib.h>
#include <stdio.h>
#include "lists.h"


int is_palindrome(listint_t **head)
{
	listint_t *curr = *head, *start = *head;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	return (is_palindrome_rec(&start, curr));
}

int is_palindrome_rec(listint_t **start, listint_t *curr)
{
	if (curr->next)
        {
		if (!is_palindrome_rec(start, curr->next))
			return (0);
		if ((*start)->n != curr->n)
			return (0);
		*start = (*start)->next;
	}
	else
	{
		if ((*start)->n != curr->n)
			return (0);
		*start = (*start)->next;
		return (1);
	}
	return (1);
}
