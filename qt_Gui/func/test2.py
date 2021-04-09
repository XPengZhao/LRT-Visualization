import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

plt.figure(12)
axes = plt.subplot(111)

data1 = []
data = [-61.71869468688965, -77.75699806213379, -70.39976787567139, -68.1099100112915, -61.986815452575684, -64.3140811920166, -62.43452262878418, -63.800851821899414, -95.3069658279419, -81.69714164733887, -67.0795841217041, -66.05714988708496, -66.29000854492188, -61.96342658996582, -76.06778812408447, -71.5758056640625]
data = [i+70 for i in data]
print(data)
pre_data = pd.DataFrame([data1[0:4],data1[4:8],data1[8:12],data1[12:]])

sns.set()
sns.heatmap(pre_data,ax=axes,fmt=".3f",center=0.1,vmax=20,vmin=-20,cmap="rainbow_r", annot=True)
sns.cubehelix_palette(as_cmap=True, reverse=True)
plt.show()
# import seaborn as sns
# import matplotlib.pyplot as plt
# import numpy as np
# sns.set()
# data = np.array([[1,2,3],[4,5,6],[7,8,9]])
# sns.heatmap(data,annot=True)
# plt.show()