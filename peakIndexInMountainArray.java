/*
class Main {
  public static void main(String[] args) {
    //System.out.println("Hello world!");
    int[] A = {0,2,1,0};
    System.out.println(peakIndexInMountainArray(A));
  }

  public static int peakIndexInMountainArray(int[] A) {
    for (int i = 1; i+1 < A.length; ++i) {
      if (A[i] > A[i-1]){
        return i;
      }
    }
    return 0;
  }
}
*/
//or below way

class Main {
  public static void main(String[] args) {
    //System.out.println("Hello world!");
    int[] B = {0,2,1,0};
    Test obj = new Test();
    System.out.println(obj.peakIndexInMountainArray(B));
  }
}

class Test {
  public static int peakIndexInMountainArray(int[] A) {
    for (int i = 1; i+1 < A.length; ++i) {
      if (A[i] > A[i-1]){
        return i;
      }
    }
    return 0;
  }
}
