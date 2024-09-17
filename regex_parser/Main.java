package regex_parser;

public class Main {
    public static void main(String[] args) {
        System.out.println(Parser.parse("aa", "a") == false);
        System.out.println(Parser.parse("aa", "aa") == true);
        System.out.println(Parser.parse("aa", "a.c") == true);
        System.out.println(Parser.parse("abbb", "ab*") == true);
        System.out.println(Parser.parse("acd", "ab*c") == true);
    }
}
