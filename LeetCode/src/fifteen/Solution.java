package fifteen;

/**
 * @author dmrfcoder
 * @date 2019/4/10
 */
public class Solution {
    public int singleNumber(int[] A) {

        int a = 0;//只出现过1次的位
        int b = 0;//出现过2次的位
        int c;//出现过三次的位
        for (int index = 0; index < A.length; index++) {
            b = b | (a & A[index]);//之前的b或上现在的出现了2次的位
            a = a ^ A[index];//只出现过1次的位
            c = a & b;
            a = a & (~c);//抹去出现了3次的bits,~c将原来是1的都变为0，这样那些为与完之后结果一定是0，原来为0的变为1，这样与的结果由a决定
            b = b & (~c);

        }
        return a;
    }

}
