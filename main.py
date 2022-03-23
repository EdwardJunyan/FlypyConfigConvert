# 将小鹤音形官网提供的挂接辅助码ini文件转换成支持Windows版百度输入法支持的配置文件
import re

file1 = open('./for安卓百度个性短语.ini', 'rt', encoding='UTF-16LE')
file2 = open('./for安卓百度个性短语-PC.txt', 'w', encoding='UTF-8')

# 原格式: [字码]=[候选位置],[候选词] 例: bag=1,靶
# 新格式: [候选位置],[字码]=[候选词] 例: 1,bag=靶

pattern = re.compile(r'[0-9]+,')  # 匹配原格式的 "数字,"
line = file1.readline()[1:]  # 避免读取源文件的BOM

while line:
    num = re.findall(pattern, line)  # 提取原格式的 "数字,"
    num = num[0]
    newLine = line.replace(num, "")  # 将原格式中的 "数字," 删除
    newLine = num + newLine  # 将提取的 "数字," 添加至开头
    file2.write(newLine)  # 写入
    line = file1.readline()  # 读取下一行

file1.close()
file2.close()
