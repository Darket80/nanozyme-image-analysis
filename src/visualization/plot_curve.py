import matplotlib.pyplot as plt

def plot_activity_curve(
        x,
        y,
        y_fit,
        title,
        xlabel,
        ylabel,
        save_path,
        yerr=None):

    plt.figure()
    if yerr is not None:
        plt.errorbar(x, y, yerr=yerr,fmt='o',capsize=4,label='experimental')
    else:
        plt.scatter(x, y, label='experimental')

    plt.plot(
        x,
        y_fit,
        label="Linear fit"
    )

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.title(title)

    plt.legend()

    plt.savefig(save_path,dpi=300,bbox_inches='tight')
    plt.close()