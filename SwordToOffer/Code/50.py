# -*- coding:utf-8 -*-
'''
在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，但不知道有几个数字是重复的。也不知道每个数字重复几次。请找出数组中任意一个重复的数字。 例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。
'''
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        length = len(numbers)
        for i in range(len(numbers)):
            index = numbers[i]
            if index >= length:
                '''
                比如当前index=2，那么如果numbers[2]>=length,有两种可能，一种是其之前的与其不相等的数给其加了length，还有一种是之前与其相等的数给其加了length，所以先给其减length，如果给其加length的数与其值相同，则减去之后的值作为下标就应该对应到自己即大于length
                '''
                index -= length

            if numbers[index] > length:
                duplication[0] = index
                return True

            numbers[index] += length

        return False


s = Solution()
a = [-1]
print s.duplicate([2, 1, 3, 0, 4], a)
print a

'''
n=5
[0,1,2,3,4]
[2, 1, 3, 0, 4]
[2,1,5,0,4]
[2,2,5,0,4]
[2,2,5,0,4]

[1,2,2,3]
[1,6,2,3]
[1,6,6,3]




[
{2,3,8,0,3,5,3}
{2,3,8,3,3,5,3}
{2,3,}
public class Main {
    public static void main(String[] args) {
        System.out.println("Hello World!");
    }
    
    
    private int findMax(int[][] array){
        int sizeW=array.length();
        int sizeH=array[0].length();
        
        int maxValue=0;
        
        for(int indexH=0;indexH<sizeH;indexH++){
            for(int indexW=0;indexW<sizeW;indexW++){
                if(array[indexH][indexW]!=0){
                     int flag=0;
                     int tempValue=0;
                    
                    for(int index=indexW-1;index>=0;index--){
                        if(array[indexH][index]==0){
                            flag=1;
                            break
                        }else{
                            if(flag==0){
                                break;
                            }
                            if(array[indexH][index]>tempValue){
                                tempValue=array[indexH][index];
                            }
                        }
                    }
                    
                    flag=0
                    for(int index=indexW+1;index<indexW;index++){
                        if(array[indexH][index]==0){
                            flag=1;
                            break
                        }else{
                            if(array[indexH][index]>tempValue){
                                tempValue=array[indexH][index];
                            }
                        }
                    }
                    
                    
                }
             
            }
        }
            
    }
    /**
    302
    
    01
    1110
    0110
    0000
    0001
    
    
    1203
    03
    */
    
}
'''
