'''
编程题] 赶去公司
时间限制：1秒
空间限制：32768K
终于到周末啦！小易走在市区的街道上准备找朋友聚会，突然服务器发来警报,
小易需要立即回公司修复这个紧急bug。假设市区是一个无限大的区域，每条街道假设坐标是(X，Y)，
小易当前在(0，0)街道，办公室在(gx,gy)街道上。小易周围有多个出租车打车点，小易赶去办公室有两种选择，
一种就是走路去公司，另外一种就是走到一个出租车打车点，然后从打车点的位置坐出租车去公司。
每次移动到相邻的街道(横向或者纵向)走路将会花费walkTime时间，打车将花费taxiTime时间。
小易需要尽快赶到公司去，现在小易想知道他最快需要花费多少时间去公司。 
输入描述:
输入数据包括五行:
 第一行为周围出租车打车点的个数n(1 ≤ n ≤ 50)
 第二行为每个出租车打车点的横坐标tX[i] (-10000 ≤ tX[i] ≤ 10000)
 第三行为每个出租车打车点的纵坐标tY[i] (-10000 ≤ tY[i] ≤ 10000)
 第四行为办公室坐标gx,gy(-10000 ≤ gx,gy ≤ 10000),以空格分隔
 第五行为走路时间walkTime(1 ≤ walkTime ≤ 1000)和taxiTime(1 ≤ taxiTime ≤ 1000),以空格分隔


输出描述:
输出一个整数表示，小易最快能赶到办公室的时间

输入例子1:
2 -2 -2 0 -2 -4 -2 15 3

输出例子1:
42
'''

'''
解题思路：简单
   考虑所有情况：计算直接步行去公司，去任意一个点打车去公司的时间，输出最少的用时
'''

'''
代码运行结果：
答案正确:恭喜！您提交的程序通过了所有的测试用例
'''

taxi_num = int(input())
taxi_x_cords = [int(each) for each in input().split()]
taxi_y_cords = [int(each) for each in input().split()]
com_add = [int(each) for each in input().split()]
walk_time, taxi_time = [int(each) for each in input().split()]

time = list()
time.append((abs(com_add[0])+abs(com_add[1]))*walk_time)

for i in range(taxi_num):
    x = taxi_x_cords[i]
    y = taxi_y_cords[i]
    time.append((abs(x)+abs(y))*walk_time+(abs(x-com_add[0])+abs(y-com_add[1]))*taxi_time)

print(min(time))
