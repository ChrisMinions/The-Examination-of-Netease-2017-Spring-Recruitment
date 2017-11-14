'''
[编程题] 调整队形
时间限制：1秒
空间限制：32768K
在幼儿园有n个小朋友排列为一个队伍，从左到右一个挨着一个编号为(0~n-1)。
其中有一些是男生，有一些是女生，男生用'B'表示，女生用'G'表示。小朋友们都很顽皮，
当一个男生挨着的是女生的时候就会发生矛盾。作为幼儿园的老师，你需要让男生挨着女生或者女生挨着男生的情况最少。
你只能在原队形上进行调整，每次调整只能让相邻的两个小朋友交换位置，现在需要尽快完成队伍调整，
你需要计算出最少需要调整多少次可以让上述情况最少。例如：
GGBBG -> GGBGB -> GGGBB
这样就使之前的两处男女相邻变为一处相邻，需要调整队形2次 
输入描述:
输入数据包括一个长度为n且只包含G和B的字符串.n不超过50.


输出描述:
输出一个整数，表示最少需要的调整队伍的次数

输入例子1:
GGBBG

输出例子1:
2
'''

'''
解题思路：透过现象看本质
   本质就是：一、所有男生在左，女生在右；二：所有女生在左，男生在右
   考虑情况一：遍历队列，发现第一个男生，把他移到左边第一位，继续遍历，发现第二位男生，把他移到左边第二位，
   记录下每次移动使用的交换次数，等移完男生后保存总交换次数
   情况二参考情况一，保存总交换次数。
   输出两次次数用得少的那一次
'''

'''
代码运行结果：
答案正确:恭喜！您提交的程序通过了所有的测试用例
'''

queue = input()
length = len(queue)
pos = 0
steps = 0
for i in range(length):
    if queue[i] == 'B':
        steps += (i - pos)
        pos += 1
pos = 0
steps_ = 0
for i in range(length):
    if queue[i] == 'G':
        steps_ += (i - pos)
        pos += 1

print(min((steps, steps_)))
