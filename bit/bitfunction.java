package bit;

public class bitfunction{
	public int getbit(int num, int i)
	{
		if((num&(1<<i))!=0)
		return 1;
	else
		return 0;
			}

	public int setbit(int num,int i)
	{
		return(num|(1<<i));
	}
	
	public int clearbit(int num, int i)
	{
	return(num&(~(1<<i)));
	}
	
	public int countsetbits(int n)
	{
		int c=0;
		while(n>0)
		{
			n= n&(n-1);
			c++;
		}
		return c;
	}
	
	
	
}