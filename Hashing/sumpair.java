
import java.util.*;

class sumpair{
	public static void main(String args[])
	{
		int arr[]={1,3,7,5,4,11};
		int num=7;
		sumpair s=new sumpair();
		s.check(arr,num);
		
	}
	
	public void check(int arr[],int n)
	{
		HashMap<Integer,Integer> hm=new HashMap<Integer,Integer>();
		
		for(int i=0;i<arr.length;i++)
			hm.put(i,arr[i]);
		
		for(int i=0;i<arr.length;i++)
		{
			if(hm.containsValue(n-hm.get(i)))
			{
				System.out.println(+hm.get(i)+" "+(n-hm.get(i)));
				break;
		}
		}
	}
}