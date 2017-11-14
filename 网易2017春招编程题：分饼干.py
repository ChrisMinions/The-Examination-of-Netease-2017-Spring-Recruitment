'''
[编程题] 分饼干
时间限制：1秒
空间限制：32768K
易老师购买了一盒饼干，盒子中一共有k块饼干，但是数字k有些数位变得模糊了，
看不清楚数字具体是多少了。易老师需要你帮忙把这k块饼干平分给n个小朋友，
易老师保证这盒饼干能平分给n个小朋友。现在你需要计算出k有多少种可能的数值 
输入描述:
输入包括两行：
 第一行为盒子上的数值k，模糊的数位用X表示，长度小于18(可能有多个模糊的数位)
 第二行为小朋友的人数n


输出描述:
输出k可能的数值种数，保证至少为1

输入例子1:
9999999999999X 3

输出例子1:
4
'''

'''
解题思路：深度优先搜索（dfs）+ 动态规划
  方法一：
  使用dfs思路不难，不过...
  复杂度太大了...最差情况复杂度是O(10^len(k))
  计算机算不出来
  方法二：
  方法二的思路来自牛客网上的答案解析，在这儿我就不拾人牙慧了，有兴趣可以去牛客网查看
'''

'''
代码运行结果：
运行超时:您的程序未能在规定时间内运行结束，请检查是否循环有错或算法复杂度过大。
case通过率为10.00%
方法二：
答案正确:恭喜！您提交的程序通过了所有的测试用例
'''

# 方法一：
# k = input()
# n = int(input())
# length = len(k)
#
#
# def get_solution(pos, dig):
#     if pos == length:
#         if dig % n == 0:
#             return 1
#         else:
#             return 0
#     else:
#         temp = 0
#         if k[pos] != 'X':
#             temp_dig = dig + int(k[pos]) * (10 ^ (length-pos-1))
#             temp_pos = pos + 1
#             temp += get_solution(temp_pos, temp_dig)
#         else:
#             for i in range(10):
#                 temp_dig = dig + i * (10 ^ (length-pos-1))
#                 temp_pos = pos + 1
#                 temp += get_solution(temp_pos, temp_dig)
#         return temp
# print(get_solution(0, 0))

# 方法二
k = input()
n = int(input())
length = len(k)
dp = [0] * n
if k[0] == 'X':
    for d in range(10):
        _ = d % n
        dp[_] += 1
else:
    dp[int(k[0]) % n] = 1

for i in range(1, length):
    new_dp = [0] * n
    for j in range(n):
        if dp[j]:
            if k[i] == 'X':
                for d in range(10):
                    new_j = (j*10+d) % n
                    new_dp[new_j] += dp[j]
            else:
                new_j = (j*10+int(k[i])) % n
                new_dp[new_j] += dp[j]
    dp = new_dp

print(dp[0])
