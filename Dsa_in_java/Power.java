import java.util.Scanner;
class Power{
    public static int power(int n,int p) {
        return (int)Math.pow(n,p);
    }
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int p=sc.nextInt();
        System.out.println(power(n,p));
    }
}