/* Decrypt.java
 * Shane Kenny
 * 2/28/2021
 */


import java.util.*;
import java.io.*;

public class Decrypt {
	public static void main(String [] args) {
		String rawData = "";
		String[] split = new String[400];
		try {
			File in = new File("ciph.txt");
			Scanner rd = new Scanner(in);
			rawData = rd.nextLine();
			rd.close();

			rawData = rawData.replaceAll("\\]", "");
			rawData = rawData.replaceAll("\\[", "");
			rawData = rawData.replaceAll(",", " ");

			split = rawData.split(" ");
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
		ArrayList<Integer> data = new ArrayList<Integer>();
		for (int i = 0; i < split.length; i++) {
			if (split[i] != null && !(split[i].equals(""))) {
				data.add(Integer.parseInt(split[i]));
				//System.out.print(Integer.parseInt(split[i]) + " ");
			}
			else if (split[i] == null) { break; }
		}
		String dec = "";
		for (int i = 1; i < data.size(); i += 2) {
			int s = data.get(i);
			// correct index is (i - 1) + (s * 2)
			//					(i of s)+ (2shift)
			int index = (i - 1) + (s * 2);
			if (index < 0) { index = data.size() + index; }
			else { index = index % data.size(); }
			int value = data.get(index);
			dec += (char)value;
		}
		System.out.println(dec);
	}
}