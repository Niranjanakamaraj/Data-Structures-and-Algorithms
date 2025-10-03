//Given a positive integer n, determine whether it is odd or even. Return true if the number is even and false if the number is odd.
import java.util.Scanner;

class Odd_even{
    static boolean isEven(int n) {
        if(n%2==0){
            return true;
        }else{
            return false;
        }
    }
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        System.out.println(isEven(n));
    }
}