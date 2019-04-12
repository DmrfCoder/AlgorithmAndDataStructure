package three;

import java.util.HashMap;
import java.util.Map;

/**
 * @author dmrfcoder
 * @date 2019/4/10
 */
class Point {
    int x;
    int y;

    Point() {
        x = 0;
        y = 0;
    }

    Point(int a, int b) {
        x = a;
        y = b;
    }
}

public class Solution {
    public int maxPoints(Point[] points) {

        int length = points.length;
        int maxPointCount = 0;
        for (int startIndex = 0; startIndex < length; startIndex++) {
            Map<String, Integer> maxPointMap = new HashMap<>();
            int commonPointCount = 0;
            int tempMaxCount = 1;
            for (int endIndex = startIndex + 1; endIndex < length; endIndex++) {
                int distanceX = points[startIndex].x - points[endIndex].x;
                int distanceY = points[startIndex].y - points[endIndex].y;


                if (distanceX == 0 && distanceY == 0) {
                    commonPointCount += 1;
                } else {
                    String curStrDis;
                    if (distanceX == 0) {
                        curStrDis = "distanceX";
                    } else if (distanceY == 0) {
                        curStrDis = "distanceY";
                    } else {
                        int maxCommonDivisor = commonDivisor(distanceX, distanceY);
                        if (maxCommonDivisor != 0) {
                            distanceX = distanceX / maxCommonDivisor;
                            distanceY = distanceY / maxCommonDivisor;
                        }

                        int flag = 0;

                        if (distanceX < 0) {
                            distanceX = -distanceX;
                            flag++;
                        }
                        if (distanceY < 0) {
                            distanceY = -distanceY;
                            flag++;
                        }

                        curStrDis = String.valueOf(distanceX) + distanceY;
                        if (flag == 1) {
                            curStrDis = "-" + curStrDis;
                        }
                    }

                    if (maxPointMap.containsKey(curStrDis)) {
                        tempMaxCount = Math.max(tempMaxCount, maxPointMap.get(curStrDis) + 1);
                        maxPointMap.put(curStrDis, maxPointMap.get(curStrDis) + 1);
                    } else {
                        //初始时put进去2，一个点是起始点，另一个点是当前点
                        maxPointMap.put(curStrDis, 2);
                        tempMaxCount = Math.max(tempMaxCount, 2);
                    }
                }
            }
            maxPointCount = Math.max(maxPointCount, tempMaxCount + commonPointCount);
        }

        return maxPointCount;
    }

    /**
     * 求最大公约数
     *
     * @param a
     * @param b
     * @return
     */
    public static int commonDivisor(int a, int b) {
        a = Math.abs(a);
        b = Math.abs(b);
        int count = 0;
        for (int i = 1; i <= Math.min(a, b); i++) {
            if (a % i == 0 && b % i == 0) {
                count = i;
            }
        }
        return count;
    }

    public static void main(String[] args) {

        Point point1 = new Point(2, 3);
        Point point2 = new Point(3, 3);
        Point point3 = new Point(-5, 3);
        Point point4 = new Point(9, -25);
        Point[] points = {point1, point2, point3};
        Solution solution = new Solution();
        System.out.println(solution.maxPoints(points));
    }

}
