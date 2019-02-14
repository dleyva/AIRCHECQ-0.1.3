# Scatter plot of environmental parameter vs environmental parameter
def plotGraph1(elementPlot, figure, X, XTitle, Y, YTitle):
    import matplotlib.pyplot as plt

    plt.rcParams.update({'font.size': 14})

    figure.clear()
    ax = figure.add_subplot(111)
    ax.scatter(X, Y, c='k', s=1, alpha=0.5)
    #ax.xaxis.set_major_locator(plt.MaxNLocator(5))
    ax.set_xlabel(XTitle)
    ax.set_ylabel(YTitle)

    elementPlot.draw()


# Plot of single parameter(env. parameter, IAQindex) vs timestamp
def plotGraph2(elementPlot, figure, X, Y, YTitle, color):
    import matplotlib.pyplot as plt
    import matplotlib.dates as mdates

    plt.rcParams.update({'font.size': 14})

    figure.clear()
    ax = figure.add_subplot(111)
    ax.plot(X, Y, color=color, linewidth=1)
    ax.set_xlim(X[0], X[len(X)-1])
    ax.xaxis.set_major_locator(plt.MaxNLocator(5))
    ax.xaxis_date()
    date_format = mdates.DateFormatter('%Y-%m-%d %H:%M')
    ax.set_ylabel(YTitle)
    ax.xaxis.set_major_formatter(date_format)

    #figure.autofmt_xdate()

    elementPlot.draw()


# Plot of multiple deviations vs timestamp
def plotGraph3(elementPlot, figure, X, Y, color, name):
    import matplotlib.pyplot as plt
    import matplotlib.dates as mdates

    plt.rcParams.update({'font.size': 14})

    ax = figure.add_subplot(111)
    ax.plot(X, Y, color=color, linewidth=1, label=name)
    ax.fill_between(X, 0, Y, color=color, alpha=0.3)
    ax.set_xlim(X[0], X[len(X)-1])
    ax.xaxis.set_major_locator(plt.MaxNLocator(5))
    ax.xaxis_date()
    date_format = mdates.DateFormatter('%Y-%m-%d %H:%M')
    ax.xaxis.set_major_formatter(date_format)
    ax.legend(loc='best')

    elementPlot.draw()


# Plot of IAQindex vs timestamp
def plotGraph4(elementPlot, figure, Z, time, colormap):
    import numpy as np
    import matplotlib.pyplot as plt
    from mpl_toolkits.axes_grid1 import make_axes_locatable
    import matplotlib.dates as mdates
    from matplotlib import cm
    import matplotlib

    Zm1 = np.expand_dims(Z[0], axis=0)
    Zm1 = np.array(Zm1, dtype=np.float64)

    cmap = matplotlib.cm.get_cmap(colormap)
    cmap.set_bad(color='white')

    ax1 = plt.subplot(511)
    img1 = ax1.imshow(Zm1, aspect='auto', cmap=cmap, vmin=0, vmax=1,
                      extent=[time[0], time[len(time) - 1], 0, 1])
    divider = make_axes_locatable(ax1)
    cax = divider.append_axes("top", size=0.15, pad=0.35)
    figure.colorbar(img1, cax=cax, orientation='horizontal')
    img1.axes.get_yaxis().set_visible(False)
    img1.axes.get_xaxis().set_visible(False)
    plt.xticks(fontsize=14)
    ax1.xaxis.set_tick_params(labelsize=14)

    Zm2 = np.expand_dims(Z[1], axis=0)
    Zm2 = np.array(Zm2, dtype=np.float64)

    ax2 = plt.subplot(224)
    img2 = ax2.imshow(Zm2, aspect='auto', cmap=cmap, vmin=0, vmax=1,
                      extent=[time[0], time[len(time) - 1], 0, 1])
    img2.axes.get_yaxis().set_visible(False)
    ax2.xaxis.set_major_locator(plt.MaxNLocator(5))
    ax2.xaxis_date()
    date_format = mdates.DateFormatter('%Y-%m-%d %H:%M')
    ax2.xaxis.set_major_formatter(date_format)
    plt.xticks(fontsize=14)
    ax2.xaxis.set_tick_params(labelsize=14)

    figure.suptitle('Title of figure', fontsize=16)
    elementPlot.draw()


