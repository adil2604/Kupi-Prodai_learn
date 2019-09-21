import java.util.*;

class MyStack<T> {
  Stack<T> stack =new Stack<>();
  T min;

  public MyStack(){

  }
  public void push(T o){
    if (stack.isEmpty){
      min=o;
    }
    stack.push(o);
    if (o.compareTo(min)<0){
      min=o;
    }
  }
  public T min(){
    return min;
  }

}
class Test{
  public static void main(String[] args) {
    MyStack<Integer> stack=new MyStack<>();
    stack.push(6);
    stack.push(4);
    stack.push(2);
    System.out.println(stack.min());
  }
}
