public class constructorInheritance {
    public static void main(String[] args){
        Grandchild g=new Grandchild();
    }
}
class Parent {
    public Parent(){
        System.out.println("Parent constructor");
    }
}
class Child extends Parent {
    public Child() {
        System.out.println("chlild construcor");
    }
}
class Grandchild extends Child{
    System.out.print("grand child construcrtor");
}