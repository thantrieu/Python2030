# Vẽ biểu đồ cột thể hiện thu nhập từng tháng của bạn trong Python
import matplotlib.pyplot as plt
import matplotlib.pylab as pl
import numpy as np

months = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
incomes = np.array([39.6, 47.2, 55.4, 66.6, 45.7, 96.3, 54.8, 80.1, 72.5, 60.4, 74.6, 98.5])
size = np.arange(len(months))
plt.bar(x=months, height=incomes, color=['#800080', '#5d3fd3'], width=0.8)
fig = pl.gcf()
fig.canvas.manager.set_window_title('Test title')
# fig, ax = plt.subplots()
# ax.set_ylabel('Thu nhập')
# ax.set_xlabel('Tháng')
# ax.bar(size, incomes, color=['#800080', '#5d3fd3'])
# ax.bar_label(ax.containers[0])
# ax.set_title('Thu nhập năm 2025 của tôi')
# ax.set_xticks(size, months)
# fig.set_figwidth(10)
# fig.set_figheight(5)
# ax.legend()
# fig.tight_layout()
plt.xlabel('Tháng')
plt.ylabel('Thu nhập')
plt.title('Thu nhập năm 2025 của tôi')
plt.grid(color='green', linestyle='--', linewidth=0.5)
plt.xticks(months, months)
month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
# plt.figure(figsize=(2, 2))
# plt.tight_layout()
plt.show()

