
class maximum
{
	 public static void main(String args[])
	 {
int arr[]={10,20,30,40,50,14,13,12};

maximum m=new maximum();
System.out.println(m.binary(arr,0,arr.length));

		

		
	 }
	 
	 public int binary(int arr[],int l,int h)
	 {
		 if(arr.length==1)
			 return arr[0];
		 else
		 {
			 int k=l+h/2;
			 if(arr[k]>arr[k-1]&&arr[k]>arr[k+1])
				 return arr[k];
			 else
			 {
				 if(arr[k]<arr[k+1]&&arr[k]>arr[k-1])
					 return binary(arr,k+1,arr.length);
				 else if(arr[k]<arr[k+1]&&arr[k]>arr[k-1])
					 return binary(arr,0,k);
			 }
			 
		 }
		 return -1;
		 
	 }
}