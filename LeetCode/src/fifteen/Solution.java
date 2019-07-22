package fifteen;

/**
 * @author dmrfcoder
 * @date 2019/4/10
 */
public class Solution {
    public int singleNumber(int[] A) {

        //只出现过1次的位
        int a = 0;
        //出现过2次的位
        int b = 0;
        //出现过三次的位
        int c;
        for (int index = 0; index < A.length; index++) {
            //之前的b或上现在的出现了2次的位
            b = b | (a & A[index]);
            //只出现过1次的位
            a = a ^ A[index];
            c = a & b;
            //抹去出现了3次的bits,~c将原来是1的都变为0，这样那些为与完之后结果一定是0，原来为0的变为1，这样与的结果由a决定
            a = a & (~c);
            b = b & (~c);

        }
        return a;
    }

}
