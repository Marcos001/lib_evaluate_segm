
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['legend.fontsize'] = 18
plt.rcParams.update({'font.size': 24})

def barchart(mean_dice_score, mean_iou):

    n_groups = 3 # algoritmos

    fig, ax = plt.subplots() #figsize=(16, 9)
    fig.set_size_inches(16,8)
    #fig.yaxis.set_ticks_position('left')

    index = np.arange(n_groups)
    print('index is ',index)
    bar_width = 0.22 #35

    opacity = 0.5
    error_config = {'ecolor': '0.3'}

    dice_score = plt.bar(index, mean_dice_score, bar_width,
                     alpha=opacity,
                     color='g',
                     #yerr=std_sob,
                     error_kw=error_config,
                     label='Dice Score ',
                     align='center')

    IOU = plt.bar(index + bar_width, mean_iou, bar_width,
                     alpha=opacity,
                     color='r',
                     #yerr=std_sen,
                     error_kw=error_config,
                     label=' IOU ')


    def autolabel(rects):
        """
        Attach a text label above each bar displaying its height
        """
        for rect in rects:
            height = rect.get_height()-5
            #ax.text(rect.get_x() + rect.get_width() / 2., 1.05 * height, #2.
            #        '%d' % int(height),
            #        ha='center', va='center')



    plt.xlabel(' Databases ')
    plt.ylabel(' Scores ')
    plt.title(' Targeting Evaluation ')
    plt.xticks(index + bar_width / 1, ('RIM-ONEv1', 'DRISHTI_GS', 'Mean'))
    plt.legend() #
    plt.grid(True)
    plt.tight_layout()

    autolabel(dice_score)
    autolabel(IOU)

    plt.show()
    plt.savefig('barchart.png')