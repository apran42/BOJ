#include <stdio.h>
#include <string.h>

void recursion(const char *s, int l, int r, int cnt){
    if(l >= r) printf("%d %d\n", 1, cnt);
    else if(s[l] != s[r]) printf("%d %d\n", 0, cnt);
    else 
    {
        cnt++;
        return recursion(s, l+1, r-1, cnt);
    }
}

void isPalindrome(const char *s){
    int cnt=1;
    return recursion(s, 0, strlen(s)-1, cnt);

}

int main(){
    int n;
    scanf("%d", &n);
    for(int i=0; i<n; i++) {
        char a[1001];
        scanf("%s", a);
        isPalindrome(a);
    }
    return 0;
}