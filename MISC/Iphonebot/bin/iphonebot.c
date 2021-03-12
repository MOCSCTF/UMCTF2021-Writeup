#include <stdio.h>
#include <unistd.h>

int main(void) {
  int choice, Iphones=5;
  long donation=0;
  setvbuf(stdout,NULL,2,0);
  setvbuf(stdin,NULL,2,0);
  printf("Welcome to IphoneBot!\n");
  for (int i=0;i<50;i++) {
    printf("You currently have %d Iphones.\n", Iphones);
    printf("Choices:\n");
    printf("\t1. Work\n");
    printf("\t2. Donate Iphones to the IphoneBot developers\n");
    printf("\t3. Buy flag(853853853 Iphones)\n");
    printf("\t4. Exit\n");
    printf("> ");
    scanf("%d", &choice);

    if (choice == 1) { 
      Iphones++;
      printf("You earned 1 Iphone! Nice work! Only %d more to go!\n", 853853853-Iphones);
      sleep(1);
    }
    else if (choice == 2) {
      printf("How many Iphone would you like to donate to the developers? ");
      scanf("%ld", &donation);
      if (donation > 0) {
        printf("Thanks for your donation!\n");
        Iphones -= donation;
      }
      else {
        printf("not negative....\n");
      }
    }
    else if (choice == 3) {
      if (Iphones > 853853853) {
        FILE *fp;
        char buff[255];
        fp = fopen("flag.txt", "r");
        fscanf(fp, "%s", buff);
        printf("Your flag is: %s\n", buff);
        break;
      }
      else {
        printf("You don't have enough Iphones!\n");
      }
    }
    else if (choice == 4) {
      printf("Bye!\n");
      break;
    }
    else {
      break;
    }
  }
  return 0;
}