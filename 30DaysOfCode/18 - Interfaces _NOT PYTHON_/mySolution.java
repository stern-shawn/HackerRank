// Provided code
import java.io.*;
import java.util.*;

interface AdvancedArithmetic{
  int divisorSum(int n);
}

//Write your code here
// Implement the divisiorSum function of the AdvancedArithmetic interface,
// ie. return the sum of all values which are even divisors of the input n
class Calculator implements AdvancedArithmetic {
  public int divisorSum(int n) {
    int sum = 0;
    // Check against all values up until n, starting at 1 to avoid mod by 0
    for (int i = 1; i <= n; i++) {
      // Only include in the sum if evenly divisible
      if (n % i == 0) {
          sum += i;
      }
    }

    return sum;
  }
}

// Provided code
class Solution {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    int n = scan.nextInt();
    scan.close();

    AdvancedArithmetic myCalculator = new Calculator();
    int sum = myCalculator.divisorSum(n);
    System.out.println("I implemented: " + myCalculator.getClass().getInterfaces()[0].getName() );
    System.out.println(sum);
  }
}
