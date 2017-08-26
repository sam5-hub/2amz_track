from zipfile import ZipFile
from scrapy.utils.project import get_project_settings
from datetime import datetime
import os
import re

settings = get_project_settings()
today = datetime.now().strftime('%y-%m-%d')
resource_path = settings.attributes.get('IMAGES_STORE').value
ch_special = re.compile(r'[<>|\\/:*?"]')


def make_resource_zip(zip_path=resource_path):
    zip_dir = zip_path
    zip_file = os.path.join(zip_path, today + '.zip')

    zipf = ZipFile(zip_file, 'w')
    pre_len = len(os.path.dirname(zip_dir))
    for parent, dirnames, filenames in os.walk(zip_dir):
        for filename in filenames:
            if ".DS_Store" not in filename and '.zip' not in filename:
                pathfile = os.path.join(parent, filename)
                arcname = pathfile[pre_len:].strip(os.path.sep)  # 相对路径
                zipf.write(pathfile, arcname)
    zipf.close()
    return zip_file


def remove_full_path():
    full_path = os.path.join(resource_path, 'full')
    os.removedirs(full_path)

    

def cn_special_func(match):
    if match.group(0) in "<>|\/?":
        return '-'
    else:
        return ''

# def regularize_filename(filename):
#     '''清理文件名'''
#     # <>|\/:*?"
#     new_name = filename.replace('>', '-').replace('<', '-').replace('|', '-').replace('\\', '-').replace('/',
#                                                                                                          '-').replace(
#         ':', '').replace('*', '').replace('?', '-').replace(r'"', r'')
#     return new_name
def regularize_filename(filename):
    new_filename = res.sub(cn_special_func,filename)
    return new_filename
