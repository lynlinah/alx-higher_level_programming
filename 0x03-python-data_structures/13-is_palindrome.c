/*
 * File: 13-is_palindrome.c
 * Auth: Carolina
 */

#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

typedef struct listint {
    int n;
    struct listint *next;
} listint_t;

int is_palindrome(listint_t **head)
{
	if (*head == NULL) 
	{
		return (1); // Empty list is considered a palindrome
	}

	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev = NULL;
	listint_t *temp;

	while (fast != NULL && fast->next != NULL) 
	{
		fast = fast->next->next;
		temp = slow;
		slow = slow->next;
		temp->next = prev;
		prev = temp;
	}

	if (fast != NULL) { // Odd number of nodes
	slow = slow->next;
	}

	while (slow != NULL && prev != NULL) 
	{
		if (slow->n != prev->n) 
		{
			return 0; // Not a palindrome
		}
		slow = slow->next;
		prev = prev->next;
	}

	return 1; // Palindrome
}

int main()
{
	listint_t *head = NULL;

	// Create a palindrome list: 1 -> 2 -> 3 -> 2 -> 1
	head = malloc(sizeof(listint_t));
	head->n = 1;
	
	listint_t *second = malloc(sizeof(listint_t));
	second->n = 2;
	head->next = second;
	
	listint_t *third = malloc(sizeof(listint_t));
	third->n = 3;
	second->next = third;
	
	listint_t *fourth = malloc(sizeof(listint_t));
	fourth->n = 2;
	third->next = fourth;
	
	listint_t *fifth = malloc(sizeof(listint_t));
	fifth->n = 1;
	fourth->next = fifth;
	fifth->next = NULL;

	int result = is_palindrome(&head);
	printf("Is the list a palindrome? %d\n", result); // Output: Is the list a palindrome? 1 (True)

	// Free the memory
	while (head != NULL) 
	{
	listint_t *temp = head;
	head = head->next;
	free(temp);
	}

	return 0;
}
