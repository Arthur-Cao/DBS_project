# -*- coding: utf-8 -*-
# import tensorflow as tf
# import numpy as np
# import matplotlib.pyplot as plt
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from urllib.request import urlopen

total_list = []
total_string = ''
str = ''

def pdf2text(filepath):
     #Open a PDF file.
     #rb 是指以二进制读的形式打开
     fp=open(filepath,"rb")
     #Create a PDF parser object associated with the file object.
     parser=PDFParser(fp)
     #Create a PDF document object that stores the document structure
     doc=PDFDocument()
     #Connect the parser annd document objects.
     parser.set_document(doc)
     doc.set_parser(parser)
     # Supply the password for initialization.
     # (If no password is set, give an empty string.)
     doc.initialize("")
     #创建 PDF 资源管理器
     resource=PDFResourceManager()
     #参数分析器
     laparam=LAParams()
     #创建一个聚合器
     device=PDFPageAggregator(resource,laparams=laparam)
     #创建 PDF 页面解释器
     interpreter=PDFPageInterpreter(resource,device)
     #使用文档对象从页面读取内容

     for page in doc.get_pages():
         #使用页面解释器来读取
         interpreter.process_page(page)
         #使用聚合器来获取内容
         layout=device.get_result()
         for out in layout:
             if hasattr(out,"get_text"):
                 total_list.append(out.get_text())
     total_string = str.join(total_list)
     return total_string


# def add_layer(inputs, in_size, out_size, activation_function=None):
#     Weights = tf.Variable(tf.random_normal([in_size, out_size]))
#     biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)
#     Wx_plus_b = tf.matmul(inputs, Weights) + biases
#     if activation_function is None:
#         outputs = Wx_plus_b
#     else:
#         outputs = activation_function(Wx_plus_b)
#     return outputs
#
# # Make up some real data
# x_data = np.linspace(-1, 1, 300)[:, np.newaxis]
# noise = np.random.normal(0, 0.05, x_data.shape)
# y_data = np.square(x_data) - 0.5 + noise
#
# ##plt.scatter(x_data, y_data)
# ##plt.show()
#
# # define placeholder for inputs to network
# xs = tf.placeholder(tf.float32, [None, 1])
# ys = tf.placeholder(tf.float32, [None, 1])
# # add hidden layer
# l1 = add_layer(xs, 1, 10, activation_function=tf.nn.relu)
# # add output layer
# prediction = add_layer(l1, 10, 1, activation_function=None)
#
# # the error between prediction and real data
# loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys-prediction), reduction_indices=[1]))
# train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)
# # important step
# sess = tf.Session()
# # tf.initialize_all_variables() no long valid from
# # 2017-03-02 if using tensorflow >= 0.12
# if int((tf.__version__).split('.')[1]) < 12 and int((tf.__version__).split('.')[0]) < 1:
#     init = tf.initialize_all_variables()
# else:
#     init = tf.global_variables_initializer()
# sess.run(init)
#
# # plot the real data
# fig = plt.figure()
# ax = fig.add_subplot(1,1,1)
# ax.scatter(x_data, y_data)
# plt.ion()
# plt.show()
#
#
# for i in range(1000):
#     # training
#     sess.run(train_step, feed_dict={xs: x_data, ys: y_data})
#     if i % 50 == 0:
#         # to visualize the result and improvement
#         try:
#             ax.lines.remove(lines[0])
#         except Exception:
#             pass
#         prediction_value = sess.run(prediction, feed_dict={xs: x_data})
#         # plot the prediction
#         lines = ax.plot(x_data, prediction_value, 'r-', lw=5)
#         plt.pause(1)