def plotGraph5(elementPlot, figure, Z, time, colormap, title, label):
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib.dates as mdates
    from matplotlib import cm
    import matplotlib

    if len(Z) == 1:
        Zm = np.expand_dims(Z[0], axis=0)
        Zm = np.array(Zm, dtype=np.float64)

        cmap = matplotlib.cm.get_cmap(colormap)
        cmap.set_bad(color='white')

        ax = plt.subplot(111)
        img = ax.imshow(Zm, aspect='auto', cmap=cmap, vmin=0, vmax=1,
                        extent=[time[0], time[len(time) - 1], 0, 1])
        img.axes.get_yaxis().set_visible(False)
        ax.xaxis.set_major_locator(plt.MaxNLocator(5))
        ax.xaxis_date()
        date_format = mdates.DateFormatter('%Y-%m-%d %H:%M')
        ax.xaxis.set_major_formatter(date_format)
        plt.xticks(fontsize=14)
        ax.xaxis.set_tick_params(labelsize=14)

        #img.axes.set(ylabel=label[0])
        ax.text(-.01, .5, label[0], va='center', ha='right', fontsize=10, transform=ax.transAxes)

        figure.suptitle(title, fontsize=16)

        figure.subplots_adjust(right=0.85)
        cbar_ax = figure.add_axes([0.9, 0.1, 0.025, 0.8])
        figure.colorbar(img, cax=cbar_ax)

        elementPlot.draw()
    elif len(Z) == 2:
        Zm1 = np.expand_dims(Z[0], axis=0)
        Zm1 = np.array(Zm1, dtype=np.float64)

        cmap = matplotlib.cm.get_cmap(colormap)
        cmap.set_bad(color='white')

        ax1 = plt.subplot(211)
        img1 = ax1.imshow(Zm1, aspect='auto', cmap=cmap, vmin=0, vmax=1,
                          extent=[time[0], time[len(time) - 1], 0, 1])
        img1.axes.get_yaxis().set_visible(False)
        img1.axes.get_xaxis().set_visible(False)

        ax1.text(-.01, .5, label[0], va='center', ha='right', fontsize=10, transform=ax1.transAxes)

        Zm2 = np.expand_dims(Z[1], axis=0)
        Zm2 = np.array(Zm2, dtype=np.float64)
        
        ax2 = plt.subplot(212)
        img2 = ax2.imshow(Zm2, aspect='auto', cmap=cmap, vmin=0, vmax=1,
                          extent=[time[0], time[len(time) - 1], 0, 1])
        img2.axes.get_yaxis().set_visible(False)
        ax2.xaxis.set_major_locator(plt.MaxNLocator(5))
        ax2.xaxis_date()
        date_format = mdates.DateFormatter('%Y-%m-%d %H:%M')
        ax2.xaxis.set_major_formatter(date_format)
        plt.xticks(fontsize=14)
        ax2.xaxis.set_tick_params(labelsize=14)

        ax2.text(-.01, .5, label[1], va='center', ha='right', fontsize=10, transform=ax2.transAxes)
        
        figure.suptitle(title, fontsize=16)

        figure.subplots_adjust(right=0.85)
        cbar_ax = figure.add_axes([0.9, 0.1, 0.025, 0.8])
        figure.colorbar(img1, cax=cbar_ax)

        elementPlot.draw()

        print(len(Zm1))
        print(len(Zm2))

    elif len(Z) == 3:
        Zm1 = np.expand_dims(Z[0], axis=0)
        Zm1 = np.array(Zm1, dtype=np.float64)

        cmap = matplotlib.cm.get_cmap(colormap)
        cmap.set_bad(color='white')

        ax1 = plt.subplot(311)
        img1 = ax1.imshow(Zm1, aspect='auto', cmap=cmap, vmin=0, vmax=1,
                          extent=[time[0], time[len(time) - 1], 0, 1])
        img1.axes.get_yaxis().set_visible(False)
        img1.axes.get_xaxis().set_visible(False)

        ax1.text(-.01, .5, label[0], va='center', ha='right', fontsize=10, transform=ax1.transAxes)

        Zm2 = np.expand_dims(Z[1], axis=0)
        Zm2 = np.array(Zm2, dtype=np.float64)

        ax2 = plt.subplot(312)
        img2 = ax2.imshow(Zm2, aspect='auto', cmap=cmap, vmin=0, vmax=1,
                          extent=[time[0], time[len(time) - 1], 0, 1])
        img2.axes.get_yaxis().set_visible(False)
        img2.axes.get_xaxis().set_visible(False)

        ax2.text(-.01, .5, label[1], va='center', ha='right', fontsize=10, transform=ax2.transAxes)

        Zm3 = np.expand_dims(Z[2], axis=0)
        Zm3 = np.array(Zm3, dtype=np.float64)

        ax3 = plt.subplot(313)
        img3 = ax3.imshow(Zm3, aspect='auto', cmap=cmap, vmin=0, vmax=1,
                          extent=[time[0], time[len(time) - 1], 0, 1])
        img3.axes.get_yaxis().set_visible(False)
        ax3.xaxis.set_major_locator(plt.MaxNLocator(5))
        ax3.xaxis_date()
        date_format = mdates.DateFormatter('%Y-%m-%d %H:%M')
        ax3.xaxis.set_major_formatter(date_format)
        plt.xticks(fontsize=14)
        ax3.xaxis.set_tick_params(labelsize=14)

        ax3.text(-.01, .5, label[2], va='center', ha='right', fontsize=10, transform=ax3.transAxes)

        figure.suptitle(title, fontsize=16)

        figure.subplots_adjust(right=0.85)
        cbar_ax = figure.add_axes([0.9, 0.1, 0.025, 0.8])
        figure.colorbar(img1, cax=cbar_ax)

        elementPlot.draw()
    elif len(Z) == 4:
        Zm1 = np.expand_dims(Z[0], axis=0)
        Zm1 = np.array(Zm1, dtype=np.float64)

        cmap = matplotlib.cm.get_cmap(colormap)
        cmap.set_bad(color='white')

        ax1 = plt.subplot(411)
        img1 = ax1.imshow(Zm1, aspect='auto', cmap=cmap, vmin=0, vmax=1,
                          extent=[time[0], time[len(time) - 1], 0, 1])
        img1.axes.get_yaxis().set_visible(False)
        img1.axes.get_xaxis().set_visible(False)

        ax1.text(-.01, .5, label[0], va='center', ha='right', fontsize=10, transform=ax1.transAxes)

        Zm2 = np.expand_dims(Z[1], axis=0)
        Zm2 = np.array(Zm2, dtype=np.float64)

        ax2 = plt.subplot(412)
        img2 = ax2.imshow(Zm2, aspect='auto', cmap=cmap, vmin=0, vmax=1,
                          extent=[time[0], time[len(time) - 1], 0, 1])
        img2.axes.get_yaxis().set_visible(False)
        img2.axes.get_xaxis().set_visible(False)

        ax2.text(-.01, .5, label[1], va='center', ha='right', fontsize=10, transform=ax2.transAxes)

        Zm3 = np.expand_dims(Z[2], axis=0)
        Zm3 = np.array(Zm3, dtype=np.float64)

        ax3 = plt.subplot(413)
        img3 = ax3.imshow(Zm3, aspect='auto', cmap=cmap, vmin=0, vmax=1,
                          extent=[time[0], time[len(time) - 1], 0, 1])
        img3.axes.get_yaxis().set_visible(False)
        img3.axes.get_xaxis().set_visible(False)

        ax3.text(-.01, .5, label[2], va='center', ha='right', fontsize=10, transform=ax3.transAxes)

        Zm4 = np.expand_dims(Z[3], axis=0)
        Zm4 = np.array(Zm4, dtype=np.float64)

        ax4 = plt.subplot(414)
        img4 = ax4.imshow(Zm4, aspect='auto', cmap=cmap, vmin=0, vmax=1,
                          extent=[time[0], time[len(time) - 1], 0, 1])
        img4.axes.get_yaxis().set_visible(False)
        ax4.xaxis.set_major_locator(plt.MaxNLocator(5))
        ax4.xaxis_date()
        date_format = mdates.DateFormatter('%Y-%m-%d %H:%M')
        ax4.xaxis.set_major_formatter(date_format)
        plt.xticks(fontsize=14)
        ax4.xaxis.set_tick_params(labelsize=14)

        ax4.text(-.01, .5, label[3], va='center', ha='right', fontsize=10, transform=ax4.transAxes)

        figure.suptitle(title, fontsize=16)
        elementPlot.draw()
    elif len(Z) == 5:
        Zm1 = np.expand_dims(Z[0], axis=0)
        Zm1 = np.array(Zm1, dtype=np.float64)

        cmap = matplotlib.cm.get_cmap(colormap)
        cmap.set_bad(color='white')

        ax1 = plt.subplot(511)
        img1 = ax1.imshow(Zm1, aspect='auto', cmap=cmap, vmin=0, vmax=1,
                          extent=[time[0], time[len(time) - 1], 0, 1])
        img1.axes.get_yaxis().set_visible(False)
        img1.axes.get_xaxis().set_visible(False)

        ax1.text(-.01, .5, label[0], va='center', ha='right', fontsize=10, transform=ax1.transAxes)

        Zm2 = np.expand_dims(Z[1], axis=0)
        Zm2 = np.array(Zm2, dtype=np.float64)

        ax2 = plt.subplot(512)
        img2 = ax2.imshow(Zm2, aspect='auto', cmap=cmap, vmin=0, vmax=1,
                          extent=[time[0], time[len(time) - 1], 0, 1])
        img2.axes.get_yaxis().set_visible(False)
        img2.axes.get_xaxis().set_visible(False)

        ax2.text(-.01, .5, label[1], va='center', ha='right', fontsize=10, transform=ax2.transAxes)

        Zm3 = np.expand_dims(Z[2], axis=0)
        Zm3 = np.array(Zm3, dtype=np.float64)

        ax3 = plt.subplot(513)
        img3 = ax3.imshow(Zm3, aspect='auto', cmap=cmap, vmin=0, vmax=1,
                          extent=[time[0], time[len(time) - 1], 0, 1])
        img3.axes.get_yaxis().set_visible(False)
        img3.axes.get_xaxis().set_visible(False)

        ax3.text(-.01, .5, label[2], va='center', ha='right', fontsize=10, transform=ax3.transAxes)

        Zm4 = np.expand_dims(Z[3], axis=0)
        Zm4 = np.array(Zm4, dtype=np.float64)

        ax4 = plt.subplot(514)
        img4 = ax4.imshow(Zm4, aspect='auto', cmap=cmap, vmin=0, vmax=1,
                          extent=[time[0], time[len(time) - 1], 0, 1])
        img4.axes.get_yaxis().set_visible(False)
        img4.axes.get_xaxis().set_visible(False)
        
        ax4.text(-.01, .5, label[3], va='center', ha='right', fontsize=10, transform=ax4.transAxes)

        Zm5 = np.expand_dims(Z[4], axis=0)
        Zm5 = np.array(Zm5, dtype=np.float64)

        ax5 = plt.subplot(515)
        img5 = ax5.imshow(Zm5, aspect='auto', cmap=cmap, vmin=0, vmax=1,
                          extent=[time[0], time[len(time) - 1], 0, 1])
        img5.axes.get_yaxis().set_visible(False)
        ax5.xaxis.set_major_locator(plt.MaxNLocator(5))
        ax5.xaxis_date()
        date_format = mdates.DateFormatter('%Y-%m-%d %H:%M')
        ax5.xaxis.set_major_formatter(date_format)
        plt.xticks(fontsize=14)
        ax5.xaxis.set_tick_params(labelsize=14)

        ax5.text(-.01, .5, label[4], va='center', ha='right', fontsize=10, transform=ax5.transAxes)

        figure.suptitle(title, fontsize=16)

        figure.subplots_adjust(right=0.85)
        cbar_ax = figure.add_axes([0.9, 0.1, 0.025, 0.8])
        figure.colorbar(img1, cax=cbar_ax)

        elementPlot.draw()
    elif len(Z) == 6:
        Zm1 = np.expand_dims(Z[0], axis=0)
        Zm1 = np.array(Zm1, dtype=np.float64)

        cmap = matplotlib.cm.get_cmap(colormap)
        cmap.set_bad(color='white')

        ax1 = plt.subplot(611)
        img1 = ax1.imshow(Zm1, aspect='auto', cmap=cmap, vmin=0, vmax=1,
                          extent=[time[0], time[len(time) - 1], 0, 1])
        img1.axes.get_yaxis().set_visible(False)
        img1.axes.get_xaxis().set_visible(False)

        ax1.text(-.01, .5, label[0], va='center', ha='right', fontsize=10, transform=ax1.transAxes)

        Zm2 = np.expand_dims(Z[1], axis=0)
        Zm2 = np.array(Zm2, dtype=np.float64)

        ax2 = plt.subplot(612)
        img2 = ax2.imshow(Zm2, aspect='auto', cmap=cmap, vmin=0, vmax=1,
                          extent=[time[0], time[len(time) - 1], 0, 1])
        img2.axes.get_yaxis().set_visible(False)
        img2.axes.get_xaxis().set_visible(False)

        ax2.text(-.01, .5, label[1], va='center', ha='right', fontsize=10, transform=ax2.transAxes)

        Zm3 = np.expand_dims(Z[2], axis=0)
        Zm3 = np.array(Zm3, dtype=np.float64)

        ax3 = plt.subplot(613)
        img3 = ax3.imshow(Zm3, aspect='auto', cmap=cmap, vmin=0, vmax=1,
                          extent=[time[0], time[len(time) - 1], 0, 1])
        img3.axes.get_yaxis().set_visible(False)
        img3.axes.get_xaxis().set_visible(False)

        ax3.text(-.01, .5, label[2], va='center', ha='right', fontsize=10, transform=ax3.transAxes)

        Zm4 = np.expand_dims(Z[3], axis=0)
        Zm4 = np.array(Zm4, dtype=np.float64)

        ax4 = plt.subplot(614)
        img4 = ax4.imshow(Zm4, aspect='auto', cmap=cmap, vmin=0, vmax=1,
                          extent=[time[0], time[len(time) - 1], 0, 1])
        img4.axes.get_yaxis().set_visible(False)
        img4.axes.get_xaxis().set_visible(False)

        ax4.text(-.01, .5, label[3], va='center', ha='right', fontsize=10, transform=ax4.transAxes)

        Zm5 = np.expand_dims(Z[4], axis=0)
        Zm5 = np.array(Zm5, dtype=np.float64)

        ax5 = plt.subplot(615)
        img5 = ax5.imshow(Zm5, aspect='auto', cmap=cmap, vmin=0, vmax=1,
                          extent=[time[0], time[len(time) - 1], 0, 1])
        img5.axes.get_yaxis().set_visible(False)
        img5.axes.get_xaxis().set_visible(False)

        ax5.text(-.01, .5, label[4], va='center', ha='right', fontsize=10, transform=ax5.transAxes)

        Zm6 = np.expand_dims(Z[5], axis=0)
        Zm6 = np.array(Zm6, dtype=np.float64)

        ax6 = plt.subplot(616)
        img6 = ax6.imshow(Zm6, aspect='auto', cmap=cmap, vmin=0, vmax=1,
                          extent=[time[0], time[len(time) - 1], 0, 1])
        img6.axes.get_yaxis().set_visible(False)
        ax6.xaxis.set_major_locator(plt.MaxNLocator(5))
        ax6.xaxis_date()
        date_format = mdates.DateFormatter('%Y-%m-%d %H:%M')
        ax6.xaxis.set_major_formatter(date_format)
        plt.xticks(fontsize=14)
        ax6.xaxis.set_tick_params(labelsize=14)

        ax6.text(-.01, .5, label[5], va='center', ha='right', fontsize=10, transform=ax6.transAxes)

        figure.suptitle(title, fontsize=16)

        figure.subplots_adjust(right=0.85)
        cbar_ax = figure.add_axes([0.9, 0.1, 0.025, 0.8])
        figure.colorbar(img1, cax=cbar_ax)

        elementPlot.draw()
    elif len(Z) == 7:
        Zm1 = np.expand_dims(Z[0], axis=0)
        Zm1 = np.array(Zm1, dtype=np.float64)

        cmap = matplotlib.cm.get_cmap(colormap)
        cmap.set_bad(color='white')

        ax1 = plt.subplot(711)
        img1 = ax1.imshow(Zm1, aspect='auto', cmap=cmap, vmin=0, vmax=1,
                          extent=[time[0], time[len(time) - 1], 0, 1])
        img1.axes.get_yaxis().set_visible(False)
        img1.axes.get_xaxis().set_visible(False)

        ax1.text(-.01, .5, label[0], va='center', ha='right', fontsize=10, transform=ax1.transAxes)

        Zm2 = np.expand_dims(Z[1], axis=0)
        Zm2 = np.array(Zm2, dtype=np.float64)

        ax2 = plt.subplot(712)
        img2 = ax2.imshow(Zm2, aspect='auto', cmap=cmap, vmin=0, vmax=1,
                          extent=[time[0], time[len(time) - 1], 0, 1])
        img2.axes.get_yaxis().set_visible(False)
        img2.axes.get_xaxis().set_visible(False)

        ax2.text(-.01, .5, label[1], va='center', ha='right', fontsize=10, transform=ax2.transAxes)

        Zm3 = np.expand_dims(Z[2], axis=0)
        Zm3 = np.array(Zm3, dtype=np.float64)

        ax3 = plt.subplot(713)
        img3 = ax3.imshow(Zm3, aspect='auto', cmap=cmap, vmin=0, vmax=1,
                          extent=[time[0], time[len(time) - 1], 0, 1])
        img3.axes.get_yaxis().set_visible(False)
        img3.axes.get_xaxis().set_visible(False)

        ax3.text(-.01, .5, label[2], va='center', ha='right', fontsize=10, transform=ax3.transAxes)

        Zm4 = np.expand_dims(Z[3], axis=0)
        Zm4 = np.array(Zm4, dtype=np.float64)

        ax4 = plt.subplot(714)
        img4 = ax4.imshow(Zm4, aspect='auto', cmap=cmap, vmin=0, vmax=1,
                          extent=[time[0], time[len(time) - 1], 0, 1])
        img4.axes.get_yaxis().set_visible(False)
        img4.axes.get_xaxis().set_visible(False)

        ax4.text(-.01, .5, label[3], va='center', ha='right', fontsize=10, transform=ax4.transAxes)

        Zm5 = np.expand_dims(Z[4], axis=0)
        Zm5 = np.array(Zm5, dtype=np.float64)

        ax5 = plt.subplot(715)
        img5 = ax5.imshow(Zm5, aspect='auto', cmap=cmap, vmin=0, vmax=1,
                          extent=[time[0], time[len(time) - 1], 0, 1])
        img5.axes.get_yaxis().set_visible(False)
        img5.axes.get_xaxis().set_visible(False)

        ax5.text(-.01, .5, label[4], va='center', ha='right', fontsize=10, transform=ax5.transAxes)

        Zm6 = np.expand_dims(Z[5], axis=0)
        Zm6 = np.array(Zm6, dtype=np.float64)

        ax6 = plt.subplot(716)
        img6 = ax6.imshow(Zm6, aspect='auto', cmap=cmap, vmin=0, vmax=1,
                          extent=[time[0], time[len(time) - 1], 0, 1])
        img6.axes.get_yaxis().set_visible(False)
        img6.axes.get_xaxis().set_visible(False)

        ax6.text(-.01, .5, label[5], va='center', ha='right', fontsize=10, transform=ax6.transAxes)

        Zm7 = np.expand_dims(Z[6], axis=0)
        Zm7 = np.array(Zm7, dtype=np.float64)

        ax7 = plt.subplot(717)
        img7 = ax7.imshow(Zm7, aspect='auto', cmap=cmap, vmin=0, vmax=1,
                          extent=[time[0], time[len(time) - 1], 0, 1])
        img7.axes.get_yaxis().set_visible(False)
        ax7.xaxis.set_major_locator(plt.MaxNLocator(5))
        ax7.xaxis_date()
        date_format = mdates.DateFormatter('%Y-%m-%d %H:%M')
        ax7.xaxis.set_major_formatter(date_format)
        plt.xticks(fontsize=14)
        ax7.xaxis.set_tick_params(labelsize=14)

        ax7.text(-.01, .5, label[6], va='center', ha='right', fontsize=10, transform=ax7.transAxes)

        figure.suptitle(title, fontsize=16)

        figure.subplots_adjust(right=0.85)
        cbar_ax = figure.add_axes([0.9, 0.1, 0.025, 0.8])
        figure.colorbar(img1, cax=cbar_ax)

        elementPlot.draw()
    elif len(Z) == 8:
        Zm1 = np.expand_dims(Z[0], axis=0)
        Zm1 = np.array(Zm1, dtype=np.float64)

        cmap = matplotlib.cm.get_cmap(colormap)
        cmap.set_bad(color='white')

        ax1 = plt.subplot(811)
        img1 = ax1.imshow(Zm1, aspect='auto', cmap=cmap, vmin=0, vmax=1,
                          extent=[time[0], time[len(time) - 1], 0, 1])
        img1.axes.get_yaxis().set_visible(False)
        img1.axes.get_xaxis().set_visible(False)

        ax1.text(-.01, .5, label[0], va='center', ha='right', fontsize=10, transform=ax1.transAxes)

        Zm2 = np.expand_dims(Z[1], axis=0)
        Zm2 = np.array(Zm2, dtype=np.float64)

        ax2 = plt.subplot(812)
        img2 = ax2.imshow(Zm2, aspect='auto', cmap=cmap, vmin=0, vmax=1,
                          extent=[time[0], time[len(time) - 1], 0, 1])
        img2.axes.get_yaxis().set_visible(False)
        img2.axes.get_xaxis().set_visible(False)

        ax2.text(-.01, .5, label[1], va='center', ha='right', fontsize=10, transform=ax2.transAxes)

        Zm3 = np.expand_dims(Z[2], axis=0)
        Zm3 = np.array(Zm3, dtype=np.float64)

        ax3 = plt.subplot(813)
        img3 = ax3.imshow(Zm3, aspect='auto', cmap=cmap, vmin=0, vmax=1,
                          extent=[time[0], time[len(time) - 1], 0, 1])
        img3.axes.get_yaxis().set_visible(False)
        img3.axes.get_xaxis().set_visible(False)

        ax3.text(-.01, .5, label[2], va='center', ha='right', fontsize=10, transform=ax3.transAxes)

        Zm4 = np.expand_dims(Z[3], axis=0)
        Zm4 = np.array(Zm4, dtype=np.float64)

        ax4 = plt.subplot(814)
        img4 = ax4.imshow(Zm4, aspect='auto', cmap=cmap, vmin=0, vmax=1,
                          extent=[time[0], time[len(time) - 1], 0, 1])
        img4.axes.get_yaxis().set_visible(False)
        img4.axes.get_xaxis().set_visible(False)

        ax4.text(-.01, .5, label[3], va='center', ha='right', fontsize=10, transform=ax4.transAxes)

        Zm5 = np.expand_dims(Z[4], axis=0)
        Zm5 = np.array(Zm5, dtype=np.float64)

        ax5 = plt.subplot(815)
        img5 = ax5.imshow(Zm5, aspect='auto', cmap=cmap, vmin=0, vmax=1,
                          extent=[time[0], time[len(time) - 1], 0, 1])
        img5.axes.get_yaxis().set_visible(False)
        img5.axes.get_xaxis().set_visible(False)

        ax5.text(-.01, .5, label[4], va='center', ha='right', fontsize=10, transform=ax5.transAxes)

        Zm6 = np.expand_dims(Z[5], axis=0)
        Zm6 = np.array(Zm6, dtype=np.float64)

        ax6 = plt.subplot(816)
        img6 = ax6.imshow(Zm6, aspect='auto', cmap=cmap, vmin=0, vmax=1,
                          extent=[time[0], time[len(time) - 1], 0, 1])
        img6.axes.get_yaxis().set_visible(False)
        img6.axes.get_xaxis().set_visible(False)

        ax6.text(-.01, .5, label[5], va='center', ha='right', fontsize=10, transform=ax6.transAxes)

        Zm7 = np.expand_dims(Z[6], axis=0)
        Zm7 = np.array(Zm7, dtype=np.float64)

        ax7 = plt.subplot(817)
        img7 = ax7.imshow(Zm7, aspect='auto', cmap=cmap, vmin=0, vmax=1,
                          extent=[time[0], time[len(time) - 1], 0, 1])
        img7.axes.get_yaxis().set_visible(False)
        img7.axes.get_xaxis().set_visible(False)

        ax7.text(-.01, .5, label[6], va='center', ha='right', fontsize=10, transform=ax7.transAxes)

        Zm8 = np.expand_dims(Z[7], axis=0)
        Zm8 = np.array(Zm8, dtype=np.float64)

        ax8 = plt.subplot(818)
        img8 = ax8.imshow(Zm8, aspect='auto', cmap=cmap, vmin=0, vmax=1,
                          extent=[time[0], time[len(time) - 1], 0, 1])
        img8.axes.get_yaxis().set_visible(False)
        ax8.xaxis.set_major_locator(plt.MaxNLocator(5))
        ax8.xaxis_date()
        date_format = mdates.DateFormatter('%Y-%m-%d %H:%M')
        ax8.xaxis.set_major_formatter(date_format)
        plt.xticks(fontsize=14)
        ax8.xaxis.set_tick_params(labelsize=14)

        ax7.text(-.01, .5, label[6], va='center', ha='right', fontsize=10, transform=ax7.transAxes)

        figure.suptitle(title, fontsize=16)

        figure.subplots_adjust(right=0.85)
        cbar_ax = figure.add_axes([0.9, 0.1, 0.025, 0.8])
        figure.colorbar(img1, cax=cbar_ax)

        elementPlot.draw()
    elif len(Z) == 9:
        Zm1 = np.expand_dims(Z[0], axis=0)
        Zm1 = np.array(Zm1, dtype=np.float64)

        cmap = matplotlib.cm.get_cmap(colormap)
        cmap.set_bad(color='white')

        ax1 = plt.subplot(911)
        img1 = ax1.imshow(Zm1, aspect='auto', cmap=cmap, vmin=0, vmax=1,
                          extent=[time[0], time[len(time) - 1], 0, 1])
        img1.axes.get_yaxis().set_visible(False)
        img1.axes.get_xaxis().set_visible(False)

        ax1.text(-.01, .5, label[0], va='center', ha='right', fontsize=10, transform=ax1.transAxes)

        Zm2 = np.expand_dims(Z[1], axis=0)
        Zm2 = np.array(Zm2, dtype=np.float64)

        ax2 = plt.subplot(912)
        img2 = ax2.imshow(Zm2, aspect='auto', cmap=cmap, vmin=0, vmax=1,
                          extent=[time[0], time[len(time) - 1], 0, 1])
        img2.axes.get_yaxis().set_visible(False)
        img2.axes.get_xaxis().set_visible(False)

        ax2.text(-.01, .5, label[1], va='center', ha='right', fontsize=10, transform=ax2.transAxes)

        Zm3 = np.expand_dims(Z[2], axis=0)
        Zm3 = np.array(Zm3, dtype=np.float64)

        ax3 = plt.subplot(913)
        img3 = ax3.imshow(Zm3, aspect='auto', cmap=cmap, vmin=0, vmax=1,
                          extent=[time[0], time[len(time) - 1], 0, 1])
        img3.axes.get_yaxis().set_visible(False)
        img3.axes.get_xaxis().set_visible(False)

        ax3.text(-.01, .5, label[2], va='center', ha='right', fontsize=10, transform=ax3.transAxes)

        Zm4 = np.expand_dims(Z[3], axis=0)
        Zm4 = np.array(Zm4, dtype=np.float64)

        ax4 = plt.subplot(914)
        img4 = ax4.imshow(Zm4, aspect='auto', cmap=cmap, vmin=0, vmax=1,
                          extent=[time[0], time[len(time) - 1], 0, 1])
        img4.axes.get_yaxis().set_visible(False)
        img4.axes.get_xaxis().set_visible(False)

        ax4.text(-.01, .5, label[3], va='center', ha='right', fontsize=10, transform=ax4.transAxes)

        Zm5 = np.expand_dims(Z[4], axis=0)
        Zm5 = np.array(Zm5, dtype=np.float64)

        ax5 = plt.subplot(915)
        img5 = ax5.imshow(Zm5, aspect='auto', cmap=cmap, vmin=0, vmax=1,
                          extent=[time[0], time[len(time) - 1], 0, 1])
        img5.axes.get_yaxis().set_visible(False)
        img5.axes.get_xaxis().set_visible(False)

        ax5.text(-.01, .5, label[4], va='center', ha='right', fontsize=10, transform=ax5.transAxes)

        Zm6 = np.expand_dims(Z[5], axis=0)
        Zm6 = np.array(Zm6, dtype=np.float64)

        ax6 = plt.subplot(916)
        img6 = ax6.imshow(Zm6, aspect='auto', cmap=cmap, vmin=0, vmax=1,
                          extent=[time[0], time[len(time) - 1], 0, 1])
        img6.axes.get_yaxis().set_visible(False)
        img6.axes.get_xaxis().set_visible(False)

        ax6.text(-.01, .5, label[5], va='center', ha='right', fontsize=10, transform=ax6.transAxes)

        Zm7 = np.expand_dims(Z[6], axis=0)
        Zm7 = np.array(Zm7, dtype=np.float64)

        ax7 = plt.subplot(917)
        img7 = ax7.imshow(Zm7, aspect='auto', cmap=cmap, vmin=0, vmax=1,
                          extent=[time[0], time[len(time) - 1], 0, 1])
        img7.axes.get_yaxis().set_visible(False)
        img7.axes.get_xaxis().set_visible(False)

        ax7.text(-.01, .5, label[6], va='center', ha='right', fontsize=10, transform=ax7.transAxes)

        Zm8 = np.expand_dims(Z[7], axis=0)
        Zm8 = np.array(Zm8, dtype=np.float64)

        ax8 = plt.subplot(918)
        img8 = ax8.imshow(Zm8, aspect='auto', cmap=cmap, vmin=0, vmax=1,
                          extent=[time[0], time[len(time) - 1], 0, 1])
        img8.axes.get_yaxis().set_visible(False)
        img8.axes.get_xaxis().set_visible(False)

        ax8.text(-.01, .5, label[7], va='center', ha='right', fontsize=10, transform=ax8.transAxes)

        Zm9 = np.expand_dims(Z[8], axis=0)
        Zm9 = np.array(Zm9, dtype=np.float64)

        ax9 = plt.subplot(919)
        img9 = ax9.imshow(Zm9, aspect='auto', cmap=cmap, vmin=0, vmax=1,
                          extent=[time[0], time[len(time) - 1], 0, 1])
        img9.axes.get_yaxis().set_visible(False)
        ax9.xaxis.set_major_locator(plt.MaxNLocator(5))
        ax9.xaxis_date()
        date_format = mdates.DateFormatter('%Y-%m-%d %H:%M')
        ax9.xaxis.set_major_formatter(date_format)
        plt.xticks(fontsize=14)
        ax9.xaxis.set_tick_params(labelsize=14)

        ax9.text(-.01, .5, label[8], va='center', ha='right', fontsize=10, transform=ax9.transAxes)

        figure.suptitle(title, fontsize=16)

        figure.subplots_adjust(right=0.85)
        cbar_ax = figure.add_axes([0.9, 0.1, 0.025, 0.8])
        figure.colorbar(img1, cax=cbar_ax)

        elementPlot.draw()
    elif len(Z) == 10:
        Zm1 = np.expand_dims(Z[0], axis=0)
        Zm1 = np.array(Zm1, dtype=np.float64)

        cmap = matplotlib.cm.get_cmap(colormap)
        cmap.set_bad(color='white')

        ax1 = plt.subplot(10,1,1)
        img1 = ax1.imshow(Zm1, aspect='auto', cmap=cmap, vmin=0, vmax=1,
                          extent=[time[0], time[len(time) - 1], 0, 1])
        img1.axes.get_yaxis().set_visible(False)
        img1.axes.get_xaxis().set_visible(False)

        ax1.text(-.01, .5, label[0], va='center', ha='right', fontsize=10, transform=ax1.transAxes)

        Zm2 = np.expand_dims(Z[1], axis=0)
        Zm2 = np.array(Zm2, dtype=np.float64)

        ax2 = plt.subplot(10,1,2)
        img2 = ax2.imshow(Zm2, aspect='auto', cmap=cmap, vmin=0, vmax=1,
                          extent=[time[0], time[len(time) - 1], 0, 1])
        img2.axes.get_yaxis().set_visible(False)
        img2.axes.get_xaxis().set_visible(False)

        ax2.text(-.01, .5, label[1], va='center', ha='right', fontsize=10, transform=ax2.transAxes)

        Zm3 = np.expand_dims(Z[2], axis=0)
        Zm3 = np.array(Zm3, dtype=np.float64)

        ax3 = plt.subplot(10,1,3)
        img3 = ax3.imshow(Zm3, aspect='auto', cmap=cmap, vmin=0, vmax=1,
                          extent=[time[0], time[len(time) - 1], 0, 1])
        img3.axes.get_yaxis().set_visible(False)
        img3.axes.get_xaxis().set_visible(False)

        ax3.text(-.01, .5, label[2], va='center', ha='right', fontsize=10, transform=ax3.transAxes)

        Zm4 = np.expand_dims(Z[3], axis=0)
        Zm4 = np.array(Zm4, dtype=np.float64)

        ax4 = plt.subplot(10,1,4)
        img4 = ax4.imshow(Zm4, aspect='auto', cmap=cmap, vmin=0, vmax=1,
                          extent=[time[0], time[len(time) - 1], 0, 1])
        img4.axes.get_yaxis().set_visible(False)
        img4.axes.get_xaxis().set_visible(False)

        ax4.text(-.01, .5, label[3], va='center', ha='right', fontsize=10, transform=ax4.transAxes)

        Zm5 = np.expand_dims(Z[4], axis=0)
        Zm5 = np.array(Zm5, dtype=np.float64)

        ax5 = plt.subplot(10,1,5)
        img5 = ax5.imshow(Zm5, aspect='auto', cmap=cmap, vmin=0, vmax=1,
                          extent=[time[0], time[len(time) - 1], 0, 1])
        img5.axes.get_yaxis().set_visible(False)
        img5.axes.get_xaxis().set_visible(False)

        ax5.text(-.01, .5, label[4], va='center', ha='right', fontsize=10, transform=ax5.transAxes)

        Zm6 = np.expand_dims(Z[5], axis=0)
        Zm6 = np.array(Zm6, dtype=np.float64)

        ax6 = plt.subplot(10,1,6)
        img6 = ax6.imshow(Zm6, aspect='auto', cmap=cmap, vmin=0, vmax=1,
                          extent=[time[0], time[len(time) - 1], 0, 1])
        img6.axes.get_yaxis().set_visible(False)
        img6.axes.get_xaxis().set_visible(False)

        ax6.text(-.01, .5, label[5], va='center', ha='right', fontsize=10, transform=ax6.transAxes)

        Zm7 = np.expand_dims(Z[6], axis=0)
        Zm7 = np.array(Zm7, dtype=np.float64)

        ax7 = plt.subplot(10,1,7)
        img7 = ax7.imshow(Zm7, aspect='auto', cmap=cmap, vmin=0, vmax=1,
                          extent=[time[0], time[len(time) - 1], 0, 1])
        img7.axes.get_yaxis().set_visible(False)
        img7.axes.get_xaxis().set_visible(False)

        ax7.text(-.01, .5, label[6], va='center', ha='right', fontsize=10, transform=ax7.transAxes)

        Zm8 = np.expand_dims(Z[7], axis=0)
        Zm8 = np.array(Zm8, dtype=np.float64)

        ax8 = plt.subplot(10,1,8)
        img8 = ax8.imshow(Zm8, aspect='auto', cmap=cmap, vmin=0, vmax=1,
                          extent=[time[0], time[len(time) - 1], 0, 1])
        img8.axes.get_yaxis().set_visible(False)
        img8.axes.get_xaxis().set_visible(False)

        ax8.text(-.01, .5, label[7], va='center', ha='right', fontsize=10, transform=ax8.transAxes)

        Zm9 = np.expand_dims(Z[8], axis=0)
        Zm9 = np.array(Zm9, dtype=np.float64)

        ax9 = plt.subplot(10,1,9)
        img9 = ax9.imshow(Zm9, aspect='auto', cmap=cmap, vmin=0, vmax=1,
                          extent=[time[0], time[len(time) - 1], 0, 1])
        img9.axes.get_yaxis().set_visible(False)
        img9.axes.get_xaxis().set_visible(False)

        ax9.text(-.01, .5, label[8], va='center', ha='right', fontsize=10, transform=ax9.transAxes)

        Zm10 = np.expand_dims(Z[9], axis=0)
        Zm10 = np.array(Zm10, dtype=np.float64)

        ax10 = plt.subplot(10,1,10)
        img10 = ax10.imshow(Zm10, aspect='auto', cmap=cmap, vmin=0, vmax=1,
                            extent=[time[0], time[len(time) - 1], 0, 1])
        img10.axes.get_yaxis().set_visible(False)
        ax10.xaxis.set_major_locator(plt.MaxNLocator(5))
        ax10.xaxis_date()
        date_format = mdates.DateFormatter('%Y-%m-%d %H:%M')
        ax10.xaxis.set_major_formatter(date_format)
        plt.xticks(fontsize=14)
        ax10.xaxis.set_tick_params(labelsize=14)

        ax10.text(-.01, .5, label[9], va='center', ha='right', fontsize=10, transform=ax10.transAxes)

        figure.suptitle(title, fontsize=16)

        figure.subplots_adjust(right=0.85)
        cbar_ax = figure.add_axes([0.9, 0.1, 0.025, 0.8])
        figure.colorbar(img1, cax=cbar_ax)

        elementPlot.draw()

