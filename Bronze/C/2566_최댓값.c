#include <stdio.h>

int main() {
  int arr[9][9];
  int m=0, n=0, chk=0;
  for(int i=0; i<9; i++)
    for(int j=0; j<9; j++)
      {
        scanf("%d", &arr[i][j]);
      }
  for(int i=0; i<9; i++)
    for(int j=0; j<9; j++)
      {
        if(arr[i][j]>=chk)
        {
          chk=arr[i][j];
          m=i+1;
          n=j+1;
        }
      }
  
  printf("%d\n", chk);
  printf("%d %d", m, n);
  return 0;
}
  