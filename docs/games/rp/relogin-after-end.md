---
statistics: true
comments: true
comment: true
---
# 在停运多年后的今天重新登录粉刷匠大作战！
!!! abstract
    [原始文章](https://www.bilibili.com/read/cv40211356?opus_fallback=1)发布于 2024年12月26日

## 1.总体

注：本文讨论的仅仅是登录渠道端账号而不是登录游戏服务器。本教程不是时光机器教程，不能帮你带回2018年。但可以帮助您在服务器不再可用的今天在一些平台显示您在近期“游玩过”粉刷匠大作战。

您需要的：

- 《粉刷匠大作战》v1.1.24
- Android 设备
- 《粉刷匠大作战》v1.3.x 任意您需要登录的渠道版本（可选
- 任意一款文本编辑器
- 任意一款支持签名的 Android 应用打包工具

从《粉刷匠大作战》版本1.1.24开始，账号系统正式回归。该版本重新开始要求用户登录账号进入游戏并使用G家账号系统取代了先前版本半残废的悦岩居账号系统。

## 2.那为什么选择版本v1.1.24呢？

版本1.1.24的账号登录流程与此后版本的粉刷匠大作战有所不同，此后版本中必须保证加载的serverlist中的服务器能够成功联通才可进行账号登录流程，而直到现在，粉刷匠的服务端获取的可能性微乎其微（近期与策划的联系中确认对服务端提供无能为力），使得此后版本无法直接登录。<br><br>事实上v1.1.6.6也支持账号登录，在经过一定修改后也能够登录《古域2》账号，而一测版本无法与二测以后的版本的Java端代码相处融洽。<br><br>以上种种原因使得版本1.1.24成为最适合我们这一教程的版本。

![img-01](/assets/docres/games/rp/relogin-after-end/img-01.webp)

## 3.配置serverlist

尽管我们使用的版本v1.1.24可以无视游戏服务器是否存在而直接登录账号，但我们仍然需要为其配置serverlist。

![img-02](/assets/docres/games/rp/relogin-after-end/img-02.webp)

以下为serverlist的内容示例，您可以直接复制该内容以创建serverlist文件。

``` title="fsj_serverlist.txt"
ID	IP	Port	Open	Desc 
9	s2.net.fsj.sdo.com	15062	0	#n服务器正在维护中，给大家带来的不便，敬请谅解～同时欢迎大家加入#R《粉刷匠大作战》官方Q群：683626467#n了解第一手游戏资讯，更有福利不断放送中~
```

接下来，您需要对《粉刷匠大作战》游戏包体 APK 进行修改。因此您需要文本编辑器和 Android 应用包打包工具。以下我们使用 MT 管理器 作为示例工具。

打开游戏包体，前往 /assets/etc 目录，打开 client_config.xml 在下加入以下语句

```xml title="client_config.xml" hl_lines="35"
<Config>
  	<!--全部更新后登陆-->
	<UpdateAllData>1</UpdateAllData>

  	<!--打开log-->
	<OpenLogFile>1</OpenLogFile>

	<!-- 程序脚本目录 -->
	<SearchPathProgrammer>
		<Path>ShellClientLua/?.lua</Path>
		<Path>ShellCommonLua/?.lua</Path>
	</SearchPathProgrammer>

	<!-- 策划脚本目录 -->
	<SearchPathDesigner>
		<Path>script/common/?.lua</Path>
		<Path>script/server/?.lua</Path>
	</SearchPathDesigner>

	<!-- 自动断开连接时间（秒） -->
	<DisconnectTime>120</DisconnectTime>
	
	<!--限制帧率-->
	<FrameRateLimited>1</FrameRateLimited>

	<!-- 是否显示控制台 -->
	<ShowConsole>1</ShowConsole>

  <!--初始窗口大小-->
  <MainWndSize Width="1280" Height="720"/>

  <!--UI标准大小-->
  <StandarUISize Width="1280" Height="720"/>

  <ServerList File="您配置的serverlist URL" />

</Config>
```

将值填写为您所要的 serverlist URL 即可

例如，我们直接在该文件的下添加以下语句并保存。

```
<ServerList File="etc/fsj_serverlist.txt" />
```

在etc目录下，创建fsj_serverlist.txt，内容填写为上述 serverlist 示例的内容并保存至 apk 中。

做好安装包签名操作后（MT管理器应该会在您保存文件至 APK 时自动要求签名操作），安装您的 APK并启动游戏。现在您应该可以使用内置的G家账号系统登录您的G家账号了。

![img-03](/assets/docres/games/rp/relogin-after-end/img-03.webp)

## 4.我想使用其他渠道账号登录

您需要准备您想要登录的渠道版本的《粉刷匠大作战》安装包体 APK。

我们仍然需要版本1.1.24的安装包体。

通过以下步骤您可以将您刚才更改的版本 1.1.24 主体轻松迁移至您准备的渠道版本《粉刷匠大作战》。

1.使用版本 1.1.24 的 /assets 目录覆盖渠道服包体的 /assets 目录。

2.使用版本 1.1.24 的 /lib 目录覆盖渠道服包体的 /lib 目录。

签名完成并安装后，您可以使用您需要的渠道账号登录游戏了。

![img-04](/assets/docres/games/rp/relogin-after-end/img-04.webp)

![效果如图](/assets/docres/games/rp/relogin-after-end/img-05.webp)


NoobArchive
