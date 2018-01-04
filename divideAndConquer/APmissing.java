class APmissing
{
	public static void main(String args[])
	{
		int arr[]={1,6,11,21,26,31,36};
		
		APmissing ob=new APmissing();
		
		System.out.println(ob.binary(arr,0,arr.length));
	}
	
	public int binary(int arr[],int l,int h)
	{
		int diff=arr[1]-arr[0];
		
		while(l<=h)
		{
			int k=(l+h)/2;
			if(arr[k+1]-arr[k]>diff)
				return arr[k+1]-diff;
			else
			{
				if(arr[k]>(1+(k*diff)))
					return binary(arr,0,k);
				else
					return binary(arr,k+1,arr.length);
			}
		}
		return -1;
		
	}
	
	
}