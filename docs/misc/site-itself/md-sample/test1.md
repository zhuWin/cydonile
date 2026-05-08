---
statistics: true
comment: true
---

# Sample #1 实验场！

!!! abstract
    更多的 MkDocs 排版实验，此处仅是实验页，当然也可以看一眼。
    
    猎人笔记的 Cheatsheet 比较规整完善一些

    另可参见 [官方文档](https://squidfunk.github.io/mkdocs-material/reference/admonitions/)

## 碎碎

> 在一行的末尾添加两个或多个空格，然后按回车键,即可创建一个换行(`<br>`)。  
uwu
uwu

**要用H2标题，全写成H1标题不会有右侧目录的！**

:smile:

graph LR
A --> B
B --> C
C --> D

## [TOC]


[TOC]

## 代码块测试

    #include <stdio.h>
    
    int main(void){
        printf("hello sekai\n");
        return 0;
    }
    /**
    真的有人这么写代码块吗？
    **/

```c
#include <stdio.h>

int main(void){
    printf("hello sekai\n");
    return 0;
}
```
## 劝要提示，两种大类型

`!!!` - 正统 admonition 插件, 不可收起详情，可隐藏标题

`???` - 默认折叠详情，可收起详情，不可隐藏标题

`???+` - 默认展开详情，可收起详情，不可隐藏标题

特别支持以外的除默认标题有区别外，没有任何差异。不论你用的是 type, important, note, hint还是啥玩意，两种大类均适用

特别支持的见 Sample #2

GitHub 里的“劝要型引文”并不支持

> [!IMPORTANT]
> **Under Construction**
> <br />Wait for upload. I managed to make this project buildable by Visual C++ 4.2.
> 
> 

### `admonition`

!!! 哎舞萌痴
    however, you’re free to use whatever you want. eg.`!!! 哎舞萌痴`


!!! bug
    bug

???+ bug
    `???+` 样式的

!!! tip
    tip

!!! info
    info

!!! warning
    warning

!!! danger "我是标题，!!!类(admonition)可以略去标题！???+的“不可以！”"
    <center> ⭐ [杼榅材质 CALMiRA ARBOR Pre#3 已经发布！](http://zw.mb233.net/index.php/2025/03/14/%e3%80%90%e6%9d%bc%e6%a6%85%e6%9d%90%e8%b4%a8projectbd%e3%80%91caerula-arbor-pre2/) ⭐ </center>

!!! danger inline ""
    <center> ⭐ [260201: Pslo4MC α#8已经发布！](https://modrinth.com/resourcepack/pslp4mc/changelog) ⭐ </center>
    带上inline的效果

#### 默认行为



!!! attention 
    以下没有特别的属性，所以我也受到上一个inline的影响

!!! caution 
    ...

!!! error 
    ...

!!! note 
    You should note that the title will be automatically capitalized.

!!! note "note"
    除非你特意来了个专门的小写附加标题

If you don’t want a title, use a blank string "":

!!! important
    This is an admonition box without a title string `""`.

    This is the second paragraph.

!!! important ""
    This is an admonition box with a blank title.

!!! important "😱"
    This is an admonition box with a title.


    
???+ success "~~*这***是** `success`~~ ==样式什么的suki=="
    - [**uwu**](/) - uwu
    - [**owo**](/) - owo

==已恢复==~~服务器炸了~~ 荧光笔标注==不能==直接后跟文本，否则 ==土豆爆炸== ！

???+ example "我是example"
    - YYYYMMDD 四个大字：==已恢复==~~服务器炸了~~ 荧光笔标注==不能==直接后跟文本，否则 ==土豆爆炸== ！
    - 20260405 全新项目：[**Chihaya Anon's Laugh**](https://modrinth.com/resourcepack/anon) - 一个简单的末地闪光替换示例
    - 20260404 项目更新：[**Endfield Update Screen**](https://modrinth.com/resourcepack/endfield/changelog) - 1.1.1 - Full music & AF 2026 Support
    - 20260201 项目更新：[**Pslo4MC 伪本地化语言包**](https://modrinth.com/resourcepack/pslp4mc/changelog) - Alpha #8 CALMiRA PLUS


inline 内联 示例1 
uwuw

???+ info inline "info inline"
    <center>页面数：{{pages}} </center>
    
    <center>总字数：{{words}} </center>

???+ info inline "info inline"
    <center>页面数：{{pages}} </center>
    
    <center>总字数：{{words}} </center>

???+ warning "warning" 
    这么乱不要命了啊！

???+ info "套娃！"
    <center>页面数：{{pages}} </center>
    
    <center>总字数：{{words}} </center>
    ???+ info inline "套娃！"
        <center>页面数：{{pages}} </center>

        <center>总字数：{{words}} </center>
        ???+ info  "套娃！"
        ???+ info inline "套娃！"
        ???+ info  "套娃！"
            <center>页面数：{{pages}} </center>

            <center>总字数：{{words}} </center>
        <center>页面数：{{pages}} </center>

        <center>总字数：{{words}} </center>

inline 内联 示例2

???+ info inline "info inline"
    <center>页面数：{{pages}} </center>
    
    <center>总字数：{{words}} </center>

???+ info  "info  不加inline可以用来终结inline"
    “适用于???+的标题,标题无意多加了空格的包容处理”
    其实inline与非inline在同一行并没有对齐，不清楚是否为设计所然，~~但是真的强迫症受不了~~
    

???+ warning "warning" 
    这么乱不要命了啊！

???+ info "套娃！"
    <center>页面数：{{pages}} </center>
    
    <center>总字数：{{words}} </center>
    ???+ info inline "套娃！"
        <center>页面数：{{pages}} </center>

        <center>总字数：{{words}} </center>
        ???+ info  "套娃！"
        ???+ info inline "套娃！"
        ???+ info  "套娃！"
            <center>页面数：{{pages}} </center>

            <center>总字数：{{words}} </center>
        <center>页面数：{{pages}} </center>

        <center>总字数：{{words}} </center>


???+ warning "施工中！" 
    <center>[![GitHub stars](https://img.shields.io/github/stars/zhuWin/NaLinux.svg?style=social&label=Stars)](https://github.com/zhuWin/NaLinux)</center>

    <center>我是center</center>

???+ success "朋友们！"
    （欢迎友链！）

    - [1](/) - 1
    - [2](/) - 2


<center><img src="/assets/img/logo-1x1.png"/></center>