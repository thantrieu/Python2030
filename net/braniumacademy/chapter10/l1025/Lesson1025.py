# Giới thiệu về biểu đồ cột trong python
# Cài đặt module
# Vẽ biểu đồ
# Thiết lập nhãn, tiêu đề, vị trí tiêu đề
# Thiết lập màu cho cột
# Thiết lập độ rộng của cột
# Thêm lưới cho biểu đồ
# Chụp màn hình biểu đồ và lưu lại

import matplotlib.pyplot as plt
import matplotlib.pylab as pl
import numpy as np

months = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
incomes = np.array([39.6, 47.2, 55.4, 66.6, 45.7, 96.3, 54.8, 80.1, 72.5, 60.4, 74.6, 98.5])
index = np.arange(len(months))
# plt.bar(x=months, height=incomes, color=['#800080', '#5d3fd3'])
# plt.title('Thu nhập năm 2025 của tôi')
# plt.ylabel('Thu nhập')
# plt.xlabel('Tháng')
# plt.xticks(months, months)

fig, ax = plt.subplots()
ax.set_title('Thu nhập năm 2025')
ax.set_ylabel('Thu nhập')
ax.set_xlabel('Tháng')
ax.bar(index, incomes, color=['#800080', '#5d3fd3'], width=0.3)
ax.bar_label(ax.containers[0])
ax.set_xticks(index, months)
# set figure size
fig.set_figwidth(7)
fig.set_figheight(5)
# set figure title
f = pl.gcf()
f.canvas.manager.set_window_title('My Income')
# add grid
plt.grid(color='green', linestyle='--', linewidth=0.5)
plt.show()