def plotGraph6(elementPlot, figure, Z, time, colormap, title, label):
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib.dates as mdates
    from matplotlib import cm
    import matplotlib

    if len(Z)!=0:
        cmap = matplotlib.cm.get_cmap(colormap)
        cmap.set_bad(color='white')

        Zm = np.empty(len(Z))
        ax = np.empty(len(Z))
        img = np.empty(len(Z))

        for i in range(0, (len(Z)-1)):
            Zm[i] = np.expand_dims(Z[i], axis=0)
            Zm[i] = np.array(Zm[i], dtype=np.float64)

            ax[i] = plt.subplot(len(Z), 1, (i+1))
            img[i] = ax[i].imshow(Zm[i], aspect='auto', cmap=cmap, vmin=0, vmax=1, extent=[time[0],
                                                                                           time[len(time) - 1], 0, 1])
            img[i].axes.get_yaxis().set_visible(False)
            img[i].axes.get_xaxis().set_visible(False)

            ax[i].text(-.01, .5, label[i], va='center', ha='right', fontsize=10, transform=ax[i].transAxes)
            if i==(len(Z)-1):
                img[i].axes.get_xaxis().set_visible(True)
                ax[i].xaxis.set_major_locator(plt.MaxNLocator(5))
                ax[i].xaxis_date()
                date_format = mdates.DateFormatter('%Y-%m-%d %H:%M')
                ax[i].xaxis.set_major_formatter(date_format)
                plt.xticks(fontsize=14)
                ax[i].xaxis.set_tick_params(labelsize=14)

        figure.suptitle(title, fontsize=16)
        figure.subplots_adjust(right=0.85)
        cbar_ax = figure.add_axes([0.9, 0.1, 0.025, 0.8])
        #figure.colorbar(img[0], cax=cbar_ax)

        elementPlot.draw()

