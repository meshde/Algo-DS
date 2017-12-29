import minheap.*;
import java.util.*;
class rope
{
	public static void main(String args[])
	{
		Scanner sc=new Scanner(System.in);
		System.out.println("enter the no of ropes");
		int n=sc.nextInt();
		binaryheap bh=new binaryheap();
		rope r=new rope();
		System.out.println("Enter length of each rope");
		for(int i=0;i<n;i++)
		{
			int l=sc.nextInt();
			bh.insert(binaryheap.heaparr,l);
		}
		
		//bh.display(binaryheap.heaparr);
	int sum=0;
		while(r.size(binaryheap.heaparr)!=1)
		{
			int a=binaryheap.heaparr[0];
			bh.delete(binaryheap.heaparr);
			int b= binaryheap.heaparr[0];
			bh.delete(binaryheap.heaparr);
			
			sum=+(a+b);
			bh.insert(binaryheap.heaparr,sum);
		}
	System.out.println("minimum length"+binaryheap.heaparr[0]);
	
	}
	
	public int size(int arr[])
	{
		int i=0;
		while(arr[i]!=0)
		{
			i++;
		}
			return i;
	}

}
