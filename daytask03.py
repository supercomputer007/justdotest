# 1. 给出一个年份,判断是否为闰年并打印
#     规则:
#       每四年一闰,每百年不闰,每四百年又闰
#     如:
#       2016年  闰年
#       2100年  不是闰年
#       2400年  是闰年
#     输入一个年份,打印这一年是否是闰年


# while True:
#     n = input('请输入年份，回车退出：')
#     if not n :
#         break
#     try :
#         year = int(n)
#     except ValueError:
#         print('你的输入数字不合法请重新输入')
#         continue
#     if year % 4 == 0:
#         if year % 100 == 0 and year % 400 != 0:
#             print(year,'是平年')
#         else:
#             print(year,'是闰年')
#     else:
#         print(year,'是平年')


# 2. 输入一个字符串,把输入的字符串中的空格全部去掉,打印出处理
#      后的字符串的长度和字符串的内容
# while True:
#     s=input('请输入字符串,回车退出：')
#     if not s:
#         break
#     a=''
#     for i in s:
#         if i is ' ':
#             pass
#         else:
#             a += i
#     print("去掉空格的字符串为",a)


# 3.
# 输入三行文字, 让这三行文字在一个方框居中显示
# (注: 不要输入中文)
# 如输入:
# hello!
# I'm studing python!
# I like python!
# 打印如下:
    # +---------------------+
    # | hello! |
    # | I'm studing python! |
    # | I likepython! |
    # +---------------------+

a = 'hello'
b = "I'm studing python"
c = 'I like python'
print('+','-'*21,'+')
print('|',a.center(21),'|')
print('|',b.center(21),'|')
print('|',c.center(21),'|')
print('+','-'*21,'+')


