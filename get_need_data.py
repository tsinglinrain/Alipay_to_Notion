# 进一步分析数据
# 这里自定义程度比较高,可以根据自己的需求进行修改
    # 比如我只想要支出，那么我就通过布尔取值，只要支出的数据

# 进一步整理数据
# 这里面的日期必须修改
# 这里面的价格必须修改
# 其他可自行修改

# 这是我示例的一个数据处理过程

import pandas as pd
import numpy as np

def get_need_data(path):
    '''删改数据'''
    df = pd.read_csv(path, encoding="utf-8")

    # 必须处理的列
    df["交易时间"] = df["交易时间"].map(lambda x: "".join([x[:10], "T", x[11:], "Z"]))  # ISO 8601
    df["金额"] = df["金额"].map(lambda x: float(x))

    # 删除不需要的列 optional
    # df.drop(["对方账号", "收/付款方式", "交易状态", "交易订单号", "商家订单号"], axis=1, inplace=True)
    df.drop(["对方账号", "交易状态"], axis=1, inplace=True)
    
    # 删除"收/支"列中为"收入"所在的行
    df = df[df["收/支"] != "收入"]
    # df.drop(df[df["收/支"] == "收入"].index, inplace=True)
    
    # 再次删除"收/支"列
    df.drop(["收/支"], axis=1, inplace=True)

    # # 对"备注"再次定义, 将所有的nan值替换为"",如果不替换，会出现requests.exceptions.InvalidJSONError: Out of range float values are not JSON compliant
    df["备注"] = df["备注"].map(lambda x: "" if pd.isnull(x) else x)

    return df

# def main():
#     path_raw = "alipay_standard.csv"
#     df = get_need_data(path_raw)
#     print(df.head(5))  # 查看前5行
#     for i in range(len(df)):
#         # print(df["交易时间"][i], df["金额"][i], df["交易分类"][i], df["交易对方"][i], df["商品说明"][i], df["备注"][i])
#         print(df.iloc[i]["交易时间"], df.iloc[i]["金额"], df.iloc[i]["交易分类"], df.iloc[i]["交易对方"], df.iloc[i]["商品说明"], df.iloc[i]["备注"])
#         # break

# if __name__ == "__main__":
#     main()