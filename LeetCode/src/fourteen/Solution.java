package fourteen;

/**
 * @author dmrfcoder
 * @date 2019/4/10
 */
public class Solution {
    public int singleNumber(int[] A) {


        int res = A[0];
        for (int index = 1; index < A.length; index++) {
            res = res ^ A[index];
        }
        return res;
    }

    public static void main(String[] args) {
        int[] A = {1, 2, 3, 2, 1};
        Solution solution = new Solution();
        System.out.println(solution.singleNumber(A));
    }
}
