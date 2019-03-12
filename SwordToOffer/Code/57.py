# -*- coding:utf-8 -*-
'''
滑动窗口的最大值
给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，那么一共存在6个滑动窗口，他们的最大值分别为{4,4,6,6,6,5}； 针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下6个： {[2,3,4],2,6,2,5,1}， {2,[3,4,2],6,2,5,1}， {2,3,[4,2,6],2,5,1}， {2,3,4,[2,6,2],5,1}， {2,3,4,2,[6,2,5],1}， {2,3,4,2,6,[2,5,1]}。
'''

'''
import java.util.ArrayList;
import java.util.LinkedList;

/**
 * @author dmrfcoder
 * @date 2019/3/10
 */
public class fiveSix {
    public ArrayList<Integer> maxInWindows(int[] num, int size) {
        LinkedList<Integer> linkedList = new LinkedList<>();
        ArrayList<Integer> res = new ArrayList<>();
        if (size == 0) {
            return res;
        }

        boolean flag = false;

        for (int index = 0; index < num.length; index++) {
            if (linkedList.size() == size) {
                linkedList.removeFirst();
            }
            while (linkedList.size() != 0 && flag) {
                if (linkedList.getFirst() < num[index]) {
                    linkedList.removeFirst();
                } else {
                    break;
                }
            }

            linkedList.addLast(num[index]);

            if (index >= size - 1) {
                flag = true;
                int max = num[index];
                for (int index2 = 0; index2 < linkedList.size(); index2++) {
                    if (linkedList.get(index2) > max) {
                        max = linkedList.get(index2);
                    }
                }
                res.add(max);
            }

        }

        return res;

    }

    public static void main(String[] args) {
        fiveSix f = new fiveSix();
        ArrayList<Integer> arr = f.maxInWindows(new int[]{2, 3, 4, 2, 6, 2, 5, 1}, 3);
        for (Integer item : arr) {
            System.out.println(item);
        }
    }
}



'''