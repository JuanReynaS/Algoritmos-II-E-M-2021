import seaborn as sns
import matplotlib.pyplot as plt
import math
import numpy as np

fmri = sns.load_dataset("fmri")
fmri.head()

sns.lineplot(
    data=fmri, x="timepoint", y="signal", hue="event", err_style="bars", ci=68
)

plt.show()