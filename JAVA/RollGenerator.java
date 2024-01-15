// package com.ritam;
import java.util.*;
public class RollGenerator {
    public static void main(String[] args) {
        Student s1 = new Student();
        System.out.println(Student.count);
        Student s2 = new Student();
        System.out.println(Student.count);
        Student s3 = new Student();
        System.out.println(Student.count);
        System.out.println(s1.showRollno());
        //System.out.println(s1.showRollno());
        System.out.println(s2.showRollno());
        System.out.println(s3.showRollno());
    }
}
class Student{
    private String rollno;
    static int count=1;

    private String generateRoll(){
        Date d=new Date();
        String rn="jisu"+(d.getYear()+1900)+count;
        count++;
        return rn;
    }

    public Student (){
        rollno=generateRoll();
    }
    public String showRollno(){
        return rollno;
    }
}