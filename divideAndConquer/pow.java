
import java.util.*;

class pow{

public static void main(String args[])
{
Scanner sc=new Scanner(System.in);
pow p=new pow();
System.out.println("enter no");
int no=sc.nextInt();
int x=sc.nextInt();
System.out.println(p.power(no,x));

}

public int power(int n, int x)
{
	if(x==0)
		return 1;
	while(x>0)
	{
		
		
		return n*power(n,x-1);
	}
	return 1;
}


}