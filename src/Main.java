import java.util.Arrays;
import java.util.Random;

public class Main {
    public static void main(String[] args) {
        Random random = new Random();
        int[] arr_0 = new int[0], arr_1 = new int[1], arr_2 = new int[2];
        System.out.println("test array is empty: " + sumPositive(arr_0)); // Not entered
        Arrays.setAll(arr_1, i -> random.nextInt(-10,10));
        System.out.println("test array size is 1: " + sumPositive(arr_1)); // Entered 1 time
        Arrays.setAll(arr_2, i -> random.nextInt(-10, 10));
        System.out.println("test array size is 2: " + sumPositive(arr_2)); // Entered 2 time
        if (test(0, sumPositive(arr_0)) && test(Math.max(arr_1[0],0),sumPositive(arr_1))
                && test((Math.max(arr_2[0],0)+Math.max(arr_2[1],0)),sumPositive(arr_2)))
            System.out.println("Expected result!"); }

    public static boolean test(int test1, int test2) { return test1 == test2; }
    public static int sumPositive(int arr[])
    {
        int sum = 0;
        for(int i = 0; i < arr.length; i++)
        {
            if(arr[i] > 0)
                sum += arr[i];
        }
        return sum;
    }

}