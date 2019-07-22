package sixteen;

/**
 * @author dmrfcoder
 * @date 2019/4/10
 */
public class Solution {
    public int candy(int[] ratings) {


        int n = ratings.length;
        int[] candyArray = new int[n];
        //第0个孩子初始分配1个糖果
        candyArray[0] = 1;
        for (int index = 1; index < ratings.length; index++) {

            //如果右边孩子的优先级大于左边孩子的优先级
            if (ratings[index] > ratings[index - 1]) {
                //右边孩子分配的糖果数更新为左边孩子分配的糖果数加1
                candyArray[index] = candyArray[index - 1] + 1;
            } else {
                //如果右边孩子的优先级不大于左边孩子的优先级，将右边孩子的糖果数分配为1
                candyArray[index] = 1;
            }
        }

        int sum = candyArray[ratings.length - 1];
        for (int index = ratings.length - 2; index >= 0; index--) {
            //如果左边孩子的优先级大于右边孩子的优先级且左边孩子分配的糖果小于等于右边孩子分配的糖果
            if (ratings[index] > ratings[index + 1] && candyArray[index] <= candyArray[index + 1]) {
                //左边孩子分配的糖果数更新为右边孩子的糖果数加1
                candyArray[index] = candyArray[index + 1] + 1;
            }
            sum += candyArray[index];
        }
        return sum;
    }


    public static void main(String[] args) {

        int[] ratings = {1, 0, 2};

        Solution solution = new Solution();
        int a = solution.candy(ratings);
        System.out.println(a);
    }
}
