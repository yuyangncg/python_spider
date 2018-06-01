# 正则表达式
# 在编写处理网页文本程序时, 经常会有查找符合某些复杂规则的字符串的需要.
# 正则表达式就是用于描述这些规则的工具. 正则表达式是由普通字符(例如字符
# a 到 z)以及特殊字符(称为'元字符')组成的文字模式. 模式用于描述在搜索文本
# 时要匹配的一个或多个字符串. 正则表达式作为一个模板, 将某个字符模式与所
# 搜索的字符串进行匹配.

# 入门小例子:
# "\b" 是正则表达式规定的一个特殊代码, 被称为元字符, 代表着单词的开头或结尾,
# 也就是单词的分界处, 它不代表英语中空格、标点符号、换行等单词分隔符, 只是
# 用来匹配一个位置, 这种理解方式很关键.
# "." 这个元字符的含义是匹配除了换行符的任意字符.
# "*" 元字符不是代表字符, 而是代表数量, 含义是 "*" 前面的内容可以连续重复
# 任意次使得整个表达式被匹配.
# ".*" 整体的意思就非常明显了, 表示可以匹配任意数量不换行的字符.

# 常见元字符:
# "."  匹配除换行符以外的任意字符.
# "\b" 匹配单词的开始或结束.
# "\d" 匹配数字
# "\w" 匹配字母、数字、下划线或汉字.
# "\s" 匹配任意空白符, 包括空格、制表符（Tab）、换行符、中文全角空格等.
# "^"  匹配字符串的开始.
# "$"  匹配字符串的结束.

# 字符转义:
# 如果你想查找元字符本身的话, 比如你查找 "." 或者 "*" 就会出现问题, 因为他们
# 具有特定功能, 没办法把他们指定为普通字符. 这个时候就需要用到转义, 使用 "\"
# 来取消这些字符的特殊意义. 因此如果查找 "."、"\" 或者 "*" 时, 必须写成 "\."、
# "\\" 和 "\*". 例如匹配 www.google.com 这个网址时, 表达式可以写为 www.\.google\.com.

# 重复:
# "*"     重复零次或者更多次.
# "+"     重复一次或更多次.
# "?"     重复零次或一次.
# "{n}"   重复n次.
# "{n,}"  重复n次或更多次.
# "{n,m}" 重复n次到m次.
# 下面是一些重复的例子:
# hello\d+: 匹配 hello 后面跟1个或更多数字, 例如可以匹配hello1、hello10等情况.
# ^\d{5,12}$: 匹配5到12个数字的字符串, 例如QQ号符合要求.
# we\d?: 匹配we后面跟0个或者一个数字, 例如 we、we0符合情况.

# 字符集合:
# 通过上面介绍的元字符, 可以看到查找数字、字母或数字、空格是很简单的, 因为已经有了
# 对应这些字符的集合, 但是如果想匹配没有预定义元字符的字符集合, 例如匹配 a、b、c、
# d 和 e 中任意个字符, 这时候就需要自定义字符集合.正则表达式是通过"[]"来实现自定义
# 字符集合, "[abcd]"就是匹配"abcd"中的任意一个字符, "[.?!]"匹配标点符号("."、"?"或"!").
# 除了将需要自定义的字符都写入"[]"中, 还可以指定一个字符范围. "[0-9]"代表的含义与"\d"
# 是完全一致的, 代表一位数字; "[a-z0-9A-Z]"页完全等于"\w"(只考虑英文), 代表着26个字母中
# 的大小写、0-9的数字和下划线中的任意字符.

# 分支条件:
# 正则表达式里的分支条件指的是有几种匹配规则, 如果满足其中任意一种规则都应该当成匹配,
# 具体方法是用"|"把不同的规则分隔开. 例如匹配电话号码, 电话号码中一种是3位区号, 8位
# 本地号, 形如 010-11223344, 另一种是4位区号, 7位本地号, 形如 0321-1234567. 如果想把
# 电话号码匹配出来, 就需要用到分支条件: 0\d{2}-\d{8}|0\d{3}-\d{7}. 在分支条件中有一点
# 需要注意, 匹配分支条件时, 将会从左到右地测试每个条件, 如果满足了某个分支的话, 就不会去
# 再管其他条件了, 条件之间是一种或的关系, 例如从 1234567890 匹配除连续的4个数字或者连续
# 8个数字, 如果协程\d{4}|\d{8}, 其实\d{8}是失效的, 既然能匹配出来8位数字, 肯定就能匹配
# 出4位数字.

# 分组:
# 先以简单的 IP 地址匹配为;例子, 想匹配类似 192.168.1.1 这样的 IP 地址, 可以这样写正则
# 表达式((\d{1,3})\.){3}\d{1,3}. 下面分析一下这个正则表达式: \d{1,3}代表着1~3位的数字,
# ((\d{1,3})\.){3}代表着将1~3位数字加上一个"."重复3次, 匹配出类似192.168.1.这部分, 之后
# 再加上\d{1,3}, 表示1~3位的数字. 但是上述的正则表达式会匹配出类似333.444.555.666这些
# 不可能存在的 IP 地址, 因为 IP 地址中每个数字都不能大于255, 所以要写出一个完整的 IP 地址
# 匹配表达式还需要关注一下细节, 下面给出一个使用分组的完整 IP 表达式:
# ((25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.){3}((25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d))
# 其中的关键是(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)部分, 大家应该有能力分析出来.

