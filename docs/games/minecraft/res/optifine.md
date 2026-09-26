# OptiFine

> 小问题：思考过为什么人们都叫他是“高清修复”这个问题吗？

昔日白月光，集万千功能于一体，在后扁平化时代逐渐吃力。

在“当代”版本，通常更推荐使用重新实现 OptiFine 功能的替代模组方案。

## “自定义字体”

这个选项存在的意义是 1.4.7 之前的 Minecraft 版本的确不会加载纹理包里的字体纹理。
![pasted-20260802103443](/assets/docres/games/minecraft/res/optifine/pasted-20260802103443.webp)

OptiFine 加入了这个选项使得不必手动改动 minecraft.jar。

1.5 开始 Minecraft 会使用纹理包里的字体了，但字体间距没有调整或调整的较为诡异，OptiFine 自定义字体选项可以用来调整字体渲染。

1.6 使用了新的资源包系统，与此同时也可以使用资源包里的字体文件了。

但这个选项仍然有用。

如果您的资源包在`/assets/minecraft/mcpatcher/font` （1.13 开始改为 `assets/minecraft/optifine/font`）里另外存放了一份字体纹理，这个选项允许您切换使用的字体的位置来“切换字体”。

杼榅材质戊边漫划 自 2020 年 v1.4 开始利用该功能。

在 1.6.x 之后、1.12.2 之前的 OptiFine 确实会继续试图修复使用第三方字体包时原版怪异的字体渲染，就像 1.5.2 之前做的那样，但无需开启选项，始终应用。

部分字体的调整差别可能不大。

但 1.13 之后失去了这一功能，装与不装二者基本没有区别了。

1.13.2 OF G5 该选项仍然具有功能，但 1.14 开始这个选项的用处仍在进一步研究，至今 （26.1.2）该选项仍然保留，但笔者在所有测试用例都无法实际使用。

可能确实没有任何作用了，但从 1.14 到 26.1.2 为什么这个选项仍然存在呢？

高版本 Badlion Client 中该选项已经改为强制禁用并给出弃用警告了。
![pasted-20260802100348](/assets/docres/games/minecraft/res/optifine/pasted-20260802100348.webp)
![minecraft-1_w1](/assets/docres/games/minecraft/res/optifine/minecraft-1_w1.webp)

![hd-font](/assets/docres/games/minecraft/res/optifine/hd-font.webp)
![hd-font-2](/assets/docres/games/minecraft/res/optifine/hd-font-2.webp)

## 自定义天空

1.13 后的版本应该可以放心使用`<namespace>`路径，至少在 OptiFine 官方实现下如此。

``` title="/assets/minecraft/optifine/sky/world0/sky1.properties"
startFadeIn=19\:20
blend=add
rotate=true
endFadeIn=20\:00
endFadeOut=7\:35
source=minecraft:mcpatcher/sky/world0/1.png
```
通过类似这样的配置可以使 1.13+ 版本继续使用 MCPatcher 目录的纹理来减少多版本支持资源包的包体体积。

部分旧版本的 MCPPPP 和 [FabricSkyboxes-interop](https://github.com/FlashyReese/nuit-interop/issues/15) 可能无法支持上述路径。

...什么，**[nuit-interop](https://github.com/FlashyReese/nuit-interop)** 诈尸了？

### 混合方式 `blend`
![pasted-20260802083128](/assets/docres/games/minecraft/res/optifine/pasted-20260802083128.webp)



![pasted-20260802082642](/assets/docres/games/minecraft/res/optifine/pasted-20260802082642.webp)
blend=screen
![pasted-20260802082755](/assets/docres/games/minecraft/res/optifine/pasted-20260802082755.webp)
blend=add
![pasted-20260802083003](/assets/docres/games/minecraft/res/optifine/pasted-20260802083003.webp)
add 和 dodge 两行各自
![pasted-20260802083227](/assets/docres/games/minecraft/res/optifine/pasted-20260802083227.webp)
dodge


### 问题参考
#### Badlion Client  MC 1.21.5+ 光敏性癫痫警告
已测试在 Badlion Client v4.4.4-f8775e4-PRODUCTION4(1.21.5,1.21.9,1.21.10)中的 “OptiFine” (Betterframes) 自定义天空具有高强度闪屏的恶劣问题。

具体呈现为天空呈现变为 高强度“逐帧”改变原版天空和资源包内建天空纹理

请在正式开始游戏之前关闭“自定义天空”功能。

如果您需要在 MC 1.21.x+ 版本 使用 自定义天空，建议使用 Skyboxify 等方案。

MC 1.8.9 & 1.21.4 Badlion 没有上述问题。

鉴于 Badlion Client 如今的情况，还是建议左转 Lunar Client 吧。
#### OptiKai ”真的好绿！“

非官方构建 OptiKai 23w13a_or_b-OptiFine_HD_K_I5_pre2 的 自定义天空 实现可能存在问题。

可能会在切换资源包后出现自定义天空黑紫或绿色等状况。

您可以尝试重启游戏，或许可以解决。

![pasted-20260801152839](/assets/docres/games/minecraft/res/optifine/pasted-20260801152839.webp)![pasted-20260801152948](/assets/docres/games/minecraft/res/optifine/pasted-20260801152948.webp)

####  1.21.6+ OptiFine J6_pre1+ 部分 blend 方式失效 (#7937)
![pasted-20260802093523](/assets/docres/games/minecraft/res/optifine/pasted-20260802093523.webp)
![pasted-20260802093456](/assets/docres/games/minecraft/res/optifine/pasted-20260802093456.webp)
天哪，这居然是`blend=burn` 的效果！
为什么在 1.21.4 之前不是呢 XD

OptiFine 1.21.6 J6_pre1 开始自定义天空出现问题，上一个可用版本 1.21.4 J4_pre2 没有问题。

https://github.com/sp614x/optifine/issues/7937