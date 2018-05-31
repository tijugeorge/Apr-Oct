class BinarySearch {
  int binarySearch(int arr[], int l, int r, int x) {
    if (r >= l) {
      int mid = l + (r - l)/2;
      if (arr[mid] == x) {
        return mid;
      }
      if (arr[mid] > x) {
        return binarySearch(arr, l, mid-1, x);
      }
      return binarySearch(arr, mid+1, r, x);  
    }
    return -1;
  }
}


class Main {
  public static void main(String[] args) {
    //System.out.println("Hello world!");
    BinarySearch ob = new BinarySearch();
    int arr[] = {2,3,5,10,50};
    int n = arr.length;
    int x = 10;
    int result = ob.binarySearch(arr, 0, n-1, x);
    if (result == -1) {
      System.out.println("Element not present");
    }
    else {
      System.out.println("Element found at index " + result);
    }
  }
}
