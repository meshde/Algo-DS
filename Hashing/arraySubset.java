import java.util.*;
class arraySubset
{
 public static void main(String args[])
 {
	 int arr1[]={1,3,2,11,5,7};
	 int arr2[]={3,1,7};
	 
arraySubset as=new arraySubset();
	int r=as.check(arr1,arr2);
	 if(r==1)
	System.out.println("it is a subset");
else
	System.out.println("Not a subset");
	 
	 }
	 
	 public int check(int arr1[],int arr2[])
	 {
		// int arr=new int[arr1.length];
		 
		 HashMap<Integer,Integer> hm=new HashMap<Integer,Integer>();
		 for(int i=0;i<arr1.length;i++)
		 hm.put(i,arr1[i]);
	 
	 
		 for(int i=0;i<arr2.length;i++)
		 {
			 if(!hm.containsValue(arr2[i]))
				 return 0;
		 }
		 return 1;
		 
	 }
	 
}