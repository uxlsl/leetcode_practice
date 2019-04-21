#! -*- coding:utf-8 -*-
import re
import shutil


def main():
    url = input('url:')
    reg = re.compile(r'https://leetcode-cn.com/problems/(.*)/')
    m = reg.match(url)
    title = m.group(1)
    shutil.copytree('template', title)


if __name__ == '__main__':
    main()
