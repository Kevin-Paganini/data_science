




# makes plots nice
def make_pretty(ax, title='', x_label='', y_label='', img=False, legend=False):
    ax.set_title(title, fontsize=20)
    ax.set_xlabel(x_label, fontsize=16)
    ax.set_ylabel(y_label, fontsize=16)
    if legend:
        ax.legend(loc='best', fontsize=16)
    if img:
        ax.axis('off')
    return ax