public class ROMGen {
	public static void main(String[] args) {
		String input = args[0];
		System.out.print("reg[7:0] s_ROM;\n\talways @(*)\n\tbegin\n\t\tcase (rom_addr)\n\t\t");
		for(int i = 0; i < input.length(); i++) {
			char c = input.charAt(input.length() - 1 - i);
			System.out.print(i + " : s_ROM = 7'h" + Integer.toString(c, 16) + ";\n\t\t");
		}
		System.out.print("default : s_ROM = 0;\n\tendcase\nend\n");
	}
}
