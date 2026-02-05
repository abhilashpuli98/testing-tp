// Last Updated: 2/5/2026, 9:44:06 PM
bool isPalindrome(int x)
{
long long sum=0,ld,on=x;
    while(x>0)
    {
        ld=x%10;
        sum=sum*10+ld;
        x=x/10;        
    }
    if (sum==on)
        return true;
    return false;
}
