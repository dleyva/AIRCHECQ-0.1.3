# Data Mining: deviations
def outLayers(x, n):

    import pandas as pd
    import numpy as np

    x_rm = pd.DataFrame(x).rolling(window=n, min_periods=1).mean()
    x_mm = x_rm[0].tolist()
    
    std = np.std(x)
    mean = np.mean(x)

    m = len(x)

    mean_c = [mean]*m

    upStd = mean+std
    lowStd = mean-std

    upStd_c = [upStd]*m
    lowStd_c = [lowStd]*m

    difRMean = np.zeros(m)

    for i in range(0, m):
        if x_mm[i] > upStd:
            difRMean[i] = x_mm[i] - upStd
        elif x_mm[i] < lowStd:
            difRMean[i] = x_mm[i] - lowStd

    if np.nanmax(abs(difRMean)) == 0:
        difRMeanNorm = np.zeros(m)
    else:
        difRMeanNorm = difRMean / [np.nanmax(abs(difRMean))]

    return difRMeanNorm
    



