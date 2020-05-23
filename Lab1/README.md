Java Lab 1: Java Warm-Up
This week you will start learning the basics of Java syntax with a few simple programming problems. You will also get to learn how to use the Java compiler and the Java Virtual Machine to run your programs. Here are the problems for you to solve:

Prime Numbers
Prime numbers often feature prominently in programming assignments, and this track will be no different! For the first problem you will create a program that finds and prints out all prime numbers less than 100. You can use this problem to practice writing Java functions and loops.

Create a file called Primes.java, and inside of this file create a class like this:

/**
 * TODO:  Comment describing your class
 */
public class Primes {
    /**
     * TODO:  Comment describing this method
     */
    public static void main(String[] args) {
        // TODO:  Implement your program
    }
}
Once you have this, you should be able to compile and run the program, but of course it won't do anything yet because you haven't actually implemented the code.

Inside this class, after the main() method, write a function isPrime(int n) that reports whether or not the argument is a prime number. You can assume that the input value n will always be at least 2. The full function signature will be:

public static boolean isPrime(int n) {
    // TODO:  Implement
}
You can implement this method however you want, but a simple approach is to write a for-loop that iterates from 2 all the way up to (but not including) n, checking to see if any value divides evenly into n. This can be tested with the % remainder operator; for example, 17 % 7 is 3, and 16 % 4 is 0. If any value evenly divides into the argument, return false; if no value evenly divides into the argument then it's prime, and you can return true. (The return statement is how you leave a method and return a value to the caller, in Java.)

Once this method is done, you can fill in the main() method with another loop that iterates over the values in the range 2 to 100, inclusive, printing out the values that your isPrime() helper indicates are prime.

Once your program is completed, compile and test it, and make sure the results are correct! There are many lists of prime numbers on the Internet, so it should be easy to verify the results.

Also, as the example code indicates, make sure to write a comment describing the purpose of the class, and also write a comment before each method describing its purpose. It is extremely important to write comments describing such things when you write programs.

Palindromes
The second program you will write this week is a program to tell if a string is a palindrome. There are several different ways that such a program could work, but we will choose an approach that will give you practice with the Java features discussed in the first lecture.

For this program, you will create a class called Palindrome, in a file called Palindrome.java. This time you can start with the following code:

/**
 * TODO:  Comment describing your class
 */
public class Palindrome {
    /**
     * TODO:  Comment describing this method
     */
    public static void main(String[] args) {
        for (int i = 0; i < args.length; i++) {
            String s = args[i];

            // TODO:  Determine if s is a palindrome, and print out the
            //        result.  Make sure s is enclosed with double-quotes
            //        in your program's output.
        }
    }
}
Again, you should be able to compile and run this program as-is, but it won't produce any interesting output yet.

Your first task is to create a method to reverse the characters in a string. The method's signature should be: public static String reverseString(String s)

You can implement this method by creating a local variable that starts with a string "", and then append the characters of the input string into the output string, in reverse order. String objects have a length() method that reports the string's length, and a charAt(int index) method that returns the character at the specified index. Indexes start with 0 and go up to size - 1. For example:

String s = "pizzeria";
System.out.println(s.length());   // Prints out 8
System.out.println(s.charAt(5));  // Prints out r
You can use the String concatenation operator + for this, or you could also use the compound assignment operator += if you prefer.

Once your reverseString() method is implemented, you can create another method public static boolean isPalindrome(String s). All this method needs to do is to create a reversed version of s, then compare it to the original input for equality. With Strings (and with all Java objects), you use the equals(Object) method to test for value-equality. For example:

String s1 = "hello";
String s2 = "Hello";
String s3 = "hello";

s1.equals(s2);  // This is false
s1.equals(s3);  // This is true
Do not use == to check for string equality! This does a different test in Java, which we will be discussing in the next lecture.

Once you have finished writing your code, compile and test your program! This time, you will give your program its input as command-line arguments, like this:

java Palindrome madam racecar apple kayak song noon
This should cause your program to print out whether each word is a palindrome or not.

As before, make sure to clearly document the purpose of your program, and each method in the program.

All Done!
When you have completed these tasks, you can submit your .java files to csman so they can be graded! Do not submit your .class files or any other file; we will compile your programs before we test them.