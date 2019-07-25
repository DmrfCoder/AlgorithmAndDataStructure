package seventeen;

/**
 * @author dmrfcoder
 * @date 2019/4/10
 */
public class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {

        //remaining为二维数组，remaing[index][0]代表车从第index出发到达index+1站后里面可以剩余的油，
        // remaing[index][1]=index，因为后面要对remaing按照remaing[index][0]即剩余的油量排序，
        // 所以要把原始的索引记录下来，排完序后直接从remaing[index][0]最大的值对应的remain[index][1]处开始开车即可
        int[][] remaining = new int[gas.length][2];

        //gas[i]---->gas[i+1]  cost[i]，计算remaining
        for (int index = 0; index < gas.length; index++) {
            remaining[index][0] = gas[index] - cost[index];
            remaining[index][1] = index;
        }

        //按照remaining[index][0]对remaing进行排序
        QuickSort(remaining, gas.length);

        //由于上面排完序是降序，所以这里从后往前遍历
        for (int index = gas.length - 1; index >= 0; index--) {
            //如果剩余的油大于等于0，说明油足够到达下一站
            if (remaining[index][0] >= 0) {
                if (helper(gas, cost, remaining[index][1])) {
                    return remaining[index][1];
                }
            } else {
                return -1;
            }
        }


        return -1;
    }

    //模拟从第startIndex站出发，看能不能走完全程
    boolean helper(int[] gas, int[] cost, int startIndex) {
        int count = 0;
        int curGas = 0;
        for (int index = startIndex; count <= gas.length; count++, index = (index + 1) % gas.length) {
            curGas += gas[index];
            if (curGas >= cost[index]) {
                curGas -= cost[index];
            } else {
                return false;
            }
        }

        return true;
    }

    void QuickSort(int[][] v, int length) {
        QSort(v, 0, length - 1);
    }

    void QSort(int[][] v, int low, int high) {

        if (low >= high) {
            return;
        }
        int t = Partition(v, low, high);
        QSort(v, low, t - 1);
        QSort(v, t + 1, high);
    }

    int Partition(int[][] v, int low, int high) {
        int pivotkey;
        pivotkey = v[low][0];

        while (low < high) {
            while (low < high && v[high][0] >= pivotkey) {
                --high;
            }
            int[] t;
            t = v[low];
            v[low] = v[high];
            v[high] = t;

            while (low < high && v[low][0] <= pivotkey) {
                ++low;
            }
            t = v[low];
            v[low] = v[high];
            v[high] = t;
        }

        return low;
    }


    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] gas = {3, 2, 5, 3, 4, 3};
        int[] cost = {2, 3, 4, 4, 3, 4};
        int index = solution.canCompleteCircuit(gas, cost);
        System.out.println("startIndex is: " + index);

    }
}