# 反义:
# 有时需要查找除某一类字符集合之外的字符. 比如想查找除了数字以外, 包含其他任意字符的情况,
# 这时候就需要用到反义.
# \W           匹配任意不是字母、数字、下划线、汉字的字符.
# \S           匹配任意不是空白符的字符.
# \D           匹配任意非数字的字符.
# \B           匹配不是单词开头或结束的位置.
# [^a]         匹配除了a以外的任意字符.
# [^abcde]     匹配除了a、b、c、d、e这几个字母以外的任意字符.
# [^(123|abc)] 匹配除了1、2、3或者a、b、c这几个字符以外的任意字符.
# 例如 "\D+" 匹配非数字的一个或者多个字符.

# 后向引用:
# 前面我们讲到了分组, 使用小括号指定一个表达式就可以看做是一个分组. 默认情况下,
# 每个分组会自动拥有一个组号, 规则是: 从左向右, 以分组的左括号为标志, 第一个出现
# 的分组的组号为1, 第二个为2, 以此类推. 还是以简单的 IP 匹配表达式((\d{1,3})\.){3}\d{1,3}
# 为例, 这里面有两个分组1和2, 使用 Match Tracer 这个工具可以很明显的看出来.
# 所以上面的表达式可以改写成((\d{1,3})\.){3}\2.
# 你也可以自己指定子表达式的组名, 要指定一个子表达式的组名, 使用这样的语法:
# (?<Digit>\d+)或者(?'Digit'\d+), 这样就把 "\d+" 的组名指定为 Digit 了. 要反向引用这个
# 分组捕获的内容, 你可以使用 \k<Digit>, 所以上面的 IP 匹配表达式写成
# ((?<Digit>\d{1,3})\.){3}\k<Digit>. 使用小括号的地方很多, 主要是用来分组.
# 捕获      (exp)          匹配 exp, 并捕获文本到自动命名的组里.
#           (?<name>exp)   匹配 exp, 并捕获文本到名称为name的组里, 也可以写成(?'name'exp)
#           (?:exp)        匹配 exp, 不捕获匹配的文本, 也不给此分组分配组号.
# 零宽断言   (?=exp)        匹配 exp 前面的位置.
#           (?<=exp)       匹配 exp 后面的位置.
#           (?!exp)        匹配后面跟的不是 exp 的位置.
#           (?<!exp)       匹配前面不是 exp 的位置.
# 注释       (?#comment)   这种类型的分组不对正则表达式的处理产生任何影响, 只用于提供注释让人阅读.

# 在捕获这个表项里, 我们讲解了前两种用法, 还有(?:exp)没有进行讲解. (?:exp)不会改变正则表达式的处理方式,
# 只是这样的组所匹配的内容不会像前两种那样被捕获到某个组里面, 也不会拥有组号, 这样做有什么意义?
# 一般来说是为了节省资源, 提高效率. 比如说验证输入是否为整数, 可以这样写 ^([1-9][0-9]*|0)$.
# 这时候我们需要用到 "()" 来限制 "|" 表示 "或" 关系范围, 但我们只是要判断规则, 没必要把 exp 匹配的内容
# 保存到组里, 这时就可以用非捕获组了 ^(?:[1-9][0-9]*|0)$.

# 零宽断言:
# 零宽断言总共有四种形式. 前两种是正向零宽断言, 后两种是负向零宽断言. 什么是零宽断言呢?
# 我们知道元字符"\b"、"^"匹配的是一个位置, 而且这个位置需要满足一定的条件, 我们把这个条件
# 称为断言或零宽断言. 断言用来声明一个应该为真的事实, 正则表达式中只有当断言为真时才会继续进行
# 匹配. 可能大家感到有些抽象, 下面通过一些例子进行讲解.
# 首先说一下正向零宽断言的两种形式:
# 1) (?=exp) 叫零宽度正预测先行断言, 它断言此位置的后面能匹配表达式 exp. 比如 [a-z]*(?=ing) 匹配
# 以 ing 结尾的单词的前面部分 (除了 ing 以外的部分), 查找 I love cooking and singing 时会匹配出
# cook 与 sing. 先行断言的执行步骤应该是从要匹配字符的最右端找到第一个 "ing', 再匹配前面的表达式,
# 如无法匹配则查找第二个 "ing".
# 2) (?<exp) 叫零宽度正回顾后发断言, 它断言此位置的前面能匹配表达式 exp. 比如 (?<=abc).* 匹配以 abc
# 开头的字符串的后面部分, 可以匹配 abcdefgabc 中的 defgabc 而不是 abcdefg. 通过比较很容易看出后发断言
# 和先行断言正好相反: 它先从要匹配的字符串的最左端开始查找断言表达式, 之后再匹配后面的字符串, 如果无法
# 匹配则继续查找第二个断言表达式, 如此反复.
# 再说一下负向零宽断言的两种形式:
# 1) (?!exp) 叫零宽度负预测先行断言, 断言此位置的后面不能匹配表达式 exp. 比如 \b((?!abc)\w)+\b 匹配
# 不包含连续字符串 abc 的单词, 查找 "abc123,ade123" 这个字符串, 可以匹配出 ade123, 可以使用 Match Tracer
# 进行查看分析.
# 2)