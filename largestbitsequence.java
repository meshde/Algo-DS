// Given a number n, find the largest sequence of 1s after flipping a bit to 1.
import bit.*;

class largestbitsequence
{
public static void main(String args[])
{
	int n=1775;
	bitfunction bf=new bitfunction();
	int c=0;
	
	int l=Integer.toBinaryString(n).length();
	System.out.println(Integer.toBinaryString(n));
	
	int i=0,curr=0,prev=0;
	int max=1;
	while(i<l)
	{
		if(bf.getbit(n,i)==1)
			curr++;
		else
		{
			if(bf.getbit(n,i+1)%2==0){
			}
			else{
				prev=curr;
				curr=0;
			}
		}
		
		if(max<(curr+prev+1))
			max=curr+prev+1;
		
		i++;
		
		
	}
	
	
	System.out.println(max);
	

}
}