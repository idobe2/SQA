import java.util.Arrays;
import java.util.Random;

public class Main {
    public static void main(String[] args) {
        int passed = 0;
        for (int n=0; n<3; n++) // n = array length
            if (runTest(n)) {
                passed++;
                showMessage(0);
            } else showMessage(1);
        if (passed==3) showMessage(100);
    }

    public static boolean runTest(int length) {
        int[] arr = new int[length];
        Random random = new Random();
        int exp;
        switch (length)
        {
            case 0:
                if (isEqual(sumPositive(arr),exp=0))
                    return true;
                break;
            case 1:
                Arrays.setAll(arr, i -> random.nextInt(-10, 10));
                System.out.println("{"+arr[0]+"}");
                if (isEqual(sumPositive(arr),exp = Math.max(sumPositive(arr), arr[0])))
                    return true;
                break;
            case 2:
                Arrays.setAll(arr, i -> random.nextInt(-10, 10));
                System.out.println("{"+arr[0]+", "+arr[1]+"}");
                if (isEqual(sumPositive(arr),exp = Math.max(sumPositive(arr), arr[0]+arr[1])))
                    return true;
                break;
            default:
                break;
        }
        return false;
    }

    public static void showMessage(int msg_id) {
        switch (msg_id)
        {
            case 0:
                System.out.println("Passed!\n");
                break;
            case 1:
                System.out.println("Failed!\n");
                break;
            case 100:
                System.out.println("All tests passed!\n");
                break;
            default:
                break;
        }
    }

    public static boolean isEqual(Object value1, Object value2) {
        System.out.println("Function result: " + value1 + "\nExpected result: " + value2);
        return value1 == value2; }

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