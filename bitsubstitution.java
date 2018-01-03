//problem to sumbstitute M into N from i to j

import bit.*;

class bitsubstitution{
	public static void main(String args[])
	{
	bitfunction bf=new bitfunction();
	int N=1072, M=19;
	int i=2,j=6;
	System.out.println(Integer.toBinaryString(N));
		System.out.println(Integer.toBinaryString(M));
	for(int k=i;k<=j;k++)
	{
		N= bf.clearbit(N,k);
	}
	

	

	
	int mshift=M<<i;
	
	
	
	System.out.println(Integer.toBinaryString(N|mshift));
//	System.out.println(Integer.toBinaryString(N&(~temp)));
	
	
	
	
	}


}
