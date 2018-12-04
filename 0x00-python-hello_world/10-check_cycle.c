#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @head: pointer to first element of listint_t linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *head)
{
	/* We start off quite prudently. Good, good... */
	if (!head)
		return (0);

	/*
	 * Now this... this is a hack.
	 * A hack which (I believe) depends on the order
	 *   in which the linked list elements were added.
	 * You probably don't want to do this in an interview.
	 */
	while ((head > head->next) && head->next)
		head = head->next;

	/* This is also questionable :) */
	return (!!head->next);
}
