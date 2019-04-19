package eleven;

import java.util.HashSet;
import java.util.Set;

/**
 * @author dmrfcoder
 * @date 2019/4/10
 */
public class Solution {
    public boolean wordBreak(String s, Set<String> dict) {
        if (s == null) {
            return false;
        }

        int sLength = s.length();
        boolean[] array = new boolean[sLength + 1];
        array[0] = true;


        for (int index = 0; index <= sLength; index++) {
            for (int index2 = 0; index2 < index; index2++) {
                for (String dictItem : dict) {
                    if (s.substring(index2, index).equals(dictItem) && array[index2]) {
                        array[index] = true;
                    }
                }
            }

        }


        return array[sLength];
    }

    public static void main(String[] args) {
        Set<String> dict = new HashSet<>();
        dict.add("aaa");
        dict.add("aaaa");
        Solution solution = new Solution();
        System.out.println(solution.wordBreak("aaaaaaa", dict));
    }
}


