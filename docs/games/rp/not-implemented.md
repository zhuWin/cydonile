---
statistics: true
comments: true
comment: true
---
# 粉刷匠大作战尚未实现或尚未启用的功能
!!! abstract
    [原始文章](https://www.bilibili.com/read/cv36499988/?opus_fallback=1)发布于 2024年07月30日

![img-01](/assets/docres/games/rp/not-implemented/img-01.webp)

注：粉刷匠大作战各版本可能包含前作《贪吃蛇乐园》的遗留内容，研究时请留意。

例如直至最终版本1.3.3.4.x“dictionary”翻译文件的90000003-90000051,97000000- 9700005d

![img-02](/assets/docres/games/rp/not-implemented/img-02.webp)

## 战绩分享功能回归 “去显摆一下”

明显尚未完成，已存在于游戏代码，尚未正式实装。目前版本常规情况该功能处于隐藏状态，位于游戏结算最高得分变动页，仅于2018.5.20崩服事件意外实装，按键暂时没有功能（？）

可通过卡顿的网络显示该按钮。

已得到官方确认

在常规定义文件CommonConstDefine.lua 中存在疑似该功能的定义。

```
eHornorShareType_Nothing                = EnumLua( 0, "/*什么都没获得*/"  )    

eHornorShareType_EndlessWhole           = EnumLua( 1, "/*圈地之神（无尽圈地100%）*/"  )    

eHornorShareType_LimitWhole             = EnumLua( 2, "/*唯我独尊（限时圈地100%）*/"  )    

eHornorShareType_UndeadBetter           = EnumLua( 3, "/*不死金身（无尽不死排名前三）*/"  )    

eHornorShareType_TeamBest               = EnumLua( 4, "/*老司机（团战贡献>TeamRadio）*/"  )    

eHornorShareType_BeyondWorld            = EnumLua( 5, "/*吉尼斯纪录（超越世界最好成绩）*/"  )    
```

![img-03](/assets/docres/games/rp/not-implemented/img-03.webp)

## 自嗨模式战绩排行榜拆分，单独的自嗨面积榜

在CommonConstDefine.lua 中有所提及，将自嗨（无尽）模式的面积榜和记录榜分别列出。

```
eRankType_EndlessRecordDay              = EnumLua( 2,   "/*无尽日榜*/" )

eRankType_EndlessRecordWeek             = EnumLua( 3,   "/*无尽周榜*/" )  

eRankType_EndlessRecordHistory          = EnumLua( 4,   "/*无尽历史榜*/" )  

eRankType_LimitRecordDay                = EnumLua( 5,   "/*限时周榜*/" )  

eRankType_LimitRecordWeek               = EnumLua( 6,   "/*限时周榜*/" )  

eRankType_LimitRecordHistory            = EnumLua( 7,   "/*限时历史榜*/" )  

eRankType_TeamRecordDay                 = EnumLua( 8,   "/*团战日榜*/" )  

eRankType_TeamRecordWeek                = EnumLua( 9,   "/*团战周榜*/" )  

eRankType_TeamRecordHistory             = EnumLua( 10,  "/*团战历史榜*/" )  

eRankType_EndlessAreaDay                = EnumLua( 11,  "/*无尽面积日榜*/" )  

eRankType_EndlessAreaWeek               = EnumLua( 12,  "/*无尽面积周榜*/" )  

eRankType_EndlessAreaHistory            = EnumLua( 13,  "/*无尽面积月榜*/" )  
```

## 家族系统

（1.3.2.4尚未加入家族系统）

根据v1.3.3存留的资源，很显然自2018.03.14以来，家族系统已经开发至接近完善并在存有诸多明显Bug的情况下能够运行，在各处文件中都能找到家族系统的引用。

主界面逻辑代码已经实现了进入家族系统的按钮，但是在GUI配置中却没有加入该按钮，因此没有显示。

通过对主界面代码的魔改，在1.3.3.4.7版本已经可以进入家族界面。

家族可设置图腾（图标），名称，宣言和批准的开关。成员分为普通族员，副族长和族长。

实现了家族成长系统和成员活跃度，家族等级实际收益未知，每星期内家族活跃度达到100后人数未满的家族方可进入推荐名单

同时包含全服家族排行榜

家族名称最多7个汉字（21字节，使用UTF-8）默认：我的家族最强大 GUI占位：家族名称在这里

家族宣言最多25个汉字（75字节，使用UTF-8）默认：我们的目标是粉刷全世界 GUI占位：999

家族最多可以升级到10级，家族升级根据家族成员历史活跃度的总和（？），每一等级100活跃度

![img-04](/assets/docres/games/rp/not-implemented/img-04.webp)

![img-05](/assets/docres/games/rp/not-implemented/img-05.webp)

![img-06](/assets/docres/games/rp/not-implemented/img-06.webp)

![img-07](/assets/docres/games/rp/not-implemented/img-07.webp)

```
eClan_Member                            = EnumLua( 0,       "/*普通族员*/" )
eClan_Vice_Leader                       = EnumLua( 1,       "/*副族长*/" )
eClan_Leader                            = EnumLua( 2,       "/*族长*/" )

CLANNAME_BYTE_SIZE                      = EnumLua( 7*3,     "/*家族名字最大字节数*/" )
CLANSLOGAN_BYTE_SIZE                    = EnumLua( 25*3,    "/*家族口号最大字节数*/" )

eJoinClan_Ok                            = EnumLua( 0,       "/*成功加入家族*/" )
eJoinClan_Failed_InClan                 = EnumLua( 1,       "/*已有家族，加入失败*/" )
eJoinClan_Failed_NoClan                 = EnumLua( 2,       "/*家族不存在，加入失败*/" )
eJoinClan_Failed_MemberMax              = EnumLua( 3,       "/*人数已满，加入失败*/" )
eJoinClan_Approve_Wait                  = EnumLua( 4,       "/*申请成功，静待审批*/" )
eJoinClan_Approve_Exist                 = EnumLua( 5,       "/*已申请过但还未审批，申请失败*/" )
eOperate_Ok                             = EnumLua( 6,       "/*操作成功*/" )
eOperate_Failed_NoPower                 = EnumLua( 7,       "/*没有权限，操作失败*/" )
eOperate_Failed_NoInfo                  = EnumLua( 8,       "/*查无此条，操作失败*/" )
eExitClan_Ok                            = EnumLua( 9,       "/*退出家族成功*/" )
eExitClan_Failed_NoInClan               = EnumLua( 10,      "/*当前无家族，退出失败*/" )
eExitClan_Failed_NoClan                 = EnumLua( 11,      "/*家族不存在，退出失败*/" )
eAccurateSearchClan_Ok                  = EnumLua( 12,      "/*精确查找家族成功*/")
eAccurateSearchClan_Failed              = EnumLua( 13,      "/*精确查找家族失败*/" )
eCreateClan_Ok                          = EnumLua( 14,      "/*创建家族成功*/" )
eCreateClan_Failed_LackResource         = EnumLua( 15,      "/*缺少资源，创建失败*/" )
eCreateClan_Failed_NoSocial             = EnumLua( 16,      "/*未连接Social服务器，创建失败*/" )
eCreateClan_Failed_NameExist            = EnumLua( 17,      "/*名字已存在，创建失败*/" )
eCreateClan_Failed_InClan               = EnumLua( 18,      "/*当前已有家族，无法创建*/")
eAgree_ClanApply                        = EnumLua( 19,      "/*同意申请*/" )
eRefuse_ClanApply                       = EnumLua( 20,      "/*拒绝申请*/" )

eClanActivity_Day                       = EnumLua( 0,       "/*日家族活跃度*/" )  
eClanActivity_Week                      = EnumLua( 1,       "/*周家族活跃度*/" ) 
eClanActivity_Month                     = EnumLua( 2,       "/*月家族活跃度*/" )  
eClanActivity_Count                     = EnumLua( 3,       "/**/" )
```

## 首充礼包

在约1.3.2.4之后的版本加入了服务端可配置开启的的首充礼包相关功能，规则是首次充值（会员钻石均可）赠送财神驾到皮肤及5000金币，100音符，200乐能量和100赠送钻石。

然而正式服务器却从未启用该功能的入口，同期在体验服可见该功能的入口于会员图标旁边，但体验服禁用了充值功能，便仍然无法进入首充礼包界面。

![img-08](/assets/docres/games/rp/not-implemented/img-08.webp)

## 更多的会员付费选项

```
0b170000    18元/月会员
0b170001    180元/年会员
0b170002    6元首充月会员
```

![img-09](/assets/docres/games/rp/not-implemented/img-09.webp)

实际可用的选项

## 更多日常赛事类型

```
9.txt
90000aad    可以瓜分奖金/分数不够，下次加油！
90000aae    30分
90000aaf    下轮奖金
90000ab0    100,000
90000ab1    比赛结束倒计时
90000ab2    99:99:99
90000ab3    当前总得分
90000ab4    剩余参赛次数
90000ab5    27分
90000ab6    30分
90000ab7    1次
90000ab8    本轮奖金
90000ab9    100,000
90000aba    距离下次比赛还有
90000abb    99:99:99
90000abc    本轮奖金
90000abd    100,000

Scene_list.xml
<!--
    nRoomType 房间类型 0单机 1服务器单人 2服务器团队  3指引 7私人限时 8私人团战 9限时赛事 10团战赛事  13限时现金赛
  -->
```

限时现金赛，用途未知

此外还包含混合赛事，可能同时包含限时和团战

```
eWorldRaceType_Limit                    = EnumLua( 1,   "/*限时赛事*/" )
eWorldRaceType_Team                     = EnumLua( 2,   "/*团战赛事*/" )
eWorldRaceType_Both                     = EnumLua( 3,   "/*混合赛事*/" )
```

## 同时启用更多的被动技能

可能只是用来测试。

```
Max_Passive_Skill_Num                  = EnumLua( 5,   "/**/" )
```

## 与现实地图场景的互动

尚未完成，后续版本已包含百度地图SDK，地图功能已得到官方人员确认，

![img-10](/assets/docres/games/rp/not-implemented/img-10.webp)

## 特惠活动

![img-11](/assets/docres/games/rp/not-implemented/img-11.webp)

名称来源自配置文件，似乎尚未完成，在5.20崩服事件中相关功能疑似得到启用，通过金币参与，获取乐能量等资源。

## 段位掉段保护

```
90000462	保护分
90000463	50/100
9000043c	掉段保护已开启
9000043d	保护积分
9000043e	积满100分=1颗星
9000043f	50/100
90000440	+12
```

于翻译文件中发现相应字符串，该功能从未实装于正式游戏中，是否完全实现仍然未知

游戏可执行文件中CLadderProtectConfig一系列函数与此有关

配置文件存于starprotect.txt，但其引用的字典ID对应的字符串大多并不存在。

早在v1.1.24便已被发现

## 截图分享功能

该功能至少在一测时就已经被提及。从未实装于正式游戏中，是否存在于代码依然未知。可能后续已经更改了分享功能的实现方式？

![img-12](/assets/docres/games/rp/not-implemented/img-12.webp)

## 账号系统与QQ微信、手机号等的绑定

尽管一测时期确实试图加入该功能，二测在v1.1.24之前也包含CLoginWnd的一系列Lua代码提及了qq微信登录（zw试图调用该函数显示登录窗口但是失败，粉刷匠立刻崩溃，signal 11）,翻译文件中账号与qq微信等第三方账号的绑定的引用可能只是前作《贪吃蛇乐园》的残留。手机号登录功能可能为粉刷匠一测原悦岩居（古域2）账号系统的功能。不过由于切换到了尚未实现的妙趣服务器上，粉刷匠在引入盛大游戏新G家账号系统之前的旧悦岩居账号系统自始至终处于不可用状态（2017.9测试）。而直到2024年7月，前作《贪吃蛇乐园》的悦岩居账号系统仍然可用。前作的账号系统可使用《古域2》账号(user.joyegame.com)登录。

![img-13](/assets/docres/games/rp/not-implemented/img-13.webp)

用户登录时间

“一个月前在线”

在翻译文件中有所提及。

## 曲目节奏评价排行

```
0aa00021	加油多拿3S吧，记得之后是有音乐的S评价获取排行的哟~
```

仅在二测以后小提示中有所提及。

## 新技能

在技能配置skill.txt中设置为不在技能列表中显示。

![img-14](/assets/docres/games/rp/not-implemented/img-14.webp)

![img-15](/assets/docres/games/rp/not-implemented/img-15.webp)

![img-16](/assets/docres/games/rp/not-implemented/img-16.webp)

死亡禁锢、影分身等未被正式启用的主动技能MagicID位于隐身之前。

而旋律抖腿的图标用于技能系统开放提示页和键位设置页。

未被启用的部分被动技能参数数值调整的过于强大，效果大于已启用同类型被动技能的数倍

## 皮肤技能/绑定技能

![img-17](/assets/docres/games/rp/not-implemented/img-17.webp)

在翻译文件，技能配置等均有所提及，在skill.txt中配置为在技能列表中显示，但实际上没有列出。

与普通被动技能的三位数ID不同，绑定被动技能使用四位数ID。

大体而言，绑定被动技能效果对应4级对应普通被动。

节奏积分加成类技能例如各种达人， 参数均为80000 ，为对应普通LV6被动效果的数倍

尚未实际测试绑定被动技能的实际效果，以上表现根据skilllevel.txt配置参数编写

尚未确定与皮肤关联的技能是否就是绑定技能。

## 全新音乐

## 苏格兰风情

自1.1.19至1.3.3.4.13该曲目始终只雪藏于配置文件，设置未不显示

## 单独的节奏鼓点练习曲目

自二测起，粉刷匠包含一个尚未被利用的曲目“鼓点练习曲”（在配置文件中被意外指定为“旋律练习曲”的翻译条目，后者本身也被意外指定为“鼓点练习曲”），音乐ID为11。该曲目仅包含中速鼓点节拍，而旋律练习曲最初仅包含“我是一个粉刷匠”标志旋律。后期版本两首曲目被合并为单首“旋律练习曲”，而鼓点练习曲被改为聋的传人音频内容被移除。

可能计划在单独的节奏练习教程关卡中使用，但后来正式加入的节奏练习关卡却仍然使用旋律练习曲。

## 原生 Windows PC端

在引擎代码中包含IsPC条件的判断

CAppUpdateMgr::GetModuleName(void)给出结果为ShellClient.exe而非libShellClient.so

1.1.19版本中CGameStartLua:OnClickShare()会判断平台是否为Android或Win32

V1.2.6时二测服甚至直接在version,inf里写明了Windows版本的链接

![img-18](/assets/docres/games/rp/not-implemented/img-18.webp)

@K·星途

有趣的是，该链接目录结构神似《粉刷匠大作战》开发者提及的可能的某“氪金网游“《古域2》

![img-19](/assets/docres/games/rp/not-implemented/img-19.webp)

前作《贪吃蛇乐园》《爆彩童话》均包含完整version.inf，其中亦提供windows版可执行文件的更新链接。

## 操作记录功能回放

CGameScene::WriteRecord( char foo )函数可保存操作记录到foo或缺省的F:/a.record

GM命令/replay

![img-20](/assets/docres/games/rp/not-implemented/img-20.webp)

## 一测教程模式

一测时期粉刷匠的教程仅包含流程图片幻灯片，但是在代码中已着手实施了单独的教程模式，如同二测后的新手教学，但有多处不同。

明显更加丰富的文字流程，玩家名称为：“你的粉刷匠”

```
10000000   欢迎来到粉刷匠世界，在这能操控节奏线，形成领域。
10000001    就先由我来示范一次吧，看如何生成节奏线。
10000002    看到了么？跟着节奏行动，能画出节奏线，来试试看。
10000003    准备开始吧，跟着音乐，有节奏的点击右键哦。
10000004    没跟上节奏呢，要有节奏的点击右键啊，再试一次吧。
10000005    很好，节奏掌握得不错，节奏线画得就比较好。
10000006    再试试向下画节奏线吧，这次和我一起来进行吧。
10000007    这次又没踩好节奏呢，让我们一起再来一次吧。
10000008    很好，节奏感是不是掌握得熟练一些了？
10000009    让我们继续行动，用节奏线围出一块节奏领域。
10000010    这次是向左画出节奏线，还是跟我一起行动吧。
10000011    点击的节奏出错了，没跟上音乐，再来一次吧。
10000012    干的不错，节奏操作掌握得越来越熟练了。
10000013    最后向上画出节奏线，就可以形成领地了。
10000014    点击的节奏又出了问题，听着音乐，再来一次吧。
10000015    非常棒，一条封闭的节奏线，就能圈出一块领域了。
10000016    节奏线的了解先到这，下面来学习如何攻击其他玩家；
10000017    要击败一个玩家，切断他的节奏线就行，我们来试试。
10000018    对我的节奏线前进吧，按节奏来行动，否则速度会慢。
10000019    不行呢，没按节奏行动，速度慢了，我回到领地了。
10000020    听着音乐节拍，按节奏操作，再来试一次吧。
10000021    看，线被切断后，我就被打败了。换我来进攻你吧。
10000022    当敌人过来时，要尽快返回自己领域，才能确保安全；
10000023    你已经画出了节奏线，我来进攻了哟，快返回领地吧。
10000024    返回也要按节奏行动，否则速度变慢了，逃跑更困难。
10000025    节奏线已经被我切断了，没按节奏行动，速度慢了哦。
10000026    听着音乐节拍，按节奏操作，再来试一次吧。
10000027    很棒！节奏把握准，成功返回了，获得了新领地范围。
10000028    好了，已经学习得差不多了，进入实战体验一下吧。
```

可惜由于一测粉刷匠的代码包装方式，zw可能无法使其重见天日。

## 模式描述

```
90000279    开黑升段更快
9000027a    无限制随便嗨
90000256    抢排位升段位
90000257    好基友一屋子
```

仅存在于翻译文件中

## 全局任务系统

在二测1.1.7.1引入任务系统的占位符，但后续版本惨遭移除。

（勿与自嗨模式本局目标混淆）

```
90000254    新手任务
90000278    任务完成
```

## 直接复制分享链接&amp;微博分享

![img-21](/assets/docres/games/rp/not-implemented/img-21.webp)

在尚未正式引入分享功能的粉刷匠v1.1.16.1中，可以直接复制分享链接，并加入了尚不可用的微博分享，后续版本该两个功能均被移除。

## 更多皮肤

以下皮肤在粉刷匠首次于Taptap上线时便于预览图中展示，但始终尚未实装，机器人和死神皮肤可能与后期加入的皮肤冲突。

![img-22](/assets/docres/games/rp/not-implemented/img-22.webp)

```
0b040006    机器人
0b040007    雪人
0b040012    死神
```

## 社交功能“摇一摇”“扫一扫”“附近的人”

自二测开始1.1.7.1便已加入占位符，但直到最后版本亦未实现。

## 麦克风相关功能

在登录界面的贴图Bug可发现麦克风图标，尚未知悉其功能。粉刷匠至始至终没有加入麦克风相关功能。

![img-23](/assets/docres/games/rp/not-implemented/img-23.webp)

---

NoobArchive 萌新粉匠档案馆

是杼榅酱喵◊N (N.猪瘟大大zhuWin)
