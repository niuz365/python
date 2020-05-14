# 导入keyword
import keyword
print(keyword.kwlist, end="||\r\n")

#遍历关键字
print("---- 遍历关键字 ----")
for kw in keyword.kwlist:
  print(kw, end=", ")
print("")
print("===============================")

# complex类型
"""
复数是由一个实数和一个虚数组合构成，j是虚部的标志符号
"""
print("---- complex类型 ----")
cp1 = 1+2j
cp2 = 2+3j
cp3 = cp1 + cp2
print(cp3)
print("===============================")


#基础类型
print("---- 基础类型 ----")
a,b,c,d=1,2.0,True,3+4j
print(a, b, c, d)
print(type(a), type(b), type(c), type(d))
print(isinstance(a, float))
print(isinstance(c, bool))
print(isinstance(d, complex))

# 数值计算
print("---- 数值计算 ----")
m, n = 17, 3
print("m, n = 17, 3")
print("m + n", end=" = ")
print(m + n)
print("m - n", "=", m - n)
print("m * n = " + str(m*n))
print("m ** n", end=" = ")
print(m ** n)
print("m / n", end=" = ")
print(m / n)
print("m // n", end=" = ")
print(m // n)
print("m % n", end=" = ")
print(m % n)

#字符串截取
s = "字符串截取实例"
'''
字符串截取的逻辑，左边是从0开始，逐渐增加，右边也是从0开始，逐渐减少
可以认为字符串的index是在单个字符的右边，如下：
0字1符2串3截4取5实6例
字-6符-5串-4截-3取-2实-1例
'''
print("---- 字符串截取 ----")
print("s[0:]")
print(s[0:])
print("s[0:-1]")
print(s[0:-1])
print("s[0:-2]")
print(s[0:-2])
print("s[1:-3]")
print(s[1:-3])
print("s[0:2]")
print(s[0:2])
print("s[1:4]")
print(s[1:4])
print("s[-5:-2]")
print(s[-5:-2])
print("s[-5:-2]*3")
print(s[-5:-2]*3)

#转义字符
print("---- 转义字符 ----")
s = "hello,\nworld."
print(s)
s = r"hello,\nworld."
print(s)