#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>
/**
 * struct node - singly linked list
 * @value: the integer
 * @next: the next node points
 * Description: node structure for the singly linked list
 */
typedef struct node
{
	int value;
	struct node *next;
} node;

typedef node listint_t;

void print_listint(const node *h);
listint_t add_nodeint(listint_t *head, const int n);
void free_listint(listint_t head);
int check_cycle(listint_t list);

#endif /* LISTS_H */
