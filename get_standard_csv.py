# 读取csv文件, 进行数据处理, 要求删除所有空格，得到有标题的csv文件
# 得到的文件便于检查数据是否正确, 也便于后续分析
# 另外因为是导出微信账单，可能出现日期与上次导入Notion有重复的情况，
    # 这里可以在 alipay_raw.csv 中直接删除某一些日期。当然你也可以用程序进行筛选

import re

def get_standard_csv(path_raw, path_new):
    '''读取原始文件，截取并得到新的文件'''

    with open(path_raw, encoding="gbk", newline="") as f: # 注意encoding="gbk"
        lines = f.readlines()   # 读取所有行
        for line in lines:  # 遍历每一行
            if line.startswith("------------------------支付宝"):   # 找到以"------------------------支付宝"开头的行
                with open(path_new, "w", encoding="utf-8", newline="") as f2: # encoding="utf-8"为便于读写
                    # 将该行之后的所有行写入新文件并且用re删除每一行中的空格
                    f2.writelines(re.sub(r"\s+,", ",", line) for line in lines[lines.index(line) + 1:])


# def main():
#     raw_path = "alipay_raw_test.csv"
#     new_path = "alipay_standard_test.csv"
#     get_new_data(raw_path, new_path)

# if __name__ == "__main__":
#     main()





