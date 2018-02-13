#coding : utf-8
import hashlib
import sys
import os
  
def md5hex(word):
    if isinstance(word, str):
        print(1)
        word = word.encode("utf8")
        m = hashlib.md5()
        m.update(word)
        print(m.hexdigest())
    elif not isinstance(word, str):
        print(2)
        word = str(word)
        m = hashlib.md5()
        m.update(word)
    return m.hexdigest()
 
def md5sum(fname):
    """ 计算文件的MD5值
    """
    def read_chunks(fh):
        fh.seek(0)
        chunk = fh.read(8096)
        while chunk:
            yield chunk
            chunk = fh.read(8096)
        else: #最后要将游标放回文件开头
            fh.seek(0)
    m = hashlib.md5()
    if isinstance(fname, str) and os.path.exists(fname):
        with open(fname, "rb") as fh:
            for chunk in read_chunks(fh):
                m.update(chunk)
    #上传的文件缓存 或 已打开的文件流
    elif fname.__class__.__name__ in ["StringIO", "StringO"] or isinstance(fname, file):
        for chunk in read_chunks(fname):
            m.update(chunk)
    else:
        return ""
    return m.hexdigest()

def sha256sum(fname):
    """ 计算文件的sha256值
    """
    def read_chunks(fh):
        fh.seek(0)
        chunk = fh.read(8096)
        while chunk:
            yield chunk
            chunk = fh.read(8096)
        else: #最后要将游标放回文件开头
            fh.seek(0)
    m = hashlib.sha256()
    if isinstance(fname, str) and os.path.exists(fname):
        with open(fname, "rb") as fh:
            for chunk in read_chunks(fh):
                m.update(chunk)
    #上传的文件缓存 或 已打开的文件流
    elif fname.__class__.__name__ in ["StringIO", "StringO"] or isinstance(fname, file):
        for chunk in read_chunks(fname):
            m.update(chunk)
    else:
        return ""
    return m.hexdigest()

def sha1sum(fname):
    """ 计算文件的sha256值
    """
    def read_chunks(fh):
        fh.seek(0)
        chunk = fh.read(8096)
        while chunk:
            yield chunk
            chunk = fh.read(8096)
        else: #最后要将游标放回文件开头
            fh.seek(0)
    m = hashlib.sha1()
    if isinstance(fname, str) and os.path.exists(fname):
        with open(fname, "rb") as fh:
            for chunk in read_chunks(fh):
                m.update(chunk)
    #上传的文件缓存 或 已打开的文件流
    elif fname.__class__.__name__ in ["StringIO", "StringO"] or isinstance(fname, file):
        for chunk in read_chunks(fname):
            m.update(chunk)
    else:
        return ""
    return m.hexdigest()



if __name__ == '__main__':
    index = 1
    result = ''
    for file in os.listdir():
        if os.path.isfile(file): #'.' != file[0] and 
            try:
                file_md5 = md5sum(file)
                file_sha256 = sha256sum(file)
                file_sha1 = sha1sum(file)
                resultmd5 = ('%i\n文件名:%s \n  MD5 :%s'%(index,file,file_md5))
                resultsha1 = (' SHA1 :%s\n'%(file_sha1))
                resultsha = ('SHA256:%s\n'%(file_sha256))
                print(resultmd5)
                print(resultsha1)
                print(resultsha)
                result += resultmd5
                result += resultsha1
                result += resultsha
                index += 1
            except PermissionError:
                resulterr = ('%i\n文件名：%s \n权限不足，无法读取\n'%(index,file))
                print(resulterr)
                result += resulterr
                index += 1
    resultfile = open('电子数据数字指纹计算结果.txt','w+')
    resultfile.write('''
广州市花都区市场监管局电子数据数字指纹计算程序 ver.20180201-01
制作单位：狮岭监管所
联系人：钟思燃
联系电话：661668
功能:本软件基于Python 3.4.4的hashlib库的md5,sha256函数，对软件所在的文件夹的
文件进行MD5和SHA256数字指纹计算，通过对比数字指纹证明相关文件的一致性、完整性。
结果将在命令行窗口显示，并保存在最终生成的“电子数据数字指纹计算结果.txt”文件中。

-------------------处理结果---------------------\n''')
    resultfile.write(result.replace('SHA256','\nSHA256'))
    resultfile.close()
    os.system('pause')
    
