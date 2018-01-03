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
	
	
	
}