#include <iostream>
#include <string>

struct Student {
    int id;
    std::string name;
    int age;
};

// Function that takes a Student structure as a parameter
static void displayStudentInfo(Student& student) {
    static int a=10;
    a+=10;
    std::cout << "A: " << a << std::endl;
    std::cout << "Student Information:\n";
    std::cout << "ID: " << student.id << std::endl;
    std::cout << "Name: " << student.name << std::endl;
    std::cout << "Age: " << student.age << std::endl;

    student.name="kalia don";
    student.id=420;
}

int main() {
    // Declare a structure variable and assign data to its members
    Student studentData;
    studentData.id = 12345;
    studentData.name = "John Doe";
    studentData.age = 20;

    // Call the function and pass the structure variable
    displayStudentInfo(studentData);
    displayStudentInfo(studentData);

    return 0;
}