# -*- coding: utf-8 -*-
import os
import time
import re
#str.split(string)分割字符串
#'连接符'.join(list) 将列表组成字符串
def change_name(path):
    global i
    if not os.path.isdir(path) and not os.path.isfile(path):
        return False
    if os.path.isfile(path):
        file_path = os.path.split(path) #分割出目录与文件
        lists = file_path[1].split('.') #分割出文件与文件扩展名
        filename = file_path[0].split('\\')  # 分割出文件夹路径
        file_ext = lists[-1] #取出后缀名(列表切片操作)
        img_ext = ['bmp','jpeg','gif','psd','png','jpg']
        if file_ext in img_ext:
            # os.rename(path,file_path[0]+'/'+lists[0]+'_fc.'+file_ext)
            os.rename(path, file_path[0] + '\\' + file_path[1]+'cd' + '.' + file_ext)
        #或者
        #img_ext = 'bmp|jpeg|gif|psd|png|jpg'
        #if file_ext in img_ext:
        #    print('ok---'+file_ext)
    elif os.path.isdir(path):
        for x in os.listdir(path):
            change_name(os.path.join(path,x)) #os.path.join()在路径处理上很有用

def change_name1(path,k):#当且仅当path为图片路径，图片序号k才会进入重新命名序号里面。
    global i
    if not os.path.isdir(path) and not os.path.isfile(path):
        return False
    if os.path.isfile(path):
        file_path = os.path.split(path) #分割出目录与文件
        lists = file_path[1].split('.') #分割出文件与文件扩展名
        filename = file_path[0].split('\\')  # 分割出文件夹路径
        file_ext = lists[-1] #取出后缀名(列表切片操作)
        img_ext = ['bmp','jpeg','gif','psd','png','jpg']
        if file_ext in img_ext:
            # os.rename(path,file_path[0]+'/'+lists[0]+'_fc.'+file_ext)
            os.rename(path, file_path[0] + '\\' + filename[-1]+str(k) + '.' + file_ext)
            i+=1 #注意这里的i是一个陷阱

    elif os.path.isdir(path):
        k=1#定义照片排序序号
        for x in os.listdir(path):
            if os.path.isdir(x):
                change_name1(os.path.join(path,x),1) #如果遇到文件夹则继续搜索其内部文件夹
            else:
                change_name1(os.path.join(path,x),k)#如果遇到图片文件则进行排序处理
                k+=1

img_dir = r'H:\808'
img_dir = img_dir.replace('\\','/')
start = time.time()
i = 0
change_name(img_dir)#首先遍历所有文件，并在图片后面增加cd后缀，这样可以避免在以1-10排序的图片报错。这是由于列表排序无规
                    #则，导致存在重命名和已有文件重名的报错。
change_name1(img_dir,1)#
c = time.time() - start
print('程序运行耗时:%0.2f'%(c))
print('总共处理了 %s 张图片'%(i))



