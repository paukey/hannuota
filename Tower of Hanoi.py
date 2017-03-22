#paukey
#pytyhon 3.5
#2017年3月22日
#http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431756044276a15558a759ec43de8e30eb0ed169fb11000
"""
汉诺塔的移动可以用递归函数非常简单地实现。

请编写move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法
"""
def move (n,a,b,c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n - 1, a, c, b)  # 将前n-1个盘子从x移动到y上
        move(1, a, b, c)  # 将最底下的最后一个盘子从x移动到z上
        move(n - 1, b, a, c)  # 将y上的n-1个盘子移动到z上



n = int(input('请输入汉诺塔的层数：'))
move(n, 'x', 'y', 'z')

"""
# 利用递归函数移动汉诺塔:
def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
        return
    move(n-1, a, c, b)
    print('move', a, '-->', c)
    move(n-1, b, a, c)

move(4, 'A', 'B', 'C')
"""