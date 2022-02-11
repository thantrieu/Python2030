import matplotlib.pyplot as plt
import numpy as np

months = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
incomes = np.array([50.6, 47.2, 55.4, 66.6, 45.7, 96.3, 54.8, 80.1, 72.5, 60.4, 74.6, 88.5])
incomes2 = np.array([29.6, 77.2, 45.4, 40.6, 40.7, 44.3, 30.8, 35.1, 38.5, 39.4, 40.6, 54.5])
incomes3 = np.array([35.6, 34.2, 36.4, 46.6, 55.7, 56.3, 64.8, 70.1, 87.5, 89.4, 92.6, 94.5])
# fig, ax = plt.subplots(figsize=(7, 5), layout='constrained')
# ax.plot(months, incomes, marker='o', color='#800080', ls='solid', label='Salary')
# ax.plot(months, incomes2, marker='o', color='#5d3fd3', ls='solid', label='Youtube')
# ax.legend()
#
# ax.grid(color='green', linestyle='--', linewidth=0.5)
# ax.set_title('Thu nhập năm 2025 của tôi')
# ax.set_ylabel('Thu nhập')
# ax.set_xlabel('Tháng')
# ax.set_xticks(months, months)
plt.plot(months, incomes, marker='o', ls='solid', color='#800080', linewidth=1.25, label='Salary') # ms=8, mfc='r',
plt.plot(months, incomes2, marker='o', ls='solid', color='#ff5733', linewidth=1.25, label='Youtube')
plt.plot(months, incomes3, marker='o', ls='solid', color='#0000fe', linewidth=1.25, label='Business')
plt.xticks(months, months)
plt.grid(color='green', linestyle='--', linewidth=0.5)
plt.title('Thu nhập năm 2025 của tôi')
plt.ylabel('Thu nhập')
plt.xlabel('Tháng')
plt.legend()
plt.show()
