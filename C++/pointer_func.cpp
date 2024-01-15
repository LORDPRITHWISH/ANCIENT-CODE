#include <iostream>
#include <string>
class Student {
private:
    std::string* name;
    int* age;
public:
    Student(const std::string& n, int a) {
        name = new std::string(n);
        age = new int(a);
    }
    void displayInfo() {
        std::cout << "Student Name: " << *name << std::endl;
        std::cout << "Student Age: " << *age << std::endl;
    }
};
int main() {
    Student* student1 = new Student("Alice", 20);
    student1->displayInfo();
    Student student2 = Student("Alice", 20);
    student2.displayInfo();
    return 0;
}
