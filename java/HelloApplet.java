import javax.swing.*;
import java.awt.*;

public class HelloApplet extends JApplet
{
  
	public void init()
	{
    Container contentPane = getContentPane();
    contentPane.setLayout(new FlowLayout());
    JLabel friendlyLabel = new JLabel("Hellow out there!/n");
    contentPane.add(friendlyLabel);
	}
}
