import os
# 工具类，用于清除get_data生成的冗余文件
root = 'G:\\'
split_image = os.path.join(root, 'split_image')
file_list = os.listdir(split_image)
i = 0
for file in file_list:
    trace_list = os.listdir(os.path.join(split_image,file))
    if len(trace_list)==0:
        os.rmdir(os.path.join(split_image,file))
        i+=1
        continue
    for trace in trace_list:
        path = os.path.join(os.path.join(split_image,file), trace)
        sub = os.listdir(path)
        flag = False
        for f in sub:
            if f=='class_name.txt':
                flag = True
        if not flag:
            for f in sub:
                p = os.path.join(path,f)
                if os.path.isdir(p):
                    for j in os.listdir(p):
                        adds = os.path.join(p,j)
                        os.remove(adds)
                    os.rmdir(p)
                else:
                    os.remove(p)
        sub = os.listdir(path)
        if len(sub) == 0:
            os.rmdir(path)
            i+=1
    print(i)

