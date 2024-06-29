import os
import re

def extract_episode_number(filename):
    """
    提取文件名中的集数。
    该函数假设集数是文件名中由两位或三位数字组成的部分。
    """
    # 匹配文件名中的数字部分，假设集数是由两位或三位数字组成的部分
    matches = re.findall(r'\d{2,3}', filename)
    
    if matches:
        # 返回第一个匹配的数字，假设这是集数
        return matches[0]
    return None

def rename_files_in_directory(directory):
    """
    重命名指定目录下的所有文件，仅保留表示集数的数字。
    """
    for filename in os.listdir(directory):
        # 获取文件的完整路径
        file_path = os.path.join(directory, filename)
        
        if os.path.isfile(file_path):
            # 提取文件名中的集数
            episode_number = extract_episode_number(filename)
            
            if episode_number:
                # 获取文件扩展名
                file_extension = os.path.splitext(filename)[1]
                
                # 新的文件名，仅保留集数
                new_filename = episode_number + file_extension
                
                # 新文件的完整路径
                new_file_path = os.path.join(directory, new_filename)
                
                # 重命名文件
                os.rename(file_path, new_file_path)
                print(f'Renamed "{filename}" to "{new_filename}"')

if __name__ == "__main__":
    # 输入目录路径
    directory = input("请输入文件夹路径: ")
    
    if os.path.isdir(directory):
        rename_files_in_directory(directory)
    else:
        print("输入的路径无效，请输入一个有效的文件夹路径。")
