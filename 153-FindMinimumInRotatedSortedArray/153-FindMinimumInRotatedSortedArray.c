// Last Updated: 2/5/2026, 9:24:43 AM
int min_value(int a,int b)
{
    return (a<b?a:b);
}
int findMin(int* arr, int n) {
    int min_val=arr[0];
    int low=0;
    int high=n-1;
    int mid;
    while(low<=high)
    { 
            mid=low+(high-low)/2;
        if(arr[low]<=arr[mid])
        {
            min_val=min_value(min_val,arr[low]);
            low=mid+1;
        }
        else
        {
            min_val=min_value(min_val,arr[mid+1]);
            high=mid;
        }
    }
    return min_val;
    
}
