# IAQ General Index based on Risk functions
def iaq_general1(wf, rhtlth, tmptlth, rtmp, rtmpflu, rrh, rrhflu, rpm, rlux, ruv, rno2, ro3, tmp, rh, size):
    """
    Calculates the general IAQ index based on the maximum risks.
    >>> iaq_general1([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0.2, 0.7], [0.4, 0.2], [0.1, 0.5], [0.2, 0.7], [0.4, 0.2], [0.1, 0.5], [0.2, 0.7], [0.4, 0.2], [0.1, 0.5],[1, 1],[1, 1],[1, 1])
    array([ 0.6,  0.3])
    """
    import numpy as np
    maxRisk = np.empty(size)
    iaq = np.empty(size)
    # RH WF*Risk
    wfriskrh = np.empty(size)
    for i in range(0, size):
        if np.isnan(rh[i]):
            wfriskrh[i] = np.nan
        elif np.isnan(rrh[i]):
            wfriskrh[i] = np.nan
        elif rh[i] >= rhtlth[0, 2] and rh[i] < 75:
            wfriskrh[i] = wf[0, 0]*rrh[i]
        elif rh[i] >= rhtlth[0, 2] and rh[i] >= 75:
            wfriskrh[i] = wf[0, 1]*rrh[i]
        elif rh[i] < rhtlth[0, 2] and rh[i] > rhtlth[0, 1]:
            wfriskrh[i] = rrh[i]
        elif rh[i] < 25:
            wfriskrh[i] = wf[0, 2]*rrh[i]
        else:
            wfriskrh[i] = wf[0, 3]*rrh[i]
    # Tmp WF*Risk
    wfrisktmp = np.empty(size)
    for i in range(0, size):
        if np.isnan(tmp[i]):
            wfrisktmp[i] = np.nan
        elif np.isnan(rtmp[i]):
            wfrisktmp[i] = np.nan
        elif tmp[i] >= tmptlth[0, 2]:
            wfrisktmp[i] = wf[0, 5] * rtmp[i]
        elif tmp[i] < tmptlth[0, 2] and tmp[i] > tmptlth[0, 1]:
            wfrisktmp[i] = rtmp[i]
        elif rh[i] <= tmptlth[0, 1]:
            wfrisktmp[i] = wf[0, 6] * rtmp[i]

    for j in range(0, size):
        maxRisk[j] = np.nanmax([wfriskrh[j], wf[0, 4]*rrhflu[j], wfrisktmp[j], wf[0, 7]*rtmpflu[j], wf[0, 8]*rlux[j],
                         wf[0, 9]*ruv[j], wf[0, 10]*ro3[j], wf[0, 10]*rno2[j], wf[0, 13]*rpm[j]])
        iaq[j] = 1 - maxRisk[j]
    return iaq
