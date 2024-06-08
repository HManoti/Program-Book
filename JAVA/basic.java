import java.util.Scanner;
public class basic
{
	public static void main(String[] args) 
	{
		Scanner sc = new Scanner (System.in);
		int N= sc.nextInt();
		int rot=sc.nextInt();
		int a[]=new int[N];

		for(int i=0; i<a.length; i++)
			a[i]=sc.nextInt();
		rot= rot%N;
		for(int i=0;i<N;i++)
		{
			if(i<rot)
				System.out.print(a[N+i-rot]+"");
			else
				System.out.print(a[i-rot]+""); 
		}
	}
}