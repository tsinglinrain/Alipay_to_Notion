# 进一步分析数据
# 这里自定义程度比较高,可以根据自己的需求进行修改
    # 比如我只想要支出，那么我就添加if语句，只要支出的数据

# 进一步整理数据
# 这里面的日期需要修改
# 这里面的价格需要修改

# 注意, 这里用csv模块, 你也可以使用pandas模块

import csv
def get_need_data(path1, path2):
    '''读取原始文件，截取并得到新的文件'''

    with open(path1, encoding="utf-8", newline="") as f:
            csvreader = csv.reader(f)
            for row in csvreader:
                if row[5] == "支出":
                    row[0] = "".join([row[0][:10], "T", row[0][11:], "Z"])
                    # print(row[4], row[6], row[1], row[0])
                    with open(path2, "a", encoding="utf-8", newline="") as f:
                        csvwriter = csv.writer(f)
                        csvwriter.writerow(row)











