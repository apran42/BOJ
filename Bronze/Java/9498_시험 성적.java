public class Main {
    public static void main(String[] args) {
        java.util.Scanner sc = new java.util.Scanner(System.in);
        int n1 = sc.nextInt();
        if (n1/10 >= 9)
            System.out.println("A");
        else if (n1/10 == 8)
            System.out.println("B");
        else if (n1/10 == 7)
            System.out.println("C");
        else if (n1/10 == 6)
            System.out.println("D");
        else
            System.out.println("F");
        
    }
}