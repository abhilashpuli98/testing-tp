// Last Updated: 2/5/2026, 9:40:32 PM
bool isValid(char* s) {
    char stack[strlen(s)];
    int top=-1;
    for(int i=0;s[i]!='\0';i++)
    {
        if(s[i]=='('||s[i]=='['||s[i]=='{')
        {
            stack[++top]=s[i];
        }
        else {
            if (top == -1 || (s[i] == ')' && stack[top] != '(') || (s[i] == '}' && stack[top] != '{') ||(s[i] == ']' && stack[top] != '[')) {
                return false;
            }
            top--;
        }
    }
    return top == -1;
}

