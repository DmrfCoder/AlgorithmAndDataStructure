package two;

import java.util.Stack;

/**
 * @author dmrfcoder
 * @date 2019/4/10
 */
public class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> operateStack = new Stack<>();

        int size = tokens.length;


        for (int index = 0; index < size; index += 1) {
            String itemToken = tokens[index];

            if ("+".equals(itemToken) || "-".equals(itemToken) || "*".equals(itemToken) || "/".equals(itemToken)) {
                Integer operate2 = operateStack.pop();
                Integer operate1 = operateStack.pop();
                Integer result = 0;
                switch (itemToken) {
                    case "+":

                        result = operate1 + operate2;
                        break;
                    case "-":

                        result = operate1 - operate2;
                        break;
                    case "*":
                        result = operate1 * operate2;
                        break;
                    case "/":
                        result = (Integer) operate1 / operate2;
                        break;
                    default:
                        break;
                }
                operateStack.push(result);

            } else {
                operateStack.push(Integer.valueOf(itemToken));
            }


        }


        return operateStack.pop();
    }

    public static void main(String[] args) {
        String[] token = {"2","1","+","3","*"};
        Solution solution = new Solution();
        System.out.println(solution.evalRPN(token));
    }
}
