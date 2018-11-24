# -*-coding:utf-8-*-

import time  # 引入time模块
import datetime

if __name__ == "__main__":
    print("----1.获取当前日期时间")
    localtime = time.localtime(time.time())
    ticks = time.time()
    print(type(localtime), "本地日期时间为 :", localtime)
    print(type(ticks), "本地日期时间戳为 :", ticks)
    print("----2.日期时间转化成字符串")
    timestr = time.strftime("%Y-%m-%d %H:%M:%S", localtime)
    print(type(timestr), timestr)
    print("----3.时间戳转化成字符串")
    timestr = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(ticks))
    print(type(timestr), timestr)
    print("----4.字符串转日期时间")
    localtime = time.strptime("2016-11-15 15:32:12", "%Y-%m-%d %H:%M:%S")
    print(type(localtime), localtime)
    print("----5.字符串转日期时间戳")
    ticks = time.mktime(time.strptime("2015-11-15 15:32:12", "%Y-%m-%d %H:%M:%S"))
    print(type(ticks), ticks)
    print("----6.日期时间转日期时间戳")
    ticks = time.mktime(localtime)
    print(type(ticks), ticks)
    print("----7.日期时间戳转日期时间")
    localtime = time.localtime(ticks)
    print(type(localtime), localtime)
    print("----8.获取当前日期时间")
    now = datetime.datetime.now()
    print(type(now), "本地日期时间为 :", now)
    print("----9.日期时间转字符串")
    nowstr = now.strftime("%Y-%m-%d %H:%M:%S")
    print(type(nowstr), nowstr)
    print("----10.日期时间转时间戳")
    un_timetemp = now.timetuple()
    un_time = time.mktime(un_timetemp)
    print(type(un_time), un_time)
    print("----11.字符串转日期时间")
    d1 = datetime.datetime.strptime('2017-10-16 19:21:22', '%Y-%m-%d %H:%M:%S')
    print(type(d1), d1)
    print("----12.时间戳转日期时间")
    unix_ts = 1509636585.0
    times = datetime.datetime.fromtimestamp(unix_ts)
    print(type(times), times)
    print("----13.时间戳转字符串")
    unix_ts = 1509636585.0
    times = datetime.datetime.fromtimestamp(unix_ts).strftime("%Y-%m-%d %H:%M:%S")
    print(type(times), times)
    print("----14.字符串转时间戳")
    d1 = datetime.datetime.strptime('2018-10-16 19:21:22', '%Y-%m-%d %H:%M:%S')
    un_timetemp = d1.timetuple()
    un_time = time.mktime(un_timetemp)
    print(type(un_time), un_time)
# %y 两位数的年份表示（00-99）
# %Y 四位数的年份表示（000-9999）
# %m 月份（01-12）
# %d 月内中的一天（0-31）
# %H 24小时制小时数（0-23）
# %I 12小时制小时数（01-12）
# %M 分钟数（00=59）
# %S 秒（00-59）
#
# %a 本地简化星期名称
# %A 本地完整星期名称
# %b 本地简化的月份名称
# %B 本地完整的月份名称
# %c 本地相应的日期表示和时间表示
# %j 年内的一天（001-366）
# %p 本地A.M.或P.M.的等价符
# %U 一年中的星期数（00-53）星期天为星期的开始
# %w 星期（0-6），星期天为星期的开始
# %W 一年中的星期数（00-53）星期一为星期的开始
# %x 本地相应的日期表示
# %X 本地相应的时间表示
# %Z 当前时区的名称
# %% %号本身
