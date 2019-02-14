def shortvariation1(variationPeriod_hours, timeDelta, parameter):
    """
    Calculates the maparameterimum variation in the time window provided
    >>> shortvariation1(variationPeriod_hours=1, timeDelta=15, parameter=[5, 2, 8, 9, 3, 4, 3, 0, 4, 1, 5, 3])  # doctest: +NORMALIZE_WHITESPACE
    array([ nan,  nan,  nan, 7., 7., 6., 6., 4., 4., 4., 5., 4.])
    """
    import numpy as np
    size = len(parameter)
    fluct = np.zeros(size)
    n = int(60*variationPeriod_hours/timeDelta)
    m = n - 1
    for i in range(0, n):
        fluct[i] = np.nan
    for i in range(m, size):
        if np.isnan(parameter[i]):
            fluct[i] = np.nan
        else:
            fluct[i] = abs(np.nanmax(parameter[i-m: i+1]) - np.nanmin(parameter[i-m: i+1]))
    return fluct

if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
