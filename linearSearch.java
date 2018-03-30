class Main {
  public static void main(String[] args) {
    int[] arr = {10, 20, 80, 30, 60, 50, 110, 100, 130, 170};
    int n  = arr.length;
    int x = 100;
    System.out.println(search(arr, n, x));
    System.out.println("Hello world!");
  }
  
  static int search(int arr[], int n , int x){
    for (int i = 0; i < n; i++){
      if (arr[i] == x)
        return i;
    }
    return -1;
  }
  
}

