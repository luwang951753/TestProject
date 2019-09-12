#! user/bin/python3
# -*- coding:utf-8 -*-

# Python3 运算符
# Python语言支持以下类型的运算符:

# 算术运算符
# 比较（关系）运算符
# 赋值运算符
# 逻辑运算符
# 位运算符
# 成员运算符
# 身份运算符
# 运算符优先级






# Python算术运算符
# 以下假设变量a为10，变量b为21：
# 运算符	                                              描述	                                                 实例
# +	                                                     加 - 两个对象相加	                                     a + b 输出结果 31
# -	                                                     减 - 得到负数或是一个数减去另一个数	                   a - b 输出结果 -11
# *	                                                     乘 - 两个数相乘或是返回一个被重复若干次的字符串	        a * b 输出结果 210
# /	                                                     除 - x 除以 y	                                         b / a 输出结果 2.1
# %	                                                     取模 - 返回除法的余数	                                  b % a 输出结果 1
# **	                                                 幂 - 返回x的y次幂	                                      a**b 为10的21次方
# //	                                                 取整除 - 向下取接近除数的整数	                           9//2 = 4     -9//2 = -5
print("===========================1===========================")
a = 21
b = 10
c = 0

c = a + b
print ("1 - c 的值为：", c)
 
c = a - b
print ("2 - c 的值为：", c)
 
c = a * b
print ("3 - c 的值为：", c)
 
c = a / b
print ("4 - c 的值为：", c)
 
c = a % b
print ("5 - c 的值为：", c)
 
# 修改变量 a 、b 、c
a = 2
b = 3
c = a**b 
print ("6 - c 的值为：", c)
 
a = 10
b = 5
c = a//b 
print ("7 - c 的值为：", c)








# Python比较运算符
# 以下假设变量a为10，变量b为20：
# 运算符	                                     描述	                                                         实例
# ==	                                        等于 - 比较对象是否相等	                                          (a == b) 返回 False
# !=	                                        不等于 - 比较两个对象是否不相等	                                   (a != b) 返回 True
# >	                                            大于 - 返回x是否大于y	                                          (a > b) 返回 False
# <	                                            小于 - 返回x是否小于y                                             (a < b) 返回 True
# >=	                                        大于等于 - 返回x是否大于等于y                                      (a >= b) 返回 False
# <=	                                        小于等于 - 返回x是否小于等于y                                      (a <= b) 返回 True
# 注意:所有比较运算符返回1表示真，返回0表示假。这分别与特殊的变量True和False等价。注意，这些变量名的大写
print("===========================2===========================")
a = 21
b = 10
c = 0
 
if ( a == b ):
   print ("1 - a 等于 b")
else:
   print ("1 - a 不等于 b")
 
if ( a != b ):
   print ("2 - a 不等于 b")
else:
   print ("2 - a 等于 b")
 
if ( a < b ):
   print ("3 - a 小于 b")
else:
   print ("3 - a 大于等于 b")
 
if ( a > b ):
   print ("4 - a 大于 b")
else:
   print ("4 - a 小于等于 b")
 
# 修改变量 a 和 b 的值
a = 5;
b = 20;
if ( a <= b ):
   print ("5 - a 小于等于 b")
else:
   print ("5 - a 大于  b")
 
if ( b >= a ):
   print ("6 - b 大于等于 a")
else:
   print ("6 - b 小于 a")





# Python赋值运算符
# 以下假设变量a为10，变量b为20：

# 运算符	                                       描述	                             实例
# =	                                              简单的赋值运算符	                  c = a + b 将 a + b 的运算结果赋值为 c
# +=	                                          加法赋值运算符	                  c += a 等效于 c = c + a
# -=	                                          减法赋值运算符	                  c -= a 等效于 c = c - a
# *=	                                          乘法赋值运算符	                  c *= a 等效于 c = c * a
# /=	                                          除法赋值运算符	                  c /= a 等效于 c = c / a
# %=	                                          取模赋值运算符	                  c %= a 等效于 c = c % a
# **=	                                          幂赋值运算符	                      c **= a 等效于 c = c ** a
# //=	                                          取整除赋值运算符	                  c //= a 等效于 c = c // a
print("===========================3===========================")
a = 21
b = 10
c = 0
 
c = a + b
print ("1 - c 的值为：", c)
 
c += a
print ("2 - c 的值为：", c)
 
c *= a
print ("3 - c 的值为：", c)
 
c /= a 
print ("4 - c 的值为：", c)
 
c = 2
c %= a
print ("5 - c 的值为：", c)
 
c **= a
print ("6 - c 的值为：", c)
 
c //= a
print ("7 - c 的值为：", c)







# Python位运算符
# 按位运算符是把数字看作二进制来进行计算的。Python中的按位运算法则如下：
# 下表中变量 a 为 60，b 为 13二进制格式如下：
# a = 0011 1100
# b = 0000 1101
# -----------------

# a&b = 0000 1100
# a|b = 0011 1101
# a^b = 0011 0001
# ~a  = 1100 0011

