import java.util.*;

class noofoccurrence
{
 public static void main(String args[])
 {
	 int arr[]={1,1,2,2,2,2,3,3};
	 Scanner sc=new Scanner(System.in);
	 System.out.println("enter no:");
	 int no=sc.nextInt();
	 int c=0;
	noofoccurrence ob=new noofoccurrence();
	
	System.out.println(ob.getlast(arr,no,0,arr.length)-ob.getfirst(arr,no,0,arr.length)+1);
	
	
	
 }
 
 public int getfirst(int arr[],int n,int l, int h)
 {
	 
		 int f=0;
		 int c=0;
		 		 if(l<=h)
		 {
		 int k=(l+h)/2;

		 if(arr[k]==n && (n>arr[k-1]|| k==0))
		 {
			return k;
		 }
		  else
		 {
			 if(arr[k]>n)
				 return getfirst(arr, n, l, k);
			 else
				 return getfirst(arr,n,k+1,h);
		 }
		 }
					 
			
return 0;
	 }
	
	
	public int getlast(int arr[],int n,int l, int h)
 {
	 
		if(l<=h)
		{
			 int k=(l+h)/2;
			 if(arr[k]==n && (n<arr[k+1]||k==(arr.length-1)))
			 {
				return k;
			 }
			  else
			 {
				 if(arr[k]>n)
					 return getlast(arr, n, l, k);
				 else
					 return getlast(arr,n,k+1,h);
			 }
					 
		}
return 0;		
			
	 }
	
	
 
 }
 
