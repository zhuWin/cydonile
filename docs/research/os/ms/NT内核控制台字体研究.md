# NT内核控制台字体研究

WIP

`NtDisplayString` 会根据自己系统语言选择 “Unicode” 转 “ANSI” 转换方式，[hex.pp.ua](https://hex.pp.ua)上有提到过

Win8+ 及 ReactOS 无视

ReactOS bootvid 基于 Unicode 00 位 显示 437 字符会**输出垃圾**

Win2K Beta 2，例如 Build 1877 时期的 bootvid 字体输出在扩展位的 ASCII 区域只会输出垃圾。