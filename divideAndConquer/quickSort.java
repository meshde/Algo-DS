class quicksort
{
	public static void main(String args[])
	{
		int arr[]={70,60,50,40,30,20,10};
		
		quicksort s=new quicksort();
		s.sort(arr,0,arr.length-1);
		
		for(int i=0;i<arr.length;i++)
			System.out.println(arr[i]);
		
		
	}
	
	
	public int partition(int arr[], int l, int h)
	{
	
		int pivot=arr[h];
		int i=l-1;
		for(int j=l;j<h;j++)
		{
			if(arr[j]<=pivot)
			{
				i++;
				int temp=arr[i];
				arr[i]=arr[j];
				arr[j]=temp;
			}
		}
		
		
		
		int temp=arr[i+1];
		arr[i+1]=arr[h];
		arr[h]=temp;
		
		return i+1;
		
	}
	
	public void sort(int arr[],int l, int h)
	{
		if(l<h)
		{
			int p=partition(arr,l,h);
		sort(arr,l,p-1);
		sort(arr,p+1,h);
		}
		
		
		
	}
	
}