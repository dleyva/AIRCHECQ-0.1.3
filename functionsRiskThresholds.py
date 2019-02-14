def risk_threshold1(x, p1, p2, p3, p4):
    """
    Calculates the risk for the thresholds type 1.

    >>> risk_threshold1(x=[4],p1=5,p2=16,p3=18,p4=25) # doctest: +NORMALIZE_WHITESPACE
    array([ 1.])
    >>> risk_threshold1(x=[10.5],p1=5,p2=16,p3=18,p4=25) # doctest: +NORMALIZE_WHITESPACE
    array([ 0.5])
    >>> risk_threshold1(x=[16],p1=5,p2=16,p3=18,p4=25) # doctest: +NORMALIZE_WHITESPACE
    array([ 0.])
    >>> risk_threshold1(x=[17],p1=5,p2=16,p3=18,p4=25) # doctest: +NORMALIZE_WHITESPACE
    array([ 0.])
    >>> risk_threshold1(x=[21.5],p1=5,p2=16,p3=18,p4=25) # doctest: +NORMALIZE_WHITESPACE
    array([ 0.5])
    >>> risk_threshold1(x=[26],p1=5,p2=16,p3=18,p4=25) # doctest: +NORMALIZE_WHITESPACE
    array([ 1.])
    """
    import numpy as np
    size = len(x)
    risk1 = np.empty(size)
    risk1.fill(np.nan)
    for i in range(0, size):
        if np.isnan(x[i]):
            risk1[i] = np.nan
        elif x[i] <= p1:
            risk1[i] = 1
        elif x[i] <= p2:
            risk1[i] = abs((x[i] - p2) / (p1 - p2))
        elif x[i] < p3:
            risk1[i] = 0
        elif x[i] < p4:
            risk1[i] = abs((x[i] - p3) / (p4 - p3))
        else:
            risk1[i] = 1
    return risk1


def risk_threshold2(x, p1, p2):
    """
    Calculates the risk for the thresholds type 2.

    >>> risk_threshold2(x=[0],p1=0,p2=30) # doctest: +NORMALIZE_WHITESPACE
    array([ 0.])
    >>> risk_threshold2(x=[15],p1=0,p2=30) # doctest: +NORMALIZE_WHITESPACE
    array([ 0.5])
    >>> risk_threshold2(x=[31],p1=0,p2=30) # doctest: +NORMALIZE_WHITESPACE
    array([ 1.])
    """
    import numpy as np
    size = len(x)
    risk2 = np.empty(size)
    for i in range(0, size):
        if np.isnan(x[i]):
            risk2[i] = np.nan
        elif x[i] <= p1:
            risk2[i] = 0
        elif x[i] <= p2:
            risk2[i] = abs((x[i] - p1) / (p2 - p1))
        else:
            risk2[i] = 1
    return risk2


def risk_threshold3(x, p1, p2, r1):
    """
    Calculates the risk for the thresholds type 3.

    >>> risk_threshold3(x=[0],p1=10,p2=30,r1=0.5) # doctest: +NORMALIZE_WHITESPACE
    array([ 0.])
    >>> risk_threshold3(x=[5],p1=10,p2=30,r1=0.5) # doctest: +NORMALIZE_WHITESPACE
    array([ 0.25])
    >>> risk_threshold3(x=[20],p1=10,p2=30,r1=0.5) # doctest: +NORMALIZE_WHITESPACE
    array([ 0.75])
    >>> risk_threshold3(x=[31],p1=10,p2=30,r1=0.5) # doctest: +NORMALIZE_WHITESPACE
    array([ 1.])
    """
    import numpy as np
    size = len(x)
    risk3 = np.empty(size)
    risk3.fill(np.nan)
    for i in range(0, size):
        if np.isnan(x[i]):
            risk3[i] = np.nan
        elif x[i] <= p1:
            risk3[i] = abs(r1 * x[i] / p1)
        elif x[i] <= p2:
            risk3[i] = abs(((1 - r1) * x[i] + r1 * p2 - p1) / (p2 - p1))
        else:
            risk3[i] = 1
    return risk3


