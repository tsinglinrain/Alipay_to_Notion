# Alipay_to_Notion
Transfer Alipay bills to Notion, does not use Alipay official API<br>
将支付宝账单转入Notion，注意没有使用支付宝官方API<br>

[English](https://github.com/tsinglinrain/Alipay_to_Notion/blob/main/README.md) | [中文](https://github.com/tsinglinrain/Alipay_to_Notion/blob/main/README_zh.md)

这是个人对于Notion API另一个尝试，目前仍然作为**练手项目**，代码可能仍存在不少问题。<br>同时，关于**微信账单**导入，我也写了另外一个项目[tsinglinrain/WechatPay_to_Notion](https://github.com/tsinglinrain/WechatPay_to_Notion)，两者之间代码几乎一样。但是分开有利于账单处理。<br>我自己就在使用，导入到Notion后利用相关模板管理支出。

# 其他说明

支付宝官方API没看懂说明<br>[查询对账单下载地址 - 支付宝文档中心 (alipay.com)](https://opendocs.alipay.com/apis/api_15/alipay.data.dataservice.bill.downloadurl.query)

这里选择先将账单导出，随后利用python语言，并借助Notion提供的API接口对其进行请求，最终将内容发送至Notion数据库。

灵感来源于少数派的[这篇文章](https://sspai.com/post/66658)，但是他没有给出完整的代码。

# 使用说明

## 1.Notion API申请

### 1.1访问[My integrations | Notion Developers](https://www.notion.so/my-integrations)

![image-20230324213427619](./image/image-20230324213427619.png)

### 1.2点击`New integration`

简单填写`Name`，并且选择`Associated workspace`后下翻找到`Submit`并点击提交。

![image-20230324214416578](./image/image-20230324214416578.png)

点击`show`后，点击`copy`，复制好后作为备用。如果是win系统，使用时敲击键盘`win`+`v`，即可查看剪贴板内容。

![image-20230324214659248](./image/image-20230324214659248.png)

## 2.Notion数据库

### 2.1 创建数据库

你可以复制此[模板](https://tsinglin.notion.site/tsinglin/68951a1caaba487a884cafcd5086810c?v=3d0c405e7cae405599aed2fe0f5233cc)进行参考。<br>请注意，如果你对于官方的请求模式并不熟悉，请不要编辑本模板；如果你需要自己设置，需要参考[Introduction (notion.com)](https://developers.notion.com/reference/intro)，并对python代码进行相关修改。

### 2.2 引入integration

如下图所示，点击`...`，`Add connections`，找到前面自己设置的`integration`，这里是点击`记账`。

![image-20230325202326631](./image/image-20230325202326631.png)

点击`confirm`后，应当如图所示。

<img src="./image/image-20230325202635760.png">

### 2.3复制`database id`

在浏览器中找到自己的数据库，观察上面的网址，网址应当如下所示，<br>https://www.notion.so/tsinglin/68151a1caaca488a884cafcd5086810c?v=3d0c405e7cae406599eed2fe3f9233dc<br>
复制`tsinglin/`与`?`之间的内容，这就是`database id`。

## 3.WeChat Pay账单的导出

打开支付宝，点击底下`我`，点击`账单`，点击右上方`...`，点击`开具交易流水证明`，点击`用于个人对账`，点击`申请`，自己选择时间，输入支付密码和邮箱。请注意邮箱一定不能填错，否则容易造成隐私泄露。

收到邮件后下载压缩包，解压密码为身份证后六位。

总之，最终得到一份格式为csv的文件。

## 4.python代码设置

### 3.1下载本项目中所有文件

可以`git`下载，也可以直接下载本文件的压缩包，然后解压。

### 3.2`database id` 和 `token`填入

请将`config.yaml`复制并改成`config_private.yaml`，然后填入如下内容：

```yaml
# 请将此config.yaml复制并重命名为config_private.yaml
database_id: "aaa121************"    # 数据库ID, 要填进去哦
token: "secret_Wa***********" # token, 记得自己填写
```

### 3.3重命名

将支付宝账单的csv文件复制进入此文件夹下，并且将此csv文件重命名为`wechat_raw.csv`。

解释原因：

1. 代码中文件位置为相对路径，必须将支付宝账单文件与上述文件为同一文件夹下
2. 代码中规定文件名称为`wechat_raw.csv`，必须重命名支付宝账单文件

### 3.4运行程序

运行`main.py`即可。

### 3.5观察运行结果

一般是出现`成功`。

出现`失败`，需要单独检查，暂时还没有返回是哪一行出现失败，以后再修改(没想好怎么改)。