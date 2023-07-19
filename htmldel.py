import os
# 将某个文件夹下面的html文件进行删除,保留其他文件

def get_file_extension(filename):
    if '.' in filename:
        return filename.rsplit('.', 1)[1].lower()
    else:
        return None
    
def delete_file(filename):
    try:
        os.remove(filename)
        print("文件删除成功",filename)
    except FileNotFoundError:
        print("文件不存在")
    except PermissionError:
        print("没有权限删除文件")

def del_html(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if get_file_extension(filename) == 'html':
            delete_file(file_path)
            

del_html("/opt/doc/15-一线数据库工程师带你深入理解 MySQL")
            