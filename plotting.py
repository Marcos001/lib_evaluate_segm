
import matplotlib.pyplot as plt
import numpy as np
#plt.rcParams['legend.fontsize'] = 12
plt.rcParams.update({'font.size': 17})

def barchart(mean_dice_score, mean_iou, mean_recall):

    n_groups = 3 # algoritmos

    fig, ax = plt.subplots() #figsize=(16, 9)
    fig.set_size_inches(12,8)
    #fig.yaxis.set_ticks_position('left')

    index = np.arange(n_groups)
    bar_width = 0.20 #35

    opacity = 0.6
    error_config = {'ecolor': '0.3'}

    dice_score = plt.bar(index, mean_dice_score, bar_width,
                     alpha=opacity,
                     color='g',
                     error_kw=error_config,
                     label='Dice Score ',
                     align='center')

    IOU = plt.bar(index + bar_width, mean_iou, bar_width,
                     alpha=opacity,
                     color='r',
                     error_kw=error_config,
                     label=' IOU ')

    recall = plt.bar(index + (2*bar_width), mean_recall, bar_width,
                     alpha=opacity,
                     color='b',
                     error_kw=error_config,
                     label=' Recall ')

    def autolabel(rects, xpos='center'):
        """
        Attach a text label above each bar in *rects*, displaying its height.

        *xpos* indicates which side to place the text w.r.t. the center of
        the bar. It can be one of the following {'center', 'right', 'left'}.
        """

        xpos = xpos.lower()  # normalize the case of the parameter
        ha = {'center': 'center', 'right': 'left', 'left': 'right'}
        offset = {'center': 0.5, 'right': 0.57, 'left': 0.43}  # x_txt = x + w*off

        for rect in rects:
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width() * offset[xpos], 1.01 * height,
                    '{}'.format(height), ha=ha[xpos], va='bottom')




    #plt.xlabel(' Databases ')
    plt.ylabel(' Scores ')
    #plt.title(' Targeting Evaluation ')
    plt.xticks(index + bar_width / 1, ('RIM-ONEv1', 'DRISHTI_GS', ' Average ', " Recall "))
    plt.legend(loc=4) #
    plt.grid(True)
    plt.tight_layout()

    autolabel(dice_score)
    autolabel(IOU)
    autolabel(recall)

    plt.show()
    plt.savefig('barchart.png')