import java.util.*;
import bit.*;
class fliptoconvert
{
   public static void main(String args[])
   {
	   Scanner sc=new Scanner(System.in);
	   System.out.println("enter the nos");
	   bitfunction bf=new bitfunction();
	   int n1=sc.nextInt();
	   int n2=sc.nextInt();
	   
	   int r= n1^n2;
	   
	   System.out.println("no of flips required:"+bf.countsetbits(r));
	   
   }
}