def risk_threshold4(x, p1, p2, p3, p4, r1, r2):
    """
    Calculates the risk for the thresholds type 3.

    >>> risk_threshold4(x=[5],p1=10,p2=20,p3=30,p4=40,r1=0.25,r2=0.75) # doctest: +NORMALIZE_WHITESPACE
    array([ 0.])
    >>> risk_threshold4(x=[15],p1=10,p2=20,p3=30,p4=40,r1=0.25,r2=0.75) # doctest: +NORMALIZE_WHITESPACE
    array([ 0.125])
    >>> risk_threshold4(x=[25],p1=10,p2=20,p3=30,p4=40,r1=0.25,r2=0.75) # doctest: +NORMALIZE_WHITESPACE
    array([ 0.5])
    >>> risk_threshold4(x=[35],p1=10,p2=20,p3=30,p4=40,r1=0.25,r2=0.75) # doctest: +NORMALIZE_WHITESPACE
    array([ 0.875])
    >>> risk_threshold4(x=[45],p1=10,p2=20,p3=30,p4=40,r1=0.25,r2=0.75) # doctest: +NORMALIZE_WHITESPACE
    array([ 1.])
    >>> risk_threshold4(x=[35],p1=10,p2='nan',p3=30,p4=40,r1=0.25,r2=0.75) # doctest: +NORMALIZE_WHITESPACE
    array([ 0.875])
    """
    import numpy as np
    size = len(x)
    risk4 = np.empty(size)
    risk4.fill(np.nan)
    if p1 != 'nan' and p2 != 'nan' and p3 != 'nan' and p4 != 'nan':
        for i in range(0, size):
            if np.isnan(x[i]):
                risk4[i] = np.nan
            elif x[i] <= p1:
                risk4[i] = 0
            elif x[i] <= p2:
                risk4[i] = abs(r1 * (x[i] - p1) / (p2 - p1))
            elif x[i] <= p3:
                risk4[i] = abs(((r2 - r1) * x[i] + r1 * p3 - r2 * p2) / (p3 - p2))
            elif x[i] <= p4:
                risk4[i] = abs(((1 - r2) * x[i] + r2 * p4 - p3) / (p4 - p3))
            else:
                risk4[i] = 1
    elif p2 == 'nan' and p1 != 'nan' and p3 != 'nan' and p4 != 'nan':
        for i in range(0, size):
            if np.isnan(x[i]):
                risk4[i] = np.nan
            elif x[i] <= p1:
                risk4[i] = 0
            elif x[i] <= p3:
                risk4[i] = abs(r2 * (x[i] - p1) / (p3 - p1))
            elif x[i] <= p4:
                risk4[i] = abs(((1 - r2) * x[i] + r2 * p4 - p3) / (p4 - p3))
            else:
                risk4[i] = 1
    elif p3 == 'nan' and p1 != 'nan' and p2 != 'nan' and p4 != 'nan':
        for i in range(0, size):
            if np.isnan(x[i]):
                risk4[i] = np.nan
            elif x[i] <= p1:
                risk4[i] = 0
            elif x[i] <= p2:
                risk4[i] = abs(r1 * (x[i] - p1) / (p2 - p1))
            elif x[i] <= p4:
                risk4[i] = abs(((1 - r1) * x[i] + r1 * p4 - p2) / (p4 - p2))
            else:
                risk4[i] = 1
    elif p2 == 'nan' and p3 == 'nan' and p1 != 'nan' and p4 != 'nan':
        for i in range(0, size):
            if np.isnan(x[i]):
                risk4[i] = np.nan
            elif x[i] <= p1:
                risk4[i] = 0
            elif x[i] <= p4:
                risk4[i] = abs((x[i] - p1) / (p4 - p1))
            else:
                risk4[i] = 1
    return risk4


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