# 运算符	      描述	                                                                                         实例
# &	             按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0	                          (a & b) 输出结果 12 ，二进制解释： 0000 1100
# |	             按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1 	                                     (a | b) 输出结果 61 ，二进制解释： 0011 1101
# ^	             按位异或运算符：当两对应的二进位相异时，结果为1	                                                (a ^ b) 输出结果 49 ，二进制解释： 0011 0001
# ~	             按位取反运算符：对数据的每个二进制位取反,即把1变为0,把0变为1 ~x 类似于 -x-1	                     (~a ) 输出结果 -61 ，二进制解释： 1100 0011， 在一个有符号二进制数的补码形式。
# <<	         左移动运算符：运算数的各二进位全部左移若干位，由"<<"右边的数指定移动的位数，高位丢弃，低位补0。	    a << 2 输出结果 240 ，二进制解释： 1111 0000
# >>	         右移动运算符：把">>"左边的运算数的各二进位全部右移若干位，">>"右边的数指定移动的位数	               a >> 2 输出结果 15 ，二进制解释： 0000 1111
# 注意: ~x类似于-x-1 可以这么理解: x->-x是x取反加一(-x = ~x+1)  那么 ~x就相当于-x-1 有时候不好理解的东西  可以换个思维理解
print("===========================4===========================")
a = 60            # 60 = 0011 1100 
b = 13            # 13 = 0000 1101 
c = 0
 
c = a & b;        # 12 = 0000 1100
print ("1 - c 的值为：", c)
 
c = a | b;        # 61 = 0011 1101 
print ("2 - c 的值为：", c)
 
c = a ^ b;        # 49 = 0011 0001
print ("3 - c 的值为：", c)
 
c = ~a;           # -61 = 1100 0011
print ("4 - c 的值为：", c)
 
c = a << 2;       # 240 = 1111 0000
print ("5 - c 的值为：", c)
 
c = a >> 2;       # 15 = 0000 1111
print ("6 - c 的值为：", c)





# Python逻辑运算符
# Python语言支持逻辑运算符，以下假设变量 a 为 10, b为 20:

# 运算符	         逻辑表达式	          描述	                                                                          实例
# and	            x and y	            布尔"与" - 如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值	           (a and b) 返回 20。
# or	            x or y	            布尔"或" - 如果 x 是 True，它返回 x 的值，否则它返回 y 的计算值	                    (a or b) 返回 10。
# not	            not x	            布尔"非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True           	   not(a and b) 返回 False
# 注意:
# python 中的 and 从左到右计算表达式，若所有值均为真，则返回最后一个值，若存在假，返回第一个假值
# or 也是从左到有计算表达式，返回第一个为真的值
# 其中数字 0 是假，其他都是真
# 字符 "" 是假，其他都是真
print("===========================5===========================")
a = 10
b = 20
print(a and b)
print(a or b) 
if ( a and b ):
   print ("1 - 变量 a 和 b 都为 true")
else:
   print ("1 - 变量 a 和 b 有一个不为 true")
 
if ( a or b ):
   print ("2 - 变量 a 和 b 都为 true，或其中一个变量为 true")
else:
   print ("2 - 变量 a 和 b 都不为 true")
 
# 修改变量 a 的值
a = 0
print(a and b)
print(a or b)
if ( a and b ):
   print ("3 - 变量 a 和 b 都为 true")
else:
   print ("3 - 变量 a 和 b 有一个不为 true")
 
if ( a or b ):
   print ("4 - 变量 a 和 b 都为 true，或其中一个变量为 true")
else:
   print ("4 - 变量 a 和 b 都不为 true")
 
if not( a and b ):
   print ("5 - 变量 a 和 b 都为 false，或其中一个变量为 false")
else:
   print ("5 - 变量 a 和 b 都为 true")








# Python成员运算符
# 除了以上的一些运算符之外，Python还支持成员运算符，测试实例中包含了一系列的成员，包括字符串，列表或元组

# 运算符	           描述	                                                    实例
# in	              如果在指定的序列中找到值返回 True，否则返回 False	          x 在 y 序列中 , 如果 x 在 y 序列中返回 True
# not in	          如果在指定的序列中没有找到值返回 True，否则返回 False	      x 不在 y 序列中 , 如果 x 不在 y 序列中返回 True
print("===========================6===========================")
a = 10
b = 20
list = [1, 2, 3, 4, 5 ];
 
if ( a in list ):
   print ("1 - 变量 a 在给定的列表中 list 中")
else:
   print ("1 - 变量 a 不在给定的列表中 list 中")
 
if ( b not in list ):
   print ("2 - 变量 b 不在给定的列表中 list 中")
else:
   print ("2 - 变量 b 在给定的列表中 list 中")
 
# 修改变量 a 的值
a = 2
if ( a in list ):
   print ("3 - 变量 a 在给定的列表中 list 中")
else:
   print ("3 - 变量 a 不在给定的列表中 list 中")








# Python身份运算符
# 身份运算符用于比较两个对象的存储单元

