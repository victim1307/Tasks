import java.util.Scanner;

class game {

    String[][] arr = new String[3][3];
    int count;

    public void setall() {
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                arr[i][j] = "   ";
            }
        }
    }

    public void check(int a, int b, int count) {
        String comp = arr[a][b];
        if (comp.equals(" x ") || comp.equals(" o ")) {
            System.out.println("Already occupied");
        } else {
            if (this.count % 2 == 0) {
                arr[a][b] = " o ";
                this.count++;
            } else {
                arr[a][b] = " x ";
                this.count++;
            }
            wins();
            display();
        }
    }

    public int getcount() {
        return this.count;
    }

    public void display() {
        System.out.println("    1   2   3");
        System.out.println(" 1 " + arr[0][0] + "|" + arr[0][1] + "|" + arr[0][2]);
        System.out.println("   -----------");
        System.out.println(" 2 " + arr[1][0] + "|" + arr[1][1] + "|" + arr[1][2]);
        System.out.println("   -----------");
        System.out.println(" 3 " + arr[2][0] + "|" + arr[2][1] + "|" + arr[2][2]);
    }

    public void wins() {
        for (int q = 0; q < 3; q++) {
            if (arr[q][0].equals(" x ") || arr[q][0].equals(" o ")) {
                if (arr[q][0].equals(arr[q][1]) && arr[q][1].equals(arr[q][2])) {
                    System.out.println(arr[q][1] + "has won");
                    break;
                } else if (arr[0][q].equals(arr[1][q]) && arr[1][q].equals(arr[2][q])) {
                    System.out.println(arr[1][q] + "has won");
                    break;
                } else if (arr[0][0].equals(arr[1][1]) && arr[1][1].equals(arr[2][2])) {
                    System.out.println(arr[1][1] + "has won");
                    break;
                }
            }
        }
    }
}

public class Main {
    public static void main(String[] args) {

        game obj = new game();
        obj.setall();
        obj.display();
        Scanner sc = new Scanner(System.in);
        int count = 0;
        while (count < 9) {
            if (count % 2 == 0) {
                System.out.println("o's turn");
            } else {
                System.out.println("x's turn");
            }
            System.out.print("Enter i : ");
            int a = sc.nextInt();
            a = a - 1;
            System.out.print("Enter j : ");
            int b = sc.nextInt();
            b = b - 1;
            obj.check(a, b, count);
            count = obj.getcount();
        }

    }
}
