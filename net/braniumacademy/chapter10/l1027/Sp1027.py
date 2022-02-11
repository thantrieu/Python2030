import matplotlib.pyplot as plt
import numpy as np

incomes = np.array([500, 300, 400, 500, 450])
labels = ['Kinh doanh', 'Làm thuê', 'Youtube', 'Khóa học', 'Chứng khoán']
colors = ['#800080', '#ff5733', '#dfff00', '#000080', '#008000']
myexplode = [0.2, 0.1, 0.1, 0, 0]
plt.pie(incomes, labels=labels, explode=myexplode, shadow=True, colors=colors)

plt.grid(color='gray', linestyle='--', linewidth=0.5)
# add title
plt.title('Thu nhập năm 2025 của tôi')
# show legend
plt.legend(title='Các nguồn thu:', loc=3)

plt.show()
