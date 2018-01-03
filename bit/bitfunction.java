package bit;

public class bitfunction{
	public boolean getbit(int num, int i)
	{
		return((num&(1<<i))!=0);
	}

	public int setbit(int num,int i)
	{
		return(num|(1<<i));
	}
	
	public int clearbit(int num, int i)
	{
	return(num&(~(1<<i)));
	}
	
	
	
}