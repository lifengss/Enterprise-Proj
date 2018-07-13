# Enterprise-Proj
BOC_POC
中国银行汇率热点预测项目

1.合作选题意见
2.讨论
3.最新版概要设计报告
4.code
   |--data 汇率和新闻数据 .csv格式
   |--NewsSpyder 新闻爬虫
   |--RatePredict 汇率热点预测文件夹，主程序入口
   |  |--RatePredict_V0 大规模数据预处理，需要改写多线程
   |  |--RatePredict_V1 小规模数据训练，已完成训练，需要可视化结果
   |  |  |--data_set_helper.py raw data处理模块，用于从文件读取数据
   |  |  |--DataBaseConnect.py 数据库远程连接，暂时不需要。
   |  |  |--EMHF.hdf5 已经训练好的模型参数文件
   |  |  |--GRU_model.h5 单独采用GRU对汇率预测的模型参数文件
   |  |  |--model_helper.py 用于构建模型的类
   |  |  |--model_plot_test.py 模型结构可视化（需调试）
   |  |  |--news_rate_predict.py 预测程序主入口
   |  |  |--rate.npy 汇率数据npy格式
   |  |  |--Rate_present.py 结果可视化文件
   |  |  |--stop_words.txt 新闻数据NLP所用停止词表
   |  |  |--text_preprocess.py 文本数据预处理类
   |  |  |--tf_idf.npy 文本数据独热编码numpy文件
   |  |  |--y_reg.npy 模型对训练数据的预测输出
   |  |  |--y_train.npy 训练数据的标签（即预测真值）
   |--results 可视化结果保存路径
   |--EMHF_model.jpg 模型结构图
