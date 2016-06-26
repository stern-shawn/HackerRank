import java.lang.reflect.Method;

class Solution {
  //Write your code here

  // Use <E> to make the function accept generic types, not sticktly ints,
  // Strings, etc
  public static <E> void printArray(E[] elements) {
    for (E element : elements) {
      System.out.println(element);
    }
  }

  // Provided code
  public static void main(String args[]){
    Integer[] intArray = { 1, 2, 3 };
    String[] stringArray = { "Hello", "World" };

    printArray( intArray  );
    printArray( stringArray );

    if(Solution.class.getDeclaredMethods().length > 2){
      System.out.println("You should only have 1 method named printArray.");
    }
  }
}
