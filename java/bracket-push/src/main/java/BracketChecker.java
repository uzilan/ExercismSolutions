import java.util.*;

final class BracketChecker {
    private static final HashMap<Character, Character> match = new HashMap() {{
       put('{','}');
       put('(',')');
       put('[',']');
    }};
    private String s;
    public BracketChecker(String s) {
        this.s = s;
    }
    public boolean areBracketsMatchedAndNestedCorrectly() {
        Stack<Character> close = new Stack();
        for (char ch : s.toCharArray()) {
            if (match.containsKey(ch)) close.push(match.get(ch));
            else if (match.values().contains(ch) && 
                (close.isEmpty() || close.pop() != ch)) return false;
        }
        return close.isEmpty();
    }
}
