'''
[编程题] 双核处理
时间限制：1秒
空间限制：32768K
一种双核CPU的两个核能够同时的处理任务，现在有n个已知数据量的任务需要交给CPU处理，假设已知CPU的每个核1秒可以处理1kb，
每个核同时只能处理一项任务。n个任务可以按照任意顺序放入CPU进行处理，
现在需要设计一个方案让CPU处理完这批任务所需的时间最少，求这个最小的时间。 
输入描述:
输入包括两行： 第一行为整数n(1 ≤ n ≤ 50) 第二行为n个整数length[i](1024 ≤ length[i] ≤ 4194304)，
表示每个任务的长度为length[i]kb，每个数均为1024的倍数。


输出描述:
输出一个整数，表示最少需要处理的时间

输入例子1:
5 3072 3072 7168 3072 1024

输出例子1:
9216
'''

'''
解题思路：动态规划 + 枚举
  方法一：动态规划
  对于动态规划，我实在没啥信心把它讲清楚，瞎几把讲一通只会让大家更加懵逼，强烈推荐大家去看《算法图解》一书，
  里面对动态规划有着非常深入浅出的描述，不出我所料，这道题目果然又超时了。所以如果数据量大的话不建议用python实现
  动态规划
  方法二：枚举
  这道题目用动态规划其实不是最合理的，这道题目也就是把这么多任务分成两堆任务而已，因为只需要分成两堆，
  我们大可以用枚举法列出所有情况，然后选出最合适的即可
'''

'''
方法一：
代码运行结果：
运行超时:您的程序未能在规定时间内运行结束，请检查是否循环有错或算法复杂度过大。
case通过率为40.00%
方法二：
代码运行结果：
答案正确:恭喜！您提交的程序通过了所有的测试用例
'''

# 方法一：动态规划
# n = int(input())
# task_lengths = [int(each)//1024 for each in input().split()]
# length_sum = sum(task_lengths)
# lengths_ave = length_sum // 2
# col = (lengths_ave + 1)
# dp = [0] * col
# for i in range(n):
#     dp_ = [0] * col
#     for j in range(1, col):
#         if task_lengths[i] > j:
#             dp_[j] = dp[j]
#         else:
#             temp = task_lengths[i] + dp[(j - task_lengths[i])]
#             dp_[j] = max(dp[j], temp)
#     dp = dp_
# print((length_sum-dp[lengths_ave])*1024)

# 方法二：枚举
n = int(input())
task_lengths = [int(each)//1024 for each in input().split()]

sum_length = sum(task_lengths)
x = set()
x.add(0)

for i in range(n):
    y = set()
    for p in x:
        if p + task_lengths[i] not in x:
            y.add(p + task_lengths[i])
    x.update(y)

ans = sum_length

ans = min([max(p, sum_length - p) for p in x])

print(ans * 1024)