def plotGraph11(elementPlot, X, XTitle, XMin, XMax, Y, YTitle, YMin, YMax):
    elementPlot.clear()
    elementPlot.plot(x=X, y=Y, pen=None, symbol='o', symbolBrush='k', symbolSize=5)
    elementPlot.setLabels(left=YTitle, bottom=XTitle)
    elementPlot.setYRange(YMin, YMax)
    elementPlot.setXRange(XMin, XMax)

def plotGraph21(elementPlot, X, XMin, XMax, Y, YTitle, YMin, YMax, color, name=None):
    import pyqtgraph as pg
    elementPlot.clear()
    elementPlot.plot(x=X, y=Y, pen=pg.mkPen(color, width=3), name=name)
    elementPlot.setLabels(left=YTitle)
    elementPlot.setYRange(YMin, YMax)
    elementPlot.setXRange(XMin, XMax)

# Plot of multiple deviations vs timestamp
def plotGraph31(elementPlot, X, XMin, XMax, Y, YTitle, YMin, YMax, color, name):
    import pyqtgraph as pg
    elementPlot.plot(x=X, y=Y, pen=pg.mkPen(color, width=3), name=name)
    elementPlot.setLabels(left=YTitle)
    elementPlot.setYRange(YMin, YMax)
    elementPlot.setXRange(XMin, XMax)


