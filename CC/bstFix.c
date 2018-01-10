#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

/*
 *  subtree(List):
 *    // The base Case
 *    if Len(list) == 1:
 *      create Node with NULL left and right
 *      return node
 *    else:
 *       root = Create Node(List[1])
 *       Left-List = CreateLeftList(List[1].val, List)
 *       root->left = subtree(Left.list)
 *       Right-List = CreateLeftList(List[1].val, List)
 *       root->right = subtree(Left.list)
 *       return (root)
 *
 */

struct tnode {
  int data;
  struct tnode *left;
  struct tnode *right;
}tnode;


struct tnode *newNode(int v)
{
  struct tnode *t;

  t = malloc(sizeof (struct tnode));
  if (t) {
    memset(t, 0, sizeof(*t));
    t->data = v;
  }
  printf("====>>NODE:(%p) %2d\n", t, t->data);
  return (t);
}

void printNode(struct tnode *t)
{
    printf("%2d ", t->data);
}


struct stack {
  struct tnode *st[1000];
  int n;
  struct tnode **sp;
}stack;

void initStack()
{
  stack.n = 0;
  stack.sp = stack.st;
}

void push (struct tnode *x)
{
  *stack.sp =x;
  stack.sp++;
  stack.n++;

}

void *Peek()
{
  if (stack.n == 0)
    return NULL;
  return (*(stack.sp-1));
}

void *pop()
{
  struct tnode *x;

  if (stack.n == 0)
    return NULL;
  (stack.sp)--;
  x = *(stack.sp);
  (stack.n)--;
  return(x);
}

void printStack()
{
  int i;
   printf("S:: ");
  for (i=stack.n; i > 0 ; i--) {
    struct tnode *t;
    t = stack.st[i-1];
    printNode(t);
  }
}

bool isStackEmpty()
{
  if (stack.n == 0) return true;
  else return false;
}


/*
 * Inorder Left-->> :: Root:: -->>Right
 * */
void inorder(struct tnode *t)
{
  if (t == NULL)
    return;
  inorder(t->left);
  printf(" %2d", t->data);
  inorder(t->right);
}



/*
 *  Pre: Root-->>Left-->>right
 */
void preorder(struct tnode *t)
{
  if (t == NULL)
    return;

  printf(" %2d", t->data);
  preorder(t->left);
  preorder(t->right);
}

void postorder(struct tnode *t)
{
  if (t == NULL)
    return;
  postorder(t->left);
  postorder(t->right);
  printf(" %2d", t->data);
}

struct tnode *
bstInsert(struct tnode *root, struct tnode *t)
{
  struct tnode *n, *curr = root;
  
  while (curr) {
    if (t->data < curr->data) 
      n = curr->left;
    else 
      n = curr->right;
    if (n) {
      curr =n;
    }else {
      break; // found the place to insert
    }
  }

  if (t->data < curr->data) {
    curr->left = t;
  } else {
    curr->right = t;
  }
  return (curr);
}

void bstorder(struct tnode *root)
{
  struct tnode *t, *prev, *curr, *p;

  curr = root;
  //while (isStackEmpty() != false) {
  do{
    if (curr) {
      push(curr);
      //printStack();
      curr = curr->left;
    } else { // reached left end
      printf("Reached L/R end\n");
      curr = pop();
      p = Peek();
      if ( prev && (curr->data < prev->data)) {
        printf("(%p)->data (%2d) prev(%p)->data(%2d)is in wrong place\n", 
              curr,curr->data, prev, prev->data);
        if (p) 
          printf("Parent(%p)->data(%2d) is in wrong place\n", p, p->data);
      }
      //printStack();
      printNode(curr);
      prev = curr;
      //Lets visit right side
      curr = curr->right;
    }
  //}
  }while (!isStackEmpty()|| curr) ;

}


int ta[] = {30, 50, 20, 35, 55};

int main() {

  int i;
  struct tnode *root, *n, *t, *t1, *t2, *tbad;

  initStack();

  root = newNode(40);


  for (i=0; i < (sizeof(ta)/sizeof(int)); i++) {
    t= newNode(ta[i]);
    if (t->data == 50)
      t1 = t;
    bstInsert(root, t);
    //introduce error
    if (t->data == 35) t2 = t;
  }
  t1->left = t2;

  printf("\n====\n"); 
  inorder(root);
  printf("\n====\n"); 
  bstorder(root);
  printf("\n====\n"); 

}


