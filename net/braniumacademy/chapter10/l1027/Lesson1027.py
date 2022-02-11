# 1. Giới thiệu biểu đồ hình quạt
# 2. Vẽ biểu đồ quạt
# 3. Thiết lập các thông số liên quan
# 4. Thiết lập vị trí cho legend
import matplotlib.pyplot as plt
import numpy as np

incomes = np.array([600, 300, 400, 500, 450])
colors = ['#800080', '#ff5733', '#dfff00', '#000080', '#008000']
labels = ['Kinh doanh', 'Làm thuê', 'Youtube', 'Khóa học', 'Chứng khoán']
explode = [0.2, 0.1, 0, 0, 0]
plt.pie(incomes, colors=colors, labels=labels, explode=explode,
        shadow=True, startangle=45, autopct='%1.2f%%',
        textprops={'color': '#ffffff'})

# set title
plt.title('Thu nhập năm 2025 của tôi')

# add legend
plt.legend(loc='lower left', title='Các nguồn thu:')
plt.show()
