'''
[编程题] 消除重复元素
时间限制：1秒
空间限制：32768K
小易有一个长度为n序列，小易想移除掉里面的重复元素，但是小易想是对于每种元素保留最后出现的那个。
小易遇到了困难,希望你来帮助他。 
输入描述:
输入包括两行： 第一行为序列长度n(1 ≤ n ≤ 50) 第二行为n个数sequence[i](1 ≤ sequence[i] ≤ 1000)，以空格分隔


输出描述:
输出消除重复元素之后的序列，以空格分隔，行末无空格

输入例子1:
9 100 100 100 99 99 99 100 100 100

输出例子1:
99 100
'''

'''
解题思路：简单
   建立一个新的列表来存储去重后的数据，遍历所有输入的元素，如果遍历到的元素没在新列表中，则把它放入新列表中，
   如果在新列表中，则删除新列表中的原有元素，把该元素放入新列表的末尾
'''

'''
代码运行结果：
答案正确:恭喜！您提交的程序通过了所有的测试用例
'''

n = int(input())
seq = [int(each) for each in input().split()]

new_seq = []

for each in seq:
    if each not in new_seq:
        new_seq.append(each)
    else:
        new_seq.remove(each)
        new_seq.append(each)

print(' '.join([str(each) for each in new_seq]))
