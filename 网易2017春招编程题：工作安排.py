'''
[编程题] 工作安排
时间限制：1秒
空间限制：32768K
现在有n位工程师和6项工作(编号为0至5)，现在给出每个人能够胜任的工作序号表
(用一个字符串表示，比如：045，表示某位工程师能够胜任0号，4号，5号工作)。
现在需要进行工作安排，每位工程师只能被安排到自己能够胜任的工作当中去，两位工程师不能安排到同一项工作当中去。
如果两种工作安排中有一个人被安排在的工作序号不一样就被视为不同的工作安排，现在需要计算出有多少种不同工作安排计划。 
输入描述:
输入数据有n+1行： 第一行为工程师人数n(1 ≤ n ≤ 6) 接下来的n行，
每行一个字符串表示第i(1 ≤ i ≤ n)个人能够胜任的工作(字符串不一定等长的)


输出描述:
输出一个整数，表示有多少种不同的工作安排方案

输入例子1:
6 012345 012345 012345 012345 012345 012345

输出例子1:
720
'''

'''
解题思路：深度优先搜索（dfs）
  本题给的数据量比较小，直接用暴力dfs搜索做
  每一层dfs都在每一个工程师能完成的任务中按顺序取出1个，加入集合中
  等到dfs遍历完所有工程师后，查看集合中工作数，如果等于工程师的个数，则方案有效，返回1，否则返回0
'''

'''
代码运行结果：
答案正确:恭喜！您提交的程序通过了所有的测试用例
'''

n = int(input())

jobs = []
for i in range(n):
    jobs.append([int(each) for each in input()])


def dfs(index, current_job, job_list):
    if index < n:
        each_eng = job_list[index]
        temp = 0
        for each_job in each_eng:
            temp_job = current_job.copy()
            temp_job.add(each_job)
            temp += dfs(index+1, temp_job, job_list)
        return temp
    else:
        if len(current_job) == n:
            return 1
        else:
            return 0

init_job = set()
print(dfs(0, init_job, jobs))
