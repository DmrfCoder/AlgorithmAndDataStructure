package twelve;

/**
 * @author dmrfcoder
 * @date 2019-04-18
 */

import java.util.*;

public class Solution {
    public ArrayList<String> wordBreak(String s, Set<String> dict) {
        ArrayList<String> dfs = dfs(s, dict, new HashMap<>());

        return dfs;
    }

    private ArrayList<String> dfs(String s, Set<String> dict, Map<String, ArrayList<String>> map) {

        ArrayList<String> arrayList = new ArrayList<>();
        if ("".equals(s)) {
            arrayList.add("");
            return arrayList;
        }
        if (map.containsKey(s)) {
            return map.get(s);
        } else {
            for (int index = s.length()-1; index >= 0; index--) {
                if (dict.contains(s.substring(index))) {
                    ArrayList<String> dfsResult = dfs(s.substring(0,index), dict, map);
                    if (dfsResult.size() == 0) {
                        continue;
                    } else {
                        String temp = s.substring(index);

                        for (String str : dfsResult) {
                            if ("".equals(str)) {
                                arrayList.add(temp);
                            } else {
                                StringBuilder stringBuilder = new StringBuilder();
                                stringBuilder.append(str).append(" ").append(temp);
                                arrayList.add(stringBuilder.toString());
                            }

                        }

                    }
                }
            }
        }
        map.put(s, arrayList);
        return arrayList;

    }

    public static void main(String[] args) {
        Set<String> dict = new HashSet<>();
        dict.add("cat");
        dict.add("cats");
        dict.add("and");
        dict.add("sand");
        dict.add("dog");
        dict.add("aaaa");
        dict.add("aa");
        dict.add("a");
        dict.add("b");
        Solution solution = new Solution();
        ArrayList<String> list = solution.wordBreak("catsanddog", dict);
        for (String s : list) {
            System.out.println(s);
        }

    }

}