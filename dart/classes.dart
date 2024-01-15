void main() {
  // User me = User("goat", 50);
  Leader me = Leader("prithwish", 50);
  me.show();
  me.greet();
}

class User {          //super class
  String name = "";
  int age = 0;

  User(String u, int a) {
    name = u;
    age = a;
  }

  void show() {
    print("Name-> $name \nAge-> $age");
  }
}

class Leader extends User {
  String mail = "";
  Leader(String us, int ag) : super(us, ag) {
    mail = us + "_" + ag.toString() + "@gmail.com";
  }
  void greet() {
    print("LOGGING IN TO ::   $mail");
  }
}
