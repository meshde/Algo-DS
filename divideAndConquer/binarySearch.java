import java.util.*;


class binarySearch{
public static void main(String args[])
{
	int arr[]={20,30, 40, 50, 60, 70, 80};
	binarySearch bs=new binarySearch();
	
	System.out.println(bs.search(arr,40,0,arr.length));
	
	
	
	
}


	public int search(int arr[],int n,int a,int b)
	{
		if(a<=b)
		{
		int key=(a+b)/2;
		if(arr[key]==n)
			return key;
		else
		{
			if(arr[key]>n)
				return search(arr, n, 0, key);
			else
				return search(arr,n, key, arr.length);
		}
		}
		return 0;
	}

}