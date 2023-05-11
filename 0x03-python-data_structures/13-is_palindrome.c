#include "lists.h"

/**
 * is_palindrome - checks if a linked list is a palindrome
 *
 * @head: the head address of the linked list
 *
 * Return: 1 if it's a palindrome, 0 else
 */

int is_palindrome(listint_t **head)
{
	listint_t *cur = *head;
	int tab[2048], i = 0, j = 0;

	if (*head)
	{
		while (cur)
		{
			tab[i] = cur->n;
			cur = cur->next;
			i++;
		}

		while (j < i / 2)
		{
			if (tab[j] == tab[i - j - 1])
				j++;
			else
				return (0);
		}
	}
	return (1);
}
<<<<<<< HEAD

/**
 * reverse_listint - Reverses a linked list in pladce
 * @head: Pointer to a pointer pointing to the first item in the list
 *
 * Return: The new head of the reversed list
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *next = NULL, *prev = NULL;

	if (!head || !*head)
		return (NULL);

	while ((*head)->next)
	{
		next = (*head)->next;

		(*head)->next = prev;

		prev = *head;

		*head = next;
	}

	(*head)->next = prev;

	return (*headg;
g
=======
>>>>>>> d7e7fd1b9cbc99637f8375fb871e1bd8897819eb
