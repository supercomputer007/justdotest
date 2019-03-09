# 1. 北京出租车计价程序
#     收费标准:
#       3公里以内收费13元
#       基本单价 2.3元/公里(超出3公里以外)
#       空驶费: 超过15公里后,每公里加收单价的50%空驶费(即:
#           15公里后为 3.45元/公里)
#     要求:
#       输入公里数,打印出费用金额(以元为单位,精确到分,分以后四舍
#       五入)
# while True:
#
#         n = input('请输入公里数,回车键退出：')
#         if not n:
#             break
#         try:
#              miles = int(n)
#         except ValueError:
#             print('你输入的不合法，请重新输入')
#             continue
#         if miles <= 3 :
#             fee = 13
#         elif miles <= 15 :
#             fee = 13 + 2.3 * ( miles - 3 )
#         else :
#             fee = 13 + 2.3*(15-3)+(miles-15)*3.15
#         print('出租车费用为',fee)

  # 2. 写程序,任意给出三个数,打印出三个数中最大的一个数
# while True:
#     a = input('请输入第一个数字,回车键退出：')
#     if not a :
#         break
#     b = input('请输入第二个数字,回车键退出：')
#     if not b :
#         break
#     c = input('请输入第三个数字,回车键退出：')
#     if not a :
#         break
#     try :
#         n1 = int(a)
#         n2 = int(b)
#         n3 = int(c)
#     except ValueError:
#         print('你的输入的数字不合法请重新输入')
#         continue
#     max1 = n1
#     if n2 > max1 :
#         max1 = n2
#     if n3 > max1 :
#         max1 = n3
#     print('最大数为：',max1)




# 3. BMI 指数(Body Mass Index) 又称身体质量指数
#     BMI值计算公式: BMI = 体重(公斤) / 身高的平方(米)
#     如:
#       一个69公斤的人,身高是173公分
#       BMI = 69/1.73**2  得 23.05
#     标准表:
#       BMI < 18.5 体重过轻
#       18.5 <= BMI < 24 正常范围
#       BMI > 24   体重过重
#     输入身高和体重,打印出BMI的值,并打印出体重状况

while True:
    h = input('请输入身高（M）,回车键退出：')
    if not h:
        break
    w = input('请输入体重(KG)，回车键退出')
    if not w:
        break
    try:
        high = float(h)
    except ValueError:
        print('你输入的身高数据不合法，请重新输入：')
        continue
    try:
        weight = float(w)
    except ValueError:
        print('你输入的体重数据不合法，请重新输入：')
        continue
    BMI = weight / high ** 2
    if BMI <18.5:
        print('体重过轻，请多吃饭')
    elif BMI < 24:
        print('身材完美,请保持住')
    else :
        print('体重超标，别在吃了')


