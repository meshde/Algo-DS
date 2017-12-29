/* Save this in a file called Main.java to compile and test it */
package maxheap;
import java.util.*;
import java.io.*;

public class binaryHeap {
	
	public static int heaparr[]=new int[100];
	
	public static void main(String args[])
	{
		
		Scanner sc=new Scanner(System.in);

	 binaryHeap bh=new binaryHeap();
	int op;
	do
	{
	 System.out.println("Choose:");
	 System.out.println("1. insert");
	  System.out.println("2. Display");
	    System.out.println("3. Delete");
		System.out.println("4. Sort");
		
	 op=sc.nextInt();
	 switch(op)
	 {
	 case 1:
	 bh.insert(heaparr);
	break;
	case 2:
	
	 bh.display(heaparr);
	break;
	case 3:  delete(heaparr);
	break;
	case 4:  bh.sort(heaparr);
	break;
	}
	}while(op!=5);
	}
	
	
	public void insert(int arr[])
	{
		Scanner sc=new Scanner(System.in);

		System.out.println("enter an element to insert");
		int newe=sc.nextInt();
		int pos=0;
		int i=0,n;
		while(arr[i]!= 0)
		{
			i++;
		}
		n=i;
		
		
		if(n==0)
		{
				arr[pos]=newe;
		}
		else
		{
		
	n=n+1;
		 pos=n;
		arr[pos-1]=newe;
		int temp;
		
		
		while(pos-1>0)
		{
			int par=pos/2;
			if(arr[pos-1]<=arr[par-1])
				return;
			else
			{
				temp=arr[pos-1];
				arr[pos-1]=arr[par-1];
				arr[par-1]=temp;
				
			}
			pos=par;
		}
		}
		
	}
	
	
	public static void delete(int arr[])
	{
		
		int i=0,n;
		while(arr[i]!= 0)
		{
			i++;
		}
		if(i==1)
		{
			arr[0]=0;
		}
		n=i-1;
		
		int ptr=1,left=2,right=3;
		
		
		
		int last=arr[n];
		arr[n]=0;
		n=n-1;
		arr[ptr-1]=last;
		
		while(left<=n)
		{
			int temp;
			if(arr[ptr-1]>=arr[left-1] && arr[ptr-1]>arr[right-1])
			{
				return;
			}
			if(arr[left-1]>=arr[right-1] && arr[right-1]!=0)
			{
				temp=arr[left-1];
				arr[left-1]=arr[ptr-1];
				arr[ptr-1]=temp;
				ptr=left;
			}
			else if(arr[left-1]<=arr[right-1] && arr[left-1]!=0){
				temp=arr[right-1];
				arr[right-1]=arr[ptr-1];
				arr[ptr-1]=temp;
				ptr=right;
			}
			
			left=2*ptr;
			right=left +1;
			
		}
		
		
		
	}
	
	
	public void sort(int arr[])
	{
		
		int root;
		int i=0;
		while(arr[i]!=0)
		{
			
			i++;
		}
		int a[]=new int[i];
		
		int j=i-1;
		while(j>=0)
		{
			root=arr[0];
			a[j]=root;
			j--;
			delete(arr);
		}
		
		for(int k=0;k<i;k++)
			System.out.println(a[k]);
	}
	
	
	
	public void display(int arr[])
	{
		int i=0;
		while(arr[i]!=0)
		{
			System.out.println("HEAP["+(i+1)+"]"+arr[i]);
			i++;
		}
	}
	
	
	
	
   
}
