Protection2.java
package p2;
class Protection2 extends p1.Protection
{
	
	Protection2()
	{
		System.out.println("Inside Protection2");
		//System.out.println("Value of n"+n);
         	//System.out.println("Value of n_pri"+n_pri);
		System.out.println("Value of n_pro"+n_pro);
		System.out.println("Value of n_pub"+n_pub);

	}
}

OtherPackage.java
package p2;
class OtherPackage
{
	p1.Protection pro = new p1.Protection();
	OtherPackage()
	{
		
		
		System.out.println("Inside Protection2");
		//System.out.println("Value of n"+pro.n);
         	//System.out.println("Value of n_pri"+pro.n_pri);
		//System.out.println("Value of n_pro"+pro.n_pro);
		System.out.println("Value of n_pub"+pro.n_pub);

	}
}

Demo.java
package p2;

class Demo
{
	public static void main(String args[])
	{
		Protection2 ob1=new Protection2();
		
		OtherPackage ob2=new OtherPackage();

	}
}
