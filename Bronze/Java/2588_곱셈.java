public class Main {
    public static void main(String[] args) {
        java.util.Scanner sc = new java.util.Scanner(System.in);
        int n1 = sc.nextInt();
        int n2 = sc.nextInt();
        System.out.println(n1*(n2%10));
        System.out.println(n1*((n2/10)%10));
        System.out.println(n1*(n2/100));
        System.out.println(n1*n2);
        
    }
}