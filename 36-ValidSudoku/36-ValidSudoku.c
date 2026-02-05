// Last Updated: 2/5/2026, 9:26:01 AM
bool isvalid(char **a,int row,int col,char val)
{
int count1=0,count2=0,count3=0,sri,sci;
for(int i=0;i<=8;i++)
{
if(a[row][i]==val)
count1++;
if(a[i][col]==val)
count2++;
}
sri=row-row%3;
sci=col-col%3;
for(int i=sri;i<=sri+2;i++)
{
for(int j=sci;j<=sci+2;j++)
{
if(a[i][j]==val)
count3++;
}
}
if(count1==1 && count2==1 && count3==1)
return true;
return false;
}

bool isValidSudoku(char** a, int boardSize, int* boardColSize)
{
    for(int i=0;i<=8;i++)
    {
         for(int j=0;j<=8;j++)
         {
            if(a[i][j]>='1' && a[i][j]<='9')
            {
                if(!isvalid(a,i,j,a[i][j]))
                return false;
            }
        

         }
    }
    return true;

}