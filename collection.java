import java.io.*;
import java.util.*;

class Main {
  public static void main(String[] args) {
    System.out.println("Hello world!");
    int arr[] = new int[] {5,4,3,2,1};
    Vector<Integer> v = new Vector();
    Hashtable<Integer, String> h = new Hashtable();
    v.addElement(1);
    v.addElement(2);
    v.addElement(3);
    h.put(1, "geeks");
    h.put(2, "4geeks");
    System.out.println(arr[1]);
    System.out.println(v.elementAt(0));
    System.out.println(h.get(2));
    System.out.println(v);
    System.out.println(h);
  }
}
