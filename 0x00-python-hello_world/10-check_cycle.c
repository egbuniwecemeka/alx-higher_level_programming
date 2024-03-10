#include "lists.h"

/**
 * check_cycle - checks if a listint_t list is a cycle
 * @list: the list to check
 *
 * Return: 1 if it is a circle, otherwise 0
 */
int check_cycle(listint_t *list)
{
	listint_t *first = list;
	listint_t *last = list;

	if (!list)
		return (0);

	while (first && last && last->next)
	{
		first = first->next;
		last = last->next->next;

		if (first == last)
			return (1);
	}

	return (0);
}
