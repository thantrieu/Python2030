# 1. Giới thiệu về biểu đồ đường
# 2. Vẽ biểu đồ đường
# 3. Thiết lập các thành phần cấu thành
# 4. Thiết lập chú thích cho biểu đồ
# 5. Thiết lập lưới cho biểu đồ
import matplotlib.pyplot as plt
import numpy as np

months = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
incomes = np.array([50.6, 47.2, 55.4, 66.6, 45.7, 96.3, 54.8, 80.1, 72.5, 60.4, 74.6, 88.5])
incomes2 = np.array([29.6, 77.2, 45.4, 40.6, 40.7, 44.3, 30.8, 35.1, 38.5, 39.4, 40.6, 54.5])
incomes3 = np.array([35.6, 34.2, 36.4, 46.6, 55.7, 56.3, 64.8, 70.1, 87.5, 89.4, 92.6, 94.5])

# first approach:
plt.plot(months, incomes, color='#800080', marker='o', ls='solid', linewidth=1.25, label='Salary')
plt.plot(months, incomes2, color='#ff5733', marker='o', ls='solid', linewidth=1.25, label='Youtube')
plt.plot(months, incomes3, color='#0000fe', marker='o', ls='solid', linewidth=1.25, label='Business')
# add tick
plt.xticks(months, months)
# add grid
plt.grid(color='gray', linestyle='--', linewidth=0.5)
# add title
plt.title('Thu nhập năm 2025 của tôi')
plt.ylabel('Thu nhập')
plt.xlabel('Tháng')
# show legend
plt.legend()

# second approach:
# fig, ax = plt.subplots()
# ax.plot(months, incomes, color='#800080', marker='o', ls='solid', linewidth=1.25, label='Salary')
# ax.plot(months, incomes2, color='#ff5733', marker='o', ls='solid', linewidth=1.25, label='Youtube')
# ax.plot(months, incomes3, color='#0000fe', marker='o', ls='solid', linewidth=1.25, label='Business')
# ax.legend()
#
# ax.grid(color='gray', linestyle='--', linewidth=0.5)
# ax.set_title('Thu nhập năm 2025 của tôi')
# ax.set_ylabel('Thu nhập')
# ax.set_xlabel('Tháng')
# ax.set_xticks(months, months)
plt.show()
