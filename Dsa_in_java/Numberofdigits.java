import java.util.Scanner;
class Numberofdigits {
    static int evenlyDivides(int n) {
        String n1=String.valueOf(n);
        int count=n1.length();
        return count;
    }
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        System.out.println(evenlyDivides(n));
    }
}