import os
import configparser

# 程序逻辑：检查是否存在配置文件，如果存在，则检查是否正确，不存在，则新建

# # 加载现有配置文件
conf = configparser.ConfigParser()

def editconf(filename):
    conf.add_section(filename)  # 添加section
    global IMG_TYPE, name
    IMG_TYPE = input("请输入待处理的图片格式：")
    name = input("目录：")
    # 为配置文件添加值
    conf.set(filename, 'IMG_TYPE', IMG_TYPE)
    conf.set(filename, 'name', name)
    #     # 写入文件
    with open(filename+'.ini', 'w') as fw:
        conf.write(fw)

def checkconf(filename):
    conf.read(filename+".ini")
    # IMG_TYPE = input("待处理的图片格式")
    print("您的配置文件是：%s" % (conf.items(filename)))

    choice = input("Y/N?: ")
    if choice == "y":
        global IMG_TYPE,name
        IMG_TYPE= conf.get(filename, "IMG_TYPE")
        name = conf.get(filename, 'name')
    else:
        conf.remove_section(filename)
        editconf(filename)

if not os.path.exists("config.ini"):
    print("生成新的配置文件")
    editconf('config')

else:
    print("检查配置文件")
    checkconf('config')
