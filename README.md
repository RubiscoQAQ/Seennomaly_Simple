# Readme

## 项目运行说明

### 数据预处理

- 由于数据集本身太过庞大无法上传，需要自行下载RICO数据集
  - [animations](https://storage.googleapis.com/crowdstf-rico-uiuc-4540/rico_dataset_v0.1/animations.tar.gz)
  - [interaction traces](https://storage.googleapis.com/crowdstf-rico-uiuc-4540/rico_dataset_v0.1/traces.tar.gz)

- 在项目中设置数据存储的地址
- 运行`get_data.py`从 GIF 中提取单帧图像，还包含清理静态图像等图像处理。
- 运行`get_class.py`获取 label 文件，即 label.txt
- 运行`convert_data_to_tfrecord.py`，它读取 label.txt 并生成 tfrecord。

### 训练

更改`finetune.bat`中的配置并运行。如果运行失败，可能是您使用conda中的python环境导致的。建议将命令复制到IDE中运行

### 特征提取与评估

- 下载评估用数据集
  - https://drive.google.com/file/d/1L68fETqmm2HYz_ZlKbEYxF9f0BI0p7v6/view?usp=sharing
- 加载模型并运行 `extract_features.py` 将典型例子映射到特征空间。运行此命令后，获得 features.p 文件。

- 运行 `evaluation.py` 来计算模型。KNN 搜索算法也在这个文件中。`

## 我的运行过程数据包

上传了一部分较小的运行时信息，可供下载参考

https://rubisco.cn/packages.zip

## 项目结构

- dataset：包含了一些用于数据预处理的函数
  - split_video.py实现了以一个视频作为输入，输出其中重要的界面变化图片，并生成label信息
  - get_data.py实现了从GIF读取图片并生成class信息
  - format_get_class.py实现了对数据中冗余文件的删除，有利于后续处理
  - get_class.py实现了读取所有图片的class信息，并生成一个label信息
  - convert_data_to_tfrecord.py实现了根据label信息将数据打包成tensorflow中可用的格式
  - get_dataset.py实现了将数据打包成可用的数据集

- net：包含了一个工厂类和许多网络模型
  - 工厂类是对这些模型的抽象，可以根据要求调用不同的模型
  - 其余网络模型都是和文件同名的
- preprocessing：包括一个工厂类和两种预处理方法
  - 工厂类可以根据要求调用不同的预处理方法
  - 只有fbn模型使用fbn预处理方法，其余都是用vae预处理方法
- main.py是主要的模型训练入口，需要设置一些参数，详见bat文件
- bat文件是一个可以直接运行的脚本，调整配置后可以直接运行main.py
- extract_features.py提取示例数据的特征
- evaluation.py是对模型效果的评估



