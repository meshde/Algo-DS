
class maxmin
{
	public static void main(String args[])
	{
		int arr[]={50,15,5,10,40,20};
		
		maxmin m=new maxmin();
		int max1=m.dividemax(arr,0,arr.length);
		System.out.println("max"+max1);
		
		

	int m1=m.dividemin(arr,0,arr.length);
	//int m2=m.dividemin1(arr,0,arr.length);
	
	System.out.println("minimum:");
	//if(m1>m2)
		//System.out.println(m2);
	//else
		System.out.println(m1);
		
	}
	
	
	public int dividemax(int arr[],int l,int h)
	{
		int m1=0,m2=0;
		
		if(l==h)
			return arr[l];
		else if(h==l+1)
		{
			if(arr[l]>arr[h])
				return arr[l];
			else 
				return arr[h];
			
		}
	
			int k=(l+h)/2;
			m1= dividemax(arr,l,k);
		m2=dividemax(arr,k+1,h-1);
		if(m2>m1)
		return m2;
	else
		return m1;
	}

	
	public int dividemin(int arr[],int l,int h)
	{
		
int m1=0,m2=0;
		if(l==h)
			return arr[l];
		else if(h==l+1)
		{
			if(arr[l]<arr[h])
				return arr[l];
			else 
				return arr[h];
			
		}
	
			int k=(l+h)/2;
			m1= dividemin(arr,l,k);
			m2= dividemin(arr,k+1,h-1);
			
			if(m1<m2)
			return m1;
		else 
			return m2;
			
	}
	

	}
	

	
	
	
