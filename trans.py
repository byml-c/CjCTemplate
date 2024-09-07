import re
import os
import json

user_config:dict = json.load(open('config.json', 'r', encoding='utf-8'))
h_template = [
r'''{
  \\\\begin{CJK*}{UTF8}{hei}\\\\zihao{5}
    \\\\vskip 1mm
    \\\\section{-text-}
  \\\\end{CJK*} 
}''',
r'''{
  \\\\begin{CJK*}{UTF8}{hei}
    \\\\subsection{-text-}
  \\\\end{CJK*}  
}''',
r'''\\\\subsubsection{-text-}'''
] 

def md2tex(path='./Readme.md'):
    global h_template
    md_content = open(path, 'r', encoding='utf-8').read()
    tex_content = re.sub(r'^#\s(.*)$', h_template[0].replace('-text-', r'\1'), md_content, flags=re.M)
    tex_content = re.sub(r'^##\s(.*)$', h_template[1].replace('-text-', r'\1'), tex_content, flags=re.M)
    tex_content = re.sub(r'^###\s(.*)$', h_template[2].replace('-text-', r'\1'), tex_content, flags=re.M)
    return tex_content

def main():
    global user_config
    md_path = ''
    while True:
        md_path = input('请输入md文件路径：')
        if os.path.exists(md_path):
            break
        elif os.path.exists(f'{md_path}.md'):
            md_path = f'{md_path}.md'
            break
        else:
            print('文件不存在，请重新输入！')
    output_name = input('请输入输出文件名（默认为 Report）：')
    if output_name == '':
        output_name = 'Report'
    
    tex_template = open('./template/bymlCjCTemplate.tex', 'r', encoding='utf-8').read()
    for key, val in user_config.items():
        tex_template = tex_template.replace(key, val)
    tex_template = re.sub(r'% 正文部分(.*?)% 致谢',
                        f'% 正文部分\n\n{md2tex(md_path)}\n\n% 致谢',
                        tex_template, flags=re.S)
    open(f'./report/{output_name}.tex', 'w', encoding='utf-8').write(tex_template)
    # 复制模板文件
    for fils in ['captionhack.sty', 'picins.sty', 'mtpro2.sty',
                 'CjC.cls', 'llncs.cls', 'tst.cls', 'ref.bib']:
        with open(f'./report/{fils}', 'wb') as f:
            f.write(open(f'./template/{fils}', 'rb').read())
    print(f'转换完成！请打开本路径下的 report 文件夹进行调整和查看。')

if __name__ == '__main__':
    main()