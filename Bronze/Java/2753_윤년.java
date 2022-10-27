public class Main {
    public static void main (String[] args) {
        java.util.Scanner sc = new java.util.Scanner(System.in);
        int year = sc.nextInt();
        if (year % 4 == 0 && year % 100 != 0)
            System.out.println("1");
        else if (year % 100 == 0 && year % 400 == 0)
            System.out.println("1");
        else
            System.out.println("0");
        
    }
}