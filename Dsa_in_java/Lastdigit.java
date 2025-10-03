import java.util.Scanner;
class Lastdigit {
    static int lastDigit(int n) {
    int last_digit=n%10;
    return last_digit;
}
public static void main(String[] args){
    Scanner sc=new Scanner(System.in);
    int n=sc.nextInt();
    System.out.println(lastDigit(n));
}
}