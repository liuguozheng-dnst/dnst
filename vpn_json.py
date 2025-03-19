import json

# 读取 JSON 文件的函数
def read_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

# 写入文本文件的函数
def write_to_txt(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

# 主程序
if __name__ == "__main__":
    # 读取 JSON 文件
    json_file_path = 'local_users_2CB8ED4AA028.json'
    try:
        data = read_json(json_file_path)
        
        # 打印整个数据结构
        print("读取的 JSON 数据:", json.dumps(data, ensure_ascii=False, indent=4))

        # 假设 JSON 数据是一个字典，包含一个 'Users' 键
        if 'Users' in data:
            names = []
            for user in data['Users']:  # 遍历每个用户
                print("当前用户数据:", user)  # 打印当前用户数据
                if 'Name' in user:  # 检查 'Name' 字段
                    names.append(user['Name'])  # 添加到列表中
                else:
                    print("未找到 'Name' 字段")  # 如果没有找到，打印提示

            # 将所有名字写入到文本文件
            txt_file_path = 'name_output.txt'
            write_to_txt(txt_file_path, '\n'.join(names))  # 每个名字一行
            print(f"用户名字已写入到 {txt_file_path}")
        else:
            print("JSON 数据中没有 'Users' 键")

    except Exception as e:
        print("读取 JSON 文件时出错:", e)