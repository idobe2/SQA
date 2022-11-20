package Test;

public class sumPositive {
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
