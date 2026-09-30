---
statistics: true
comments: true
comment: true
---
# 粉刷匠大作战部分内容研究

!!! abstract
    [原始文章](https://www.bilibili.com/read/cv36804285?opus_fallback=1)发布于 2024年08月07日

包含原创研究，部分内容尚未得到实际确认，可能包含事实错误，欢迎指正。

## 总体

![img-01](/assets/docres/games/rp/technical-overview/img-01.webp)

GammaKernel 引擎

《粉刷匠大作战》由广州妙趣软件有限公司开发，其由广州第九艺术网络科技有限公司和广州悦岩居软件有限公司的成员创建。

（一测发布之前，粉刷匠直接使用九艺\悦岩居网络域名fsj.joyegame.com）

游戏使用九艺网络/悦岩居一直使用的Gamma游戏引擎，使用C++和Lua编写。

目前仍然运营的基于该引擎的游戏：《古域2》

除了疑似与该引擎相关的“九艺游戏软件开发工具系统”软著登记，该引擎在网络上找不到任何信息。

此外九艺网络在其招聘信息中直接提及“熟悉lua者“优先。

九艺网络曾经于其网站上提及

> **我们的优势：**<br>**1.成熟的技术：自主研发的 3D 引擎。**

关于该3D引擎是否就是GammaKernel仍需进一步挖掘

已知包含Android,iOS,Windows三大平台(win版本尚未公开发布,官方推荐mumu模拟器)

配置文件除INI外可使用UTF-16LE，UTF·-8和GBK，事实上粉刷匠自身使用的文本编码十分混乱

INI文件建议使用UTF-8，使用其他编码有概率报错can not use asc file here!!并立刻_cxa_throw终止 ( Gamma::CIniFile::Init() )

(但保存的INI配置依然还是UTF-16，如media.inf和user.ini)

MP3使用pvmp3dec库，MP3 Version 1，2均可。但包含较长的ID3元数据的MP3文件可能无法解码并报错Support Layer3 mp3 only!!!!!

视频可播放H264裸流(.264)，一般而言常规的使用ffmpeg转换的h264裸流是没有问题的（ffmpeg -i input.mp4 -vcodec h264 output.h264）

2D贴图文件tex,jpg,bmp,png,jxr,tga均可，默认使用tex格式作为贴图储存（.jxr在引擎中称为.ajpg）

Tex格式疑似为专有容器文件格式，目前已知包含WMPHOTO字段的tex格式（即实际上的JPEG-XR格式）可以被解包查看（但使用该格式的tex文件少之又少，目前仅见粉刷匠残存的《全民猎妖》的部分loading_x.tex在用）

其容器的文件头仍需进一步解析，疑似包含分辨率数据

粉刷匠原生支持键盘输入，优先级大于触控

通过键盘控制可以在新手教学等限制触控按键的状态实现控制粉刷匠移动

## 历史沿革

全民猎妖 0.0.45.1 主程序编译时间Sep 8 2015

贪吃蛇乐园 200.0.0.0 Nov  9 2016 Tap发布日期：2017.2.15

爆彩童话 1.1.0.2 Mar 21 2017 Tap发布日期：2017.1.10，最后更新：2017.3.21

节奏粉刷匠3D 视频录制时间：2017-06-06

粉刷匠大作战 一测 1.1.6.6 Jul 27 2017

《粉刷匠大作战》疑似直接基于《贪吃蛇乐园》代码库

翻译文件曾直接使用贪吃蛇乐园现有文件，且直到粉刷匠最终版本，原贪吃蛇乐园的残留也没有全部移除。其中最著名的是：

![img-02](/assets/docres/games/rp/technical-overview/img-02.webp)

来源：粉刷匠大作战 v1.3.3.4.7

此外，在粉刷匠内测直至盛大圣诞首测（v1.2.1）之前，包括贪吃蛇的纹理资源snake数字.tex仍然存于粉刷匠资源文件中

粉刷匠一测时期仍保留贪吃蛇乐园的UI贴图tcs_jm001.tex

![img-03](/assets/docres/games/rp/technical-overview/img-03.webp)

贴图来源：粉刷匠大作战v1.1.6.6

粉刷匠地图地面贴图文件名为tcs_dt.tex，至于tcs是什么不言而喻。

常量配置读取相关函数直接使用“SnakeConstant”一词。

Strings.txt中相关配置依然保持原贪吃蛇乐园的注释。

Android APK结构和Dex代码与《爆彩童话》类似。可执行文件目录结构均为

仅附带libAndroidBoot.so运行库的libShellClient.so，而非贪吃蛇乐园的原libDeltaxAdapter.so和gdbserver运行库

《粉刷匠大作战》资源加载模块GUI资源bc_jieya.gui中的bc疑似就是原《爆彩童话》，且后者同样包含相同文件名的文件。

~~（粉刷匠和爆彩童话都会在设备开机时以完全一致的方式弹窗崩溃）~~

![img-04](/assets/docres/games/rp/technical-overview/img-04.webp)

svn engine version，《雷霆射击》《全民猎妖》等更古早的Gamma游戏项目版本没有在配置文件写出svn engine version

匪夷所思的是，粉刷匠任何一个版本，贪吃蛇乐园以及爆彩童话v1.1.0.2中均包含完全一样的/assets/etc/loading_0.tex，其内容就是爆彩童话本身的旧logo。

其他/assets/etc/loading_x.tex文件来源自《全民猎妖》

![img-05](/assets/docres/games/rp/technical-overview/img-05.webp)

我们依然不了解粉刷匠从爆彩童话里还继承了什么。尽管爆彩童话以涂染为主题，粉刷匠大作战中曲目“无尽涂染”本身与爆彩童话却毫无关系。

可能是爆彩童话的涂染主题给予官方另一个灵感：粉刷，但我们无法直接肯定，~~且悦岩居公司周边碰巧有一家以刷子为标识的装修公司。~~

官网沿革：fsj.joyegame.com(在1.1.6.6中提及，可能仅用作一测前游戏服务器)》fsj.mqgamer.com》666.sdo.com

## 版本更新

最终引擎二进制版本1.3.3.4.7

最终资源版本1.3.3.4.13

不同于悦岩居先前的游戏，如《爆彩童话》《贪吃蛇乐园》，粉刷匠自内测一直到自1.2-1.3期间的某一版本之前并没有开强制要求联网检测更新，OnNewCodeVersionRetrieved始终为true

且包内version.inf指定的资源目录为本地pkgroot:/，而非前作的仅使用网络资源。

即使在后期版本加载模块翻译文件有所提及，已知版本（1.1.6.6，1.1.6.8，1.1.6.10，1.1.7.1，1.1.16.1，1.1.19，1.1.20，1.1.24，1.2.0，1.2.1,1.2.4,1.3.0,1.3.2.4，1.3.3.4.7）均未启用哈希校验。

一般而言，Android平台Gamma引擎游戏只有当OnNewCodeVersionRetrieved和OnPackageInfoRetrieved均为true时才有可启动进入游戏的可能性（粉刷匠一定，其他gamma手游未知）

关于版本启动流程可见《【粉刷匠大作战】简谈游戏版本检查流程及version.inf配置示例》

补充：粉刷匠等游戏也会解析UpdateInfo项的内容，其作用为将指定的Updateinfo文件内容显示在更新提示窗口中

以下是一份示例version.inf

```inf title="version.inf"
[Mirror]
Mirror1 = http://dl.qmly.m.37.com/lieyao/qmly/data/,http://res.qmly.m.37.com/lieyao/qmly/data/
Mirror2 = http://dl.qmly.m.37.com/lieyao/minapks/,http://res.qmly.m.37.com/lieyao/minapks/
Mirror3 = http://dl.qmly.m.37.com/fknyj/qmly/data/,http://res.qmly.m.37.com/fknyj/qmly/data/
Mirror4 = http://dl.qmly.m.37.com/fknyj/minapks/,http://res.qmly.m.37.com/fknyj/minapks/
[Media]
Code = 37wan
[Silent]
Size = 5194304
[Data]
Version = 0.0.45.1
URL = pkgroot:/
[WinCoreCode]
Version = 0.0.45
Size = 1524596
Md5 = 78f55339aea59a9b021aea5c83577f54
URL = http://dl.qmly.m.37.com/lieyao/qmly/data/bin/release/ShellClient_78f55339aea59a9b021aea5c83577f54_0.0.45.exez
[AndroidCode]
Version = 0.0.40.3
Size = 4154295
Md5 = ${AndroidCodeMd5}
URL = http://dl.qmly.m.37.com/lieyao/minapks/qmly_min_0.0.40.3_37wan.apk
[AndroidCoreCode]
Version = 0.0.45
Size = 1792058
Md5 = 786e5cd1018249f6d69288c05ec17fd8
URL = http://dl.qmly.m.37.com/lieyao/qmly/data/bin/release/libShellClient.soz.786e5cd1018249f6d69288c05ec17fd8_0.0.45
[DeltaXCode]
Version = 0.0.45
Size = 113378
Md5 = ca04b958c45832f848e77d480528e011
URL = http://dl.qmly.m.37.com/lieyao/qmly/data/bin/release/DeltaxCpp_ca04b958c45832f848e77d480528e011_0.0.45.swf
[ShellCode]
Version = 0.0.45.1
Size = 1478217
Md5 = 506eba435379e9d5dcc74fdc949e0942
URL = http://dl.qmly.m.37.com/lieyao/qmly/data/bin/release/Main_506eba435379e9d5dcc74fdc949e0942_0.0.45.1.swf
[ServerList]
URL = http://res.fsj.mqgamer.com/fsj_serverlist.txt
[Stat]
ActiveUrl = http://res.baocai.joyegame.com/statistics/realtime/php/saveActiveData.php
[UpdateInfo]
URL = http://mizukoud.icu/fenshuajiang/updateinfo.txt
```

## 游戏地图场景

游戏局内场景称为scene，可为不同类型的游戏模式配置相应scene。

Scene配置：/config/scene_list.xml

已知单局内玩家数量超过50可能导致游戏崩溃

场景大小调整过大也可能导致游戏崩溃

若非联机模式将bServer设置为1则会出现无法圈地等问题

![img-06](/assets/docres/games/rp/technical-overview/img-06.webp)

不是该问题，但大体上是这样子的

地图地面位图为/gui/tex/tcs_dt.tex

可配置多张map，map可配置的作用暂时未知，待研究

如配置局内掉落的物品为金币还是经验宝石

## 玩法

自嗨模式（无尽模式）Endless

自嗨模式玩家生成由CWanfaEndless:OnCreateDirector()函数处理，包含账户ID，领地ID（？）音乐ID，配置技能的数据，段位星数，玩家名称等数据

主动被动技能硬编码为0和{}

玩家皮肤选择决定着玩家生成pPlayer:StartUp( nEquipID )的( nEquipID )数值，nEquipID即皮肤ID

修改szNickName的参数即可更改名字

![img-07](/assets/docres/games/rp/technical-overview/img-07.webp)

## 技能（V3）

（以下技能说明基于2018.1.15更新后的第三代新技能系统,数据基于2018年5月的v1.3.3.4.7）

游戏内的技能配置/config/skill/skilllevel.txt

技能养成界面配置/config/resource/skill.txt

技能理论可设置最高10级

本质上从技能实现来看，主动技能和被动技能都是一样的，只是是否随时开启

技能按实施方式分为三类 主动技能（ID从1开始） 被动技能（从100开始） 绑定被动技能（从1000开始）

技能的实现为传递参数并执行其指定的Magic

每种技能可指定AIRandom，Level等级，Effect视觉效果，冷却时间，以及最多6种Magic，每个Magic可指定时间和4个参数。

可以配置多个同ID不同Level的技能。

例如：战斗怒火配置为执行3种Magic 1,3,4即同时执行速度调整，视野调整和击杀积分加成调整。

冲刺本质上为极短时间内将速度调整为相对及其大的数值。

Magic

0 无

1 速度调整

3 视野调整

4 击杀积分加成调整

5 圈地积分加成调整

6 节奏积分加成调整

7 范围击杀（铁头）

8 拾取物品的范围调整

9 轨迹线立刻变为领地（固化）

10 死亡禁锢（被你击杀的敌人复活时间延长，且复活后短时间内速度降低）

11 创建影分身

12 角色及轨迹线的透明度（？）（隐身）

14 被击败方经验宝石掉落数量调整 1个参数

15 积分加成调整_判定条件：音乐类型 参数一：1：电子 2：摇滚 3：古典    摇滚节奏22 古典领地31  电音击杀 10 电音节奏12

16 积分加成调整_判定条件：局内击杀玩家次数累计 参数一：已击败玩家的次数

17 积分加成调整_判定条件：COMBO数量 参数一：COMBO数量 **需要测试该数值为当前连击数还是局内累计连击数**

18 积分加成调整_判定条件：是否已团灭出局一队伍 冷血领地11

20 技能冷却时间缩减调整

包含判定条件的积分加成调整 Magic

第一个参数为判定条件数值

第二个参数为加成的积分类型。0：击杀积分 1：领地积分 2：节奏积分 3:速度（？）

## 音乐

30000023   小提示：所有音乐的节拍都是固定的，不会有节拍变奏！

即使官方小提示中有这一句话，这仅仅是游戏规则的设计使然，引擎支持同一曲目无限量的变奏。

事实上粉刷匠的音乐机制理论上任意BPM都可以，只要数值不像Hello（BPM）年份那几个曲子那么离谱一般都可以<br> 且单曲可以随时变奏<br> <br> “中速”“快速”“极速”只是统一设计使然，降低操作难度

单曲目节拍速度可随意调整，途中可以节奏变速<br> 曲目本身无法变速

曲目节奏配置需要为每一个节拍写上相应时间节点和相邻之间的时间间隔。

没有现成的“谱面”生成工具

曲目节奏配置时长配置错误可能导致第一次播放结束时节奏卡住，游戏窗口失去焦点时随音乐暂停，节奏亦会卡在上一判定速度。（已知古域2在游戏窗口失去焦点时确实会暂停音乐，而其他动画进程仍在进行）

![img-08](/assets/docres/games/rp/technical-overview/img-08.webp)

如若音乐加载失败可能导致

![img-09](/assets/docres/games/rp/technical-overview/img-09.webp)

## 皮肤

注：爱神丘比特是小天使在粉刷匠引入fusionskin皮肤之前的旧称

ID顺序与商店顺序不同，参见equip.txt

普通皮肤翻译字符串条目顺序与实际皮肤ID顺序不同

节奏粉刷匠拥有未启用的绑定被动技能万磁王（绑），宝石猎人（绑）和杀手狂欢（绑），参见equip_skill.txt

```
Equip
ID  名称
1   节奏粉刷匠
2   食人花
3   黑衣忍者
4   章鱼保罗
5   呆若木鸡
6   小黄人灯泡
7   柴犬
8   哈士奇
9   街球王
10  冲浪小子
11  兔酱
12  节奏小粉酱
13  蜘蛛娃
14  喵星人
15  乱棍老法师
16  玩具哥斯拉
17  原谅全世界
18  音波豆丁
19  国宝熊猫
20  蹦迪僵尸
21  张飞砍咸鱼
22  齐天大圣
23  神兽羊驼
24  缺爱小龙蛋
25  内测玩赏家
27  红烧狮子头
28  外卖大哥
29  青蛙王子
30  呆萌骷髅
31 财神驾到
32  圣诞老人
33  叨鱼
34  抱抱新娘
35  小爆哥
Fusion
ID 名称
1001    小天使
1002    天使长
1003    六翼炽天使
1011    小恶魔
1012    恶魔王子
1013    德古拉伯爵
1021    机甲士兵
1022    机甲勇士
1023    机甲战神
1031    天府侍女
1032    星月女神
1033    天幽宫御使
1041    盛气战士
1042    神武上校
1043    星炎灵战神
1051    森之精灵
1052    密林使者
1053    神隐域女王
```

## 杂项功能

好友GM问题栏类型由gm_type.txt决定(实测却无法修改)，可指定类型名称，类型的类型和相应1个参数

类型0为FAQ类 参数为gm_column.txt中的nID一致

gm_column.txt可指定问题类型ID 问题名称和描述

类型1为问题反馈类 参数1 充值问题 参数2外挂反馈(?) 参数3 其他问题 默认指定1和3

## 常量配置

SnakeConstant常量系统，沿用贪吃蛇乐园原代码使用粉刷匠配置

/config/constant.txt

``` title="/config/constant.txt"
MoveSpeed   80  移动速度
InitWidth   80  初始领地边长
InitRhythmID    0   领地初始化高度采用的结果编号
InitLineRhythmID    3   线的初始高度采用的结果编号
TraceBackCDTime 10000   快速回退功能冷却时间
TraceBackSpeed  600 快速回退的回退速度
HighSpeed   180 加速后的速度
CameraZ 300 摄像机距离角色水平距离
CameraFov   8000    镜头广角
PlayerScale 3600    角色大小
SpeedUpDeplete  10  每秒消耗能量值
FadeInInterval  400 领地颜色淡入时间
FadeOutInterval 1000    领地颜色淡出时间
LineFadeOutPerUnit  12  "每格轨迹线的淡出时间单位,毫秒"
SafeDistance    192 "安全距离必须为64的倍数,不能小于初始面积加64"
MaxCameraY  430 摄像机距离角色垂直距离最大值
MinCameraY  350 摄像机距离角色垂直距离最小值
MaxAreaRatio    50  百分比
MinAreaRatio    10  百分比
InitGold    2000    初始玩家拥有金币数量
MaxItemCount    11  死亡产出金币最大数量
MinItemCount    7   死亡产出金币最小数量
ItemLimitTime   15000   
RhythmDeplete   4   节奏错误消耗
RhythmRecover   2   节奏恢复
MoveRadius  48  人物移动对领地压下的半径
AiIsJump    1   ai是否跳动
JumpRatio   3800    跳动最小比例
UnitInterval    1   领地格子之间的间隔(像素)
RhythmWndTime   0   游戏多长时间才会出现节奏统计界面
CountDownMax    120 主界面游戏倒数计时提示(s)
CountDownMin    30  主界面游戏倒数计时提示(s)
CountDownTipShow    8   主界面游戏倒数计时提示显示时长(s)
TipShow 1200    通用提示显示时长(ms)
VolRatio    4000    体积分数的系数调整(万分比)
CoinRatio   75  积分转金币的系数调整
Rebirth 3000    重生复活时间
StartLimitSchema    10000   玩家生涯积分小于这个分数限时模式不开启
TuanzhanOpenScore   20000   玩家生涯积分小于这个分数团战模式不开启
StopTishiScore  50000   玩家生涯积分超过这个分数以后不弹提示
LineTooLongTip  45  领地线超过这个格子数弹出提示
LineShowTip 4   领地线后这个格子数弹提示
ConFaultTip 5   连续失误多少个节奏开始弹提示
PressAllWay 3000    持续按多少毫秒开始弹提示
PickRange   4   拾取金币的范围（格子=16像素）
DefaultMusicID  121 默认音乐
ModeMaxDayCoin  7000    全模式金币上限
EndlessMaxDayCoin   1000    无尽模式金币上限
InheritPercent  50  继承百分比(0~100整数)
InheritMax  171 "继承上限,星星个数"
AccumulateCouldObtainGold   25000   累积可获取金币上限
GuideFrame  24  帧数
GuideVideoTime  82  视屏时长（秒）
GuideScore  5000    本局游戏积分低于这个分时，显示指引
EndlessTodayScore   1000    无尽模式局内排行起评分
LimitTodayScore 2000    限时模式局内排行起评分
TeamToadyScore  2000    团战模式局内排行起评分
TaskWndFadeTime 1000    无尽模式任务窗口渐隐时长(毫秒)
FirstEndlessArea    1   第一次玩无尽模式，结算时面积小于该值则显示教程提示，该值范围0~100
FirstEndlessMiss    40  第一次玩无尽模式，结算时节奏失误率大于该值则显示教程提示，该值范围0~100
AfterEndlessArea    5   后续玩无尽模式，连续两局结算时面积小于该值则显示教程提示，该值范围0~100
AfterEndlessMiss    25  后续玩无尽模式，连续两局结算时节奏失误率大于该值则显示教程提示，该值范围0~100
FieldReconnectTime  3000    客户端重连field时间
NewNodeTip  4   无尽模式，每生成该大小个数领地则提示
EndlessTipCount 10  无尽模式提示显示次数
DoubleGradeStartTime    60000   场景剩余时间小于该值时，获得积分翻倍（毫秒）
xianshijiesuomianji 3000    解锁限时模式需要的无尽模式累计圈地面积
tuanzhanjiesuofenshu    7000    解锁团战模式需要的限时模式累计获得的积分数
tuanzhantishifenshu 30000   团战历史累计分数达到这个分数后，不再弹出技能提示
SkillCD 10000   技能CD
SkillSpeed  1600    技能速度
SkillTime   100 技能时间
LimitModeOpenMusicID    131 解锁限时模式奖励音乐ID
LimitModeOpenFragmentID 12  解锁限时模式奖励碎片ID
LimitModeOpenFramentCount   10  解锁限时模式奖励碎片个数
TeamModeOpenMusicID 151 解锁团战模式奖励音乐ID
TeamModeOpenFragmentID  12  解锁团战模式奖励碎片ID
TeamModeOpenFragmentCount   10  解锁团战模式奖励碎片个数
ExpManorCount   60  经验地块初始数量(大块非格子数)
ExpManorGainExp 100 每个经验地块增加的经验数
ExpManorSpace   3   经验水晶的间距，单位格子
WhetherShowExp  1   是否显示经验相关东西，大于0表示显示经验相关，等于0表示不显示
PickExpRange    3   拾取经验的范围（格子=16像素）
MaxExpProgressY 235 在主界面的Y坐标
MinExpProgressY 218 在主界面的Y坐标
RhythmGuidePrize    5000    新手节奏指引奖励的金币数
GuideMgrPrize   2000    新手游戏指引奖励的金币数
VideoGuidePrize 2000    新手完成教学视频奖励的金币数
CameraY1    2500    观战中切换视角的镜头高度
RollStayTime    60  抽奖前两圈item显示的间隔时间，单位为毫秒
RollSlowDownNum 5   "光环在目标物品之前减速的相距物品数，[1,12]范围"
RollIncreaseTime    70  光环减速后每经过一个奖励物品则增加的毫秒数
WhetherOpenLadder   1   是否开启赛季结算，0表示关闭，1表示开启
RollEndStayTime 1000    转盘活动最后物品停留的时间，单位毫秒
HandlePosTime   3000    私密房间普通玩家对位置的操作时间限制，单位毫秒
CaptainHandlePosTime    0   私密房间房主对位置的操作时间限制，单位毫秒
PassvieSkillNum 3   被动技能最大激活个数
viptreasureboxID    1   VIP会员的宝箱ID
ShareCoinDailyLimit 25  每天通过分享获得音符的上限
ShareCoinWeeklyLimit    10000   每周通过分享获得音符的上限
DefaultOpenAccountLevel 0   "是否默认开放账号等级系统,1是默认开启，0是默认不开启"
UnlockAccountLevelRainbowHistory    200 历史分享币超过该值后解锁账号等级系统  
ShareCoinPerTime    5   每次分享获得的分享币
Diamondinitialspeed 200 经验宝石吸附效果的初始速度
Diamondacceleration 40  经验宝石吸附效果的加速度
Teambattlerebornsaferange   10  团战重生的安全距离格子数（必须要5的倍数）
MaxQueryCount   10  每日最大的反馈次数
Diamondendheight    40  钻石吸附到角色身上的高度值
MinEndlessRunTime   45  无尽模式最低非作弊圈地时间（单位秒）
EndlessCheatPenaltyTime 86400   无尽模式改数据作弊自动封禁时长（单位秒） 默认一天
TodayReportNum  5   每日可举报次数
RaceNumberingSeconds    5   赛事房间开启的倒数计时
CreateClanCostIndex 0   创建家族消耗资源小类
CreateClanCostCount 3000    创建家族消耗资源数量
ClanMemberCountMax  20  单个家族人数上限
ClanPropelActivity  100 推荐家族活跃度需超过的分数(本周)
ClanPropelMemberCountMax    20  推荐家族人数不得超过该值
DefaultClanIconID   12001   创建家族时的默认家族IconID
ClanActivityDayLimit    1000    每个玩家每天可获取的家族活跃度上限 
BeyondTeamRaceReconnect 18000   超过该秒数后，在赛事12人界面退出团战赛事的玩家不能再进入
TeamRaceJoinLimit   1   团战赛事小队人数限制解除（测试方便用，0表示不限制，其他值表示限制）
```

## 已知BUG

请参阅《粉刷匠大作战Bug合辑》

## 尚未实现的功能

请参阅《粉刷匠大作战尚未实现或尚未启用的功能》

## 其他配置

Client_config.xml中ShowConsole键指的是游戏窗口外的命令行终端，而非游戏内的Debug框。

![img-10](/assets/docres/games/rp/technical-overview/img-10.webp)

## 渠道SDK

V1.1.24之前版本默认使用修改为使用妙趣服务器的悦岩居账号系统

登录服务器URL信息储存于APK根目录下的resources.arsc中

/包名/string/string

将所有的user.mqgamer.com更改为user.joyegame.com即可修复登录系统。

使用古域2账户登录

V1.1.24之后版本默认使用盛趣游戏账号系统

众多渠道服版本在替换原账号系统SDK为其自身的账号系统时保留原账号系统SDK的部分文件（如bilibili渠道），但可能包含例外。

## 渠道服列表

每个渠道可分别设置其是否允许分享功能

1.default 缺省 开启分享 http://share.fsj.sdo.com/public/index.php

2.chjyww 未知 开启分享 http://fsj.mqgamer.com/public/index.php

3.ww9e 九艺网络（仅用测试分享相关功能） 开启分享 http://fsj.mqgamer.com/public/index.php

4.gwtst 测试（未知用途） 开启分享 http://fsj.mqgamer.com/public/index.php

5.gwdemo 演示（未知用途）开启分享 http://fsj.mqgamer.com/public/index.php

6.gw9e 九艺网络（内测官网包、盛大游戏新体验服sndatest(?)）开启分享 http://fsj.mqgamer.com/public/index.php

7.taptap Taptap（内测, 后盛大首测内测官网包） 开启分享 http://fsj.mqgamer.com/public/index.php

8.hykb 好游快爆（内测，后盛大首测内测官网包）开启分享 http://fsj.mqgamer.com/public/index.php

9.fsjgwios 内测iOS版（内测Testflight官网包）开启分享 http://fsj.mqgamer.com/public/index.php

10.snda 盛大游戏（2018.2.7正式服官网包）开启分享 http://share.fsj.sdo.com/public/index.php

11.sndagwios 正式服iOS版（苹果App Store）开启分享 http://share.fsj.sdo.com/public/index.php

12.huawei 华为AppGallery 开启分享 http://share.fsj.sdo.com/public/index.php

13.meizu 魅族 开启分享 http://share.fsj.sdo.com/public/index.php

14.jinli 金立 开启分享 http://share.fsj.sdo.com/public/index.php

15.oppo OPPO 开启分享 http://share.fsj.sdo.com/public/index.php

16.yyb 腾讯应用宝（微信QQ登录）关闭分享

17.qihu360 360手机助手 关闭分享

18.muzhiwan 拇指玩 开启分享 http://share.fsj.sdo.com/public/index.php

19.bilibili B站 开启分享 http://share.fsj.sdo.com/public/index.php

20.kkmh 未知（正式服） 开启分享 http://share.fsj.sdo.com/public/index.php

21.coolpad 酷派 开启分享 http://share.fsj.sdo.com/public/index.php

22.xiaomi 小米应用商店 开启分享 http://share.fsj.sdo.com/public/index.php

23.uc 九游 开启分享 http://share.fsj.sdo.com/public/index.php

24.douyu 斗鱼 开启分享 http://share.fsj.sdo.com/public/index.php

25.m4399 4399游戏 开启分享 http://share.fsj.sdo.com/public/index.php

26.lenovo 联想 开启分享 http://share.fsj.sdo.com/public/index.php

27.vivo vivo 关闭分享

![img-11](/assets/docres/games/rp/technical-overview/img-11.webp)

---

NoobArchive 萌新粉匠档案馆

CC BY 4.0

## 参考资料

天眼查“广州第九艺术网络科技有限公司”

天眼查“广州悦岩居软件有限公司”

天眼查“广州妙趣软件有限公司”

https://bbs.gameres.com/thread_249070_1_1.html

[http://bop.webpatch.sdg-china.com/channel_share.lua](http://res.fsj.mqgamer.com/channel_share.lua) (2018.12.15)
