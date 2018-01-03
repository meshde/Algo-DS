import java.util.*;
import bit.*;

class arraydup
{
	public static void main(String args[])
	{
		
		int arr[]={5,5, 3, 5, 6, 3, 3};
		
bitfunction b=new bitfunction();
			int sum=0,r=0;
			
			int l=Integer.toBinaryString(arr[0]).length();
			System.out.println("hi"+l);
			
			for(int i=0;i<l;i++)
			{
			int count=0;
			for(int j=0;j<arr.length;j++)
			{
				count=count+b.getbit(arr[j],i);
			}
			if(count%3!=0)
				r=b.setbit(r,i);
			
			}
			
			
			System.out.println(r);
						
			
	
		
		
		
		
		
	}
}