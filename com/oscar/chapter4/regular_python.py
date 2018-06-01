# Python 与正则
# 上一节讲解了正则表达式的语法和应用, 对于不同的编程语言来说, 对正则表达式的语法
# 绝大部分语言都是支持的, 但是还是略有不同, 每种编程语言都有一些独特的匹配规则,
# Python 也不例外.
# 语法            含义                       表达式示例      完整匹配的字符串
# \A         仅匹配字符串开头                \Aabc               abc
# \Z         仅匹配字符串末尾                abc\Z               abc
# (?P<name>) 分组, 除了原有编号外再指        (?P<word>abc){2}    abcabc
#            定一个额外的别名
# (?P=name)  引用别名为<name>的分组匹配      (?P<id>\d)abc(?P-id) 1abc1
#            到的                                                5abc5
# 在讲 Python 对正则表达式的实现之前, 首先让说一下反斜杠问题. 正则表达式里使用
# "\" 作为转义符, 这就可能造成反斜杠困扰. 假如你需要匹配文本中的字符 "\", 那么
# 使用编程语言表示的正则表达式里将需要4个反斜杠 "\\\\": 前两个和后两个分别用于
# 在编程语言里转义成反斜杠, 转换成两个反斜杠后再在正则表达式里转义成一个反斜杠.
# 但是 Python 提供了对原生字符串的支持, 从而解决了这个问题. 匹配一个 '\' 的正
# 则表达式可以写为 r'\\', 同样, 匹配一个数字的 '\\d' 可以写成 r'\d'.
# Python 通过 re 模块提供对正则表达式的支持. 使用 re 的一般步骤是先将正则表达式
# 的字符串形式编译为 Pattern 实例, 然后使用 Pattern 实例处理文本并获得匹配结果,
# 最后使用 Match 实例获得信息, 进行其他操作. 主要用到的方法列举如下:
# re.compile(string[,flag])
# re.match(pattern, string[,flags])
# re.search(pattern, string[,flagsl])
# re.split(pattern, string[, maxsplit])
# re.findall(pattern, string[,flags])
# re.finditer(pattern, string[,flags])
# re.sub(pattern, repl, string[,count])
# re.subn(pattern, repl, string[,count])

# 首先说一下 re 中 compile 函数, 它将一个正则表达式的字符串转化为 Pattern 匹配对象.
# 示例如下:
# pattern = re.compile(r'\d+')
# 这会生成一个匹配数字的 pattern 对象, 用来给接下来的函数作为参数, 进行进一步的搜索操作.
# 大家发现其他几个函数中, 还有一个 flag 参数. 参数 flag 是匹配模式, 取值可以使用按位或
# 运算符 "|" 表示同时生效, 比如 re.I|re.M. flag 的可选值如下: