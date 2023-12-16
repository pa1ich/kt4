import numpy as np
import pandas as pd
from IPython.display import display

data=pd.read_excel("https://raw.githubusercontent.com/junaart/ForStudents/master/Big_Data/Seminar_3/demo26.xlsx",sheet_name="ОПЖ")
display(data)
dframe_new = data.copy()
arr = dframe_new.transpose()
columns = ["FIRST", "SECOND", "THIRD", "FOURTH", "FIFTH", "SIXTH", "SEVENTH", "EIGHTH", "NINTH"]
arr.columns = columns
new = pd.DataFrame(arr)

new['SECOND'] = pd.to_numeric(new['SECOND'], errors='coerce')

mean_second = new['SECOND'].mean()
new = new[new['SECOND'] > mean_second]
even_years = new.index % 2 == 0
print(new[even_years])
import matplotlib.pyplot as plt
plt.plot(new.index, new['THIRD'])
plt.xlabel('Год')
plt.ylabel('Третий столбец')
plt.show()
median_third = new['THIRD'].median()
median_fourth = new['FOURTH'].median()
new['NEW'] = np.where((new['THIRD'] > median_third) & (new['FOURTH'] > median_fourth), 'good', 'bad')
display(data)