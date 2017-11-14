'''
[编程题] 涂棋盘
时间限制：1秒
空间限制：32768K
小易有一块n*n的棋盘，棋盘的每一个格子都为黑色或者白色，小易现在要用他喜欢的红色去涂画棋盘。
小易会找出棋盘中某一列中拥有相同颜色的最大的区域去涂画，帮助小易算算他会涂画多少个棋格。 
输入描述:
输入数据包括n+1行：
 第一行为一个整数n(1 ≤ n ≤ 50),即棋盘的大小
 接下来的n行每行一个字符串表示第i行棋盘的颜色，'W'表示白色，'B'表示黑色


输出描述:
输出小易会涂画的区域大小

输入例子1:
3 BWW BBB BWB

输出例子1:
3
'''

'''
解题思路：审题
  拥有相同颜色的最大的区域必须连续
  我们遍历棋牌中的每一列，计算每一列中颜色相同的最大区域数放入一个列表中，最后输出列表中最大的值即可
'''

'''
代码运行结果：
答案正确:恭喜！您提交的程序通过了所有的测试用例
'''

n = int(input())


def calc(col):
    max_count = 1
    count = 1
    for x in range(1, n):
        if col[x] == col[x-1]:
            count += 1
            if count > max_count:
                max_count = count
        else:
            count = 1
    return max_count

maps = []
for i in range(n):
    maps.append(input())
results = []
for i in range(n):
    temp = ''
    for each in maps:
        temp += each[i]
    results.append(calc(temp))

print(max(results))
