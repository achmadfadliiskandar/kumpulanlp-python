import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class StatistikDasar {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Masukkan jumlah elemen: ");
        int n = scanner.nextInt();
        
        int[] data = new int[n];
        System.out.println("Masukkan elemen:");
        for (int i = 0; i < n; i++) {
            data[i] = scanner.nextInt();
        }
        
        System.out.println("Rata-rata: " + hitungRataRata(data));
        System.out.println("Median: " + hitungMedian(data));
        System.out.println("Modus: " + hitungModus(data));
    }

    public static double hitungRataRata(int[] data) {
        int total = 0;
        for (int num : data) {
            total += num;
        }
        return (double) total / data.length;
    }

    public static double hitungMedian(int[] data) {
        Arrays.sort(data);
        if (data.length % 2 == 0) {
            return (data[data.length / 2 - 1] + data[data.length / 2]) / 2.0;
        } else {
            return data[data.length / 2];
        }
    }

    public static int hitungModus(int[] data) {
        Map<Integer, Integer> frekuensi = new HashMap<>();
        for (int num : data) {
            frekuensi.put(num, frekuensi.getOrDefault(num, 0) + 1);
        }

        int modus = data[0];
        int maxFrekuensi = 0;

        for (Map.Entry<Integer, Integer> entry : frekuensi.entrySet()) {
            if (entry.getValue() > maxFrekuensi) {
                maxFrekuensi = entry.getValue();
                modus = entry.getKey();
            }
        }

        return modus;
    }
}