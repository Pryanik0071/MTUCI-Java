public class Palindrome {
    public static void main(String[] args) {
        for(int i = 0; i < args.length; i++) {
            String s = args[i];
            if (isPalindrome(s)) {
                System.out.println(s + " is Palindrome");
            } else {
                System.out.println(s + " NO");
            }
        }
    }

    public static String reverseString(String s) {
        String out = "";
        for(int i = s.length() - 1; i >= 0; i--) {
            out += s.charAt(i);
        }
        return out;
    }

    public static boolean isPalindrome(String s) {
        return s.equals(reverseString(s));
    }
}