# 运算符	         描述	                                               实例
# is	            is 是判断两个标识符是不是引用自一个对象	                 x is y, 类似 id(x) == id(y) , 如果引用的是同一个对象则返回 True，否则返回 False
# is not	        is not 是判断两个标识符是不是引用自不同对象	             x is not y ， 类似 id(a) != id(b)。如果引用的不是同一个对象则返回结果 True，否则返回 False
# 注： id() 函数用于获取对象内存地址
print("===========================7===========================")
a = 20
b = 20
 
if ( a is b ):
   print ("1 - a 和 b 有相同的标识")
else:
   print ("1 - a 和 b 没有相同的标识")
 
if ( id(a) == id(b) ):
   print ("2 - a 和 b 有相同的标识")
else:
   print ("2 - a 和 b 没有相同的标识")
 
# 修改变量 b 的值
b = 30
if ( a is b ):
   print ("3 - a 和 b 有相同的标识")
else:
   print ("3 - a 和 b 没有相同的标识")
 
if ( a is not b ):
   print ("4 - a 和 b 没有相同的标识")
else:
   print ("4 - a 和 b 有相同的标识")








# Python运算符优先级
# 以下表格列出了从最高到最低优先级的所有运算符：
# 运算符	                        描述
# **	                           指数 (最高优先级)
# ~ + -	                           按位翻转, 一元加号和减号 (最后两个的方法名为 +@ 和 -@)  最后这两个符号不理解
# * / % //	                       乘，除，取模和取整除
# + -	                           加法减法
# >> <<	                           右移，左移运算符
# &	                               位 'AND'
# ^ |	                           位运算符
# <= < > >=	                       比较运算符
# <> == !=	                       等于运算符
# = %= /= //= -= += *= **=	       赋值运算符
# is is not	                       身份运算符
# in not in	                       成员运算符
# not and or	                   逻辑运算符 优先级：not>and>or
print("===========================8===========================")
a = 20
b = 10
c = 15
d = 5
e = 0
 
e = (a + b) * c / d       #( 30 * 15 ) / 5
print ("(a + b) * c / d 运算结果为：",  e)
 
e = ((a + b) * c) / d     # (30 * 15 ) / 5
print ("((a + b) * c) / d 运算结果为：",  e)
 
e = (a + b) * (c / d);    # (30) * (15/5)
print ("(a + b) * (c / d) 运算结果为：",  e)
 
e = a + (b * c) / d;      #  20 + (150/5)
print ("a + (b * c) / d 运算结果为：",  e)

# 一个示例说明的一个问题
print("===========================9===========================")
b = 5000  
a = 5000 
print(id(a))     # 140735059489152
print(id(b))     # 140735059489152
# 可以看出， python 中，变量是以内容为基准而不是像 c 中以变量名为基准，所以只要你的数字内容是5，不管你起什么名字，这个变量的 ID 是相同的，同时也就说明了 python 中一个变量可以以多个名称访问
# 这样的设计逻辑决定了 python 中数字类型的值是不可变的，因为如果如上例，a 和 b 都是 5，当你改变了 a 时，b 也会跟着变，这当然不是我们希望的
# 因此，正确的自增操作应该 a = a + 1 或者 a += 1，当此 a 自增后，通过 id() 观察可知，id 值变化了，即 a 已经是新值的名9






# == 和 is 的区别
# is 判断两个对象是否为同一对象, 是通过 id 来判断的; 当两个基本类型数据(或元组)内容相同时, id 会相同, 但并不代表 a 会随 b 的改变而改变
# == 判断两个对象的内容是否相同, 是通过调用 __eq__() 来判断的
# 1、当列表，元组，字典中的值都引用 a,b 时，总是返回 True，不受 a,b 值大小的影响
print("===========================10===========================")
a=1000
b=1000
list1=[a,3,5]
list2=[b,4,5]
print(list1[0] is list2[0])
tuple1=(a,3,5)
tuple2=(b,4,5)
print(tuple1[0] is tuple2[0])
dict1={6:a,2:3,3:5}
dict2={1:b,2:4,3:7}
print(dict1[6] is dict2[1])
# 2、当不引用a,b，直接用具体值来测试时，列表，字典，不受值大小影响，返回True，元组则受 256 值范围的影响，超出范围则地址改变，返回 False
print("===========================11===========================")
list1=[1000,3,5]
list2=[1000,4,5]
print(list1[0] is list2[0])
tuple1=(1000,3,5)
tuple2=(1000,4,5)
print(tuple1[0] is tuple2[0])
dict1={6:1000,2:3,3:5}
dict2={1:1000,2:4,3:7}
print(dict1[6] is dict2[1])
# 3、当直接用列表、元组、字典本身来测试时，刚好相反，元组返回 True，列表，字典返回 False
print("===========================12===========================")
list1=[1000,3,5]
list2=[1000,3,5]
print(list1 is list2)
tuple1=(1000,3,5)
tuple2=(1000,3,5)
print(tuple1 is tuple2)
dict1={1:1000,2:3,3:5}
dict2={1:1000,2:3,3:5}
print(dict1 is dict2)




