
//import for Scanner and other utility classes
import java.util.*;
import maxheap.*;

// Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail

class klarge {
    public static void main(String args[] ) throws Exception {
      
	  binaryHeap bh=new binaryHeap();
	  Scanner sc=new Scanner(System.in);
	  
	  System.out.println("enter no of elements in array");
	  int n=sc.nextInt();
	
	  
	  System.out.println("Enter the elements:");
	  for(int i=0;i<n;i++)
	  {
		  bh.insert(binaryHeap.heaparr);
	  }
	  
	  
	  
	  System.out.println("Enter k:");
	  int k=sc.nextInt();
	  
	  
	  for(int i=0;i<k;i++)
	  {
		  int max=binaryHeap.heaparr[0];
		  System.out.println(max);
		  bh.delete(binaryHeap.heaparr);
	  }
	  


    }
}
