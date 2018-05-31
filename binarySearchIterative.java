class BinarySearch {
  int binarySearch(int arr[], int x) {
    int l= 0, r = arr.length -1;
    while (l <= r) {
      int mid = l + (r - l)/2;
      if (arr[mid] == x) {
        return mid;
      }
      if (arr[mid] < x) {
        l = mid + 1;
      }
      else {
        r = mid -1;
      }
    }
    return -1;
  }
}


class Main {
  public static void main(String[] args) {
    //System.out.println("Hello world!");
    BinarySearch ob = new BinarySearch();
    int arr[] = {1,3,5,10,50};
    int n  = arr.length;
    int x =10;
    int result = ob.binarySearch(arr, x);
    if (result == -1){
      System.out.println("Element is not present in array");
    }
    else {
      System.out.println("Element found at index " + result);
    }
  }
}
