public class Main implements Animal{
    public void eat(){
      System.out.println("Mammals eat");
    }
    public void travel(){
      System.out.println("Mammals travel");
    }
    public int noOfLegs(){
      return 0;
    }

  public static void main(String[] args) {
    System.out.println("Hello world!");
    Main m = new Main();
    m.eat();
    m.travel();
  }
}






interface Animal {
  public void eat();
  public void travel();
}
