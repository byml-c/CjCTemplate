# Byml's CjC template
本项目旨在通过调整 [《中国计算机学报》](http://cjc.ict.ac.cn/index.htm)的投稿 LaTeX 模板，使其更加能够更加方便地应用于《智能科学导论》实验课的实验报告撰写。

## 项目特点
1. 对 LaTeX 模板手动格式化，使其具有更好的可读性
2. 修改编码为 UTF-8，使其具有更好的适用性
3. 添加格式填充内容，使基本信息填写更加方便快捷
4. 改用 BibLaTeX 管理参考文献，使参考文献的管理更加方便

## 项目使用
1. clone 本项目
2. 使用 LaTeX 编辑器打开 `template` 文件夹下的 `bymlCjCTemplate.tex` 文件（编码为 UTF-8）
3. 尝试编译，如果遇到字符集问题，可以参考[这篇文章](https://www.bilibili.com/read/cv20507474/)
4. 在当前目录下的 `config.json` 中填写填充的基本信息
5. 运行 `trans.py` 脚本，根据提示将指定 markdown 文件转换为 LaTeX 格式
    - 目前仅支持1、2、3级标题的转换
6. 输出会存放在 `report` 文件夹中，可以直接复制整个文件夹到任何地方进行修改，调整正文、添加参考文献并自行编译