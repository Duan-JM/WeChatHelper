WeChatHelper
============
简介
----
WeCharHelper是基于Tkkk-iOSer的WeChatPlugin-MacOS微信插件的LaunchBar第三方插件支持。
主要功能有以下两个：
1. **在不打开微信的情况下**，通过搜索快速定位到要聊天的对象，并**打开相应的聊天窗口**
2. 通过搜索快速定位到聊天对象，并发送信息。**全程不打开微信窗口**。

*补充说明：支持使用拼音进行汉字的模糊搜索。*

依赖库
------
1. python >= 3.6
2. requests
3. TKkk-iOSer/WeChatPlugin-MacOS（支持防撤回，微信免扫码认证，微信多开，自动回复）

安装指南
--------
1. HomeBrew安装
  在终端中执行如下指令即可：
  ```bash
  /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
  ```
2. 通过HomeBrew安装python3
  ```bash
  brew install python3
  ```
3. 安装python3的Requests库
  ```bash
  pip3 install requests
  ```
4. 安装WeChatPlugin-MacOS
  WeChatPlugin-MacOS的[Github地址](https://github.com/TKkk-iOSer/WeChatPlugin-MacOS)，这里有详细的下载说明。

5. 下载目录中的WeChatHelper.lbaction，双击即可安装

使用说明
--------
1. 呼出WeChatHelper
通过LaunchBar搜索WeChatHelper叫出WeChatHelper之后键入空格进入输入模式
2. 发送模式 
输入内容格式为“要搜索的微信名/发送的内容”时，下方会出现下拉菜单，选择你要发送的对象发送信息。
3. 打开聊天窗口模式
输入内容格式为“要搜索的微信名”，在下拉菜单中选择要打开窗口的对象即可

*注：由于launchBar的自身原因，在发送内容的时候，以下拉菜单中显示的消息为准，有时会延迟大约2ms左右。*

