import java.util.*;

class spiral {
    int a[][], x;

    void nor() {
        int i, j, m = 1;
        for (i = 0; i < x; i++) {
            for (j = 0; j < x; j++) {
                a[i][j] = m++;
            }
        }
    }

    void print() {
        int i, j;
        for (i = 0; i < x; i++) {
            for (j = 0; j < x; j++) {
                System.out.print(a[i][j] + "\t");
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("ENTER SIZE OF ARRAY");
        spiral ob = new spiral(sc.nextInt());
        ob.run();
    }

    void accept() {
        Scanner sc = new Scanner(System.in);
        sc.nextInt();
    }

    spiral(int c) {
        a = new int[c][c];
        x = c;
    }

    void run() {
        spi();
        print();
    }

    void spi() {
        int i, j, n = 1;
        for (j = 0; j <= (x / 2); j++) {
            for (i = j; i < (x - j); i++)
                a[j][i] = n++;
            if (j < (x / 2)) {
                for (i = j + 1; i < x - 1 - j; i++)
                    a[i][x - 1 - j] = n++;
                for (i = x - 1 - j; i >= j; i--)
                    a[x - 1 - j][i] = n++;
                for (i = x - 2 - j; i > 0 + j; i--)
                    a[i][j] = n++;
            }
        }
    }

    void bor() {
        int i, n = 1;
        for (i = 0; i < x; i++)
            a[0][i] = n++;
        for (i = 1; i < x - 1; i++)
            a[i][x - 1] = n++;
        for (i = x - 1; i >= 0; i--)
            a[x - 1][i] = n++;
        for (i = x - 2; i > 0; i--)
            a[i][0] = n++;
    }
}