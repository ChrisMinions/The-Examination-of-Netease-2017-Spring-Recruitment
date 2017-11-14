'''
[编程题] 魔力手环
时间限制：1秒
空间限制：32768K
小易拥有一个拥有魔力的手环上面有n个数字(构成一个环),当这个魔力手环每次使用魔力的时候就会发生一种奇特的变化：
每个数字会变成自己跟后面一个数字的和(最后一个数字的后面一个数字是第一个),
一旦某个位置的数字大于等于100就马上对100取模(比如某个位置变为103,就会自动变为3).
现在给出这个魔力手环的构成，请你计算出使用k次魔力之后魔力手环的状态。 
输入描述:
输入数据包括两行： 第一行为两个整数n(2 ≤ n ≤ 50)和k(1 ≤ k ≤ 2000000000),以空格分隔 
第二行为魔力手环初始的n个数，以空格分隔。范围都在0至99.


输出描述:
输出魔力手环使用k次之后的状态，以空格分隔，行末无空格。

输入例子1:
3 2 1 2 3

输出例子1:
8 9 7
'''

'''
解题思路：移位
  一开始老老实实用题目中描述的方法实现了一边，超时了，通过率只有20%，后来自己拿笔算了几组数据，
  发现了一些规律：
  比如， 最开始四个数是：
       a      b       c      d
  此时，第一个数有1个a，0个b，0个c，0个d组成，用向量表示就是[1,0,0,0]
  第二个数有0个a，1个b，0个c，0个d组成，用向量表示就是[0,1,0,0]
  这相当于第二个数字的向量是第一个数组向量向右移动了移位
  进过一次运算 这四个数是
     a+b     b+c      c+d     d+a
  此时，第一个数可用向量[1,1,0,0]表示，其本质就是原来第一个数的向量+该向量向右移一位的向量
  也就是 [1,1,0,0] = [1,0,0,0] + [0,1,0,0]
  找到这个规律后，我们可以简单算出经过k次操作后，序列中各个数字的向量表示，然后利用该向量表示，算出
  具体数值，最后用100取余即可
  But！！
  用该方法的通过率只有10%，惨，不过牛客网上也没有人可以通过测试，数据量实在是太大了
'''

'''
代码运行结果：
运行超时:您的程序未能在规定时间内运行结束，请检查是否循环有错或算法复杂度过大。
case通过率为10.00%
'''

from collections import deque

n, k = [int(each) for each in input().split()]
digs = [int(each) for each in input().split()]
digs

temp_list = [0] * n
temp_list[n-1] = 1
d = deque(temp_list)


def shift_add(deq):
    deq_ = deq.copy()
    temp = deq_.popleft()
    deq_.append(temp)
    deq_r = deque()
    while deq:
        deq_r.append(deq.popleft() + deq_.popleft())
    return deq_r


def shift(deq):
    temp = deq.popleft()
    deq.append(temp)
    return deq

for i in range(k):
    d = shift_add(d)

result = []
for i in range(n):
    temp_deq = d.copy()
    for k in range(i):
        temp_deq = shift(temp_deq)
    temp_digs = digs.copy()
    temp_sum = 0
    for j in range(n):
        temp_sum += temp_digs.pop() * temp_deq.popleft()
    temp_sum = temp_sum % 100
    result.append(temp_sum)

# print(result)
print(' '.join([str(each) for each in result]))
