import random

# 雨点黑线生成器
# 很烂，而且是我为了写雨点黑线手搓的代码
# 不会控制黑线只出现在FTR梯形界内，只能控制出现在矩形界内，我是垃圾
# 更新：现在搓了一会终于能梯形了
# 而且还有各种浮点问题，比如出来一个什么0.000000000003坐标
# 我已经尝试修过浮点问题了但是修不好...我是垃圾

# 设置雨点黑线开始时间（毫秒）
start = 116521
# 设置每一段雨点的持续时间（把下面的64改成你想要的持续毫秒数）
end = (start + 64)
# 设置雨点黑线的时段数量（把16改掉）
for __count in range(16):
    # 设置同时有多少雨点黑线（把3改掉）
    for __count in range(3):
        # 设置雨点黑线出现位置区间（y坐标乘以100）
        y100 = random.randint(0, 100)
        y = (y100 * 0.01)
        # 注意！这里0.5是控制梯形上底长度，FTR为0.5，BYD为0.25，矩形为0
        # 总之这里的意思是x的大小和梯形上底削减长度的关系
        # 还是不懂就直接品鉴一下这个屎山
        triangle = (y100 * 0.5)
        x100min = (-50 + triangle)
        x100max = (150 - triangle)
        x100minint = int(x100min)
        x100maxint = int(x100max)
        x100 = random.randint(x100minint,x100maxint)
        x = (x100 * 0.01)
        List = ['arc(', str(start), ',', str(end), ',', str(x), ',', str(x), ',', 's,', str(y), ',', str(y), ',0,none,true);']
        print("".join(List))
    start = end
    # 设置相邻两个时段的雨点头部时间差，不是尾部到头部的时间差！
    end = (start + 64)


