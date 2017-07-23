__author__ = 'bharat'
# !/usr/bin/python
import os
import argparse

def filesearch(ext,path):
    pathjoin=os.path.join(path)
    filing= open('/home/bharat/fileextentionout.txt','wb')
    for r, d, f in os.walk(pathjoin):
        for files in f:
            if files.endswith(ext):
                filing.write(os.path.join(r,files)+'\n')
    filing.close()


def main():
    parser = argparse.ArgumentParser(description="This is out Description")
    parser.add_argument('--path', type=str, help="Path is required", required=True)
    parser.add_argument('--ext', type=str, help="Type Extention you want to run to remote system such as txt", required=True)
    parser.add_argument('-o', type=str, help="This is Optional", required=False)
    cmd_argu = parser.parse_args()
    pat = cmd_argu.path
    ext = cmd_argu.ext
    if pat and ext:
        filesearch(ext,pat)
    if os.path.isfile("/home/bharat/fileextentionout.txt"):
        f = open('/home/bharat/fileextentionout.txt','rb')
        print('{0}\n '.format(f.read()))
        f.close()


if __name__ == '__main__':
    main()
