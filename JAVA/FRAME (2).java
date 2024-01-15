import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
class FRAME
{
    JFrame f;
    JButton b;
    JPanel p;
    JLabel l;
    void run()
    {
        frame1();
        frame2();
    }

    FRAME()
    {
        f= new JFrame("PRITHWISH CHAKRABORTY");
        p= new JPanel();
        l= new JLabel("PERFECTION");
        b= new JButton("CLICK ME");
    }
    
    void frame2()
    {
        f.setLayout(null);
        f.setVisible(true);
        //f.add(p);
        f.add(l);
        f.add(b);
        //l.setLocation(1100,900);
    }

    void frame1()
    {
        
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        f.setSize(700,700);
        f.setLocation(300,20);
        b.setBounds(100,100,100,100);
        l.setVisible(true);
        l.setFont(new Font("Comic Sans",Font.BOLD,60));
        l.setBounds(400,400,400,400);
        p.setBackground(Color.blue);
        //l.setLocation(110,290);
    }
    
    public static void main(String[] args) {
        
        FRAME ob= new FRAME();
        ob.run();
    }
}