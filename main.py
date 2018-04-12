
import data, os
import process_image as pi
from metrics import IOU, Dice_Score, index_recall
from plotting import barchart


def mesure_segmentation(path_mask_cnn, path_mask_esp, extensao_cnn, extensao_eps, arquivo):

    lista_img = data.get_list_images(path_mask_cnn, extensao_cnn)

    resultado = open(arquivo, 'w')
    resultado.write(' Nome Imagem,IOU,Dice_Score,Recall\n')

    sum_dice_score = 0
    sum_IOU = 0
    sum_recall = 0

    for index, i in enumerate(lista_img):
        print('index = ', index, len(lista_img))

        mask_cnn = pi.gray(i)
        mask_esp = pi.resize(pi.gray(path_mask_esp+pi.get_name(i)+extensao_eps), mask_cnn.shape[0], mask_cnn.shape[1])

        iou = IOU(mask_cnn, mask_esp, 255)
        dice_score = Dice_Score(mask_cnn, mask_esp, 255)
        recall = index_recall(mask_esp, mask_cnn)

        sum_dice_score += dice_score
        sum_IOU += iou
        sum_recall += recall

        resultado.write(' %s,%.2f,%.2f,%.2f\n' %(pi.get_name(i), iou, dice_score,recall))

        if index is (len(lista_img)-1):
            resultado.write(' TOTAL,%.2f,%.2f,%.2f\n' % ( (sum_IOU)/(index+1), (sum_dice_score) / (index+1), (sum_recall) / (index+1)))

    resultado.close()

def plot_graphics():
    file = open(os.getcwd()+'/files_csv/RIM-ONEv1.csv', 'r')
    iou_rim, dice_rim = file.read().split('TOTAL,')[1].split(',')
    print(iou_rim, 'and ', dice_rim)
    file.close()

    file = open(os.getcwd() + '/files_csv/DRISHTI_GS.csv', 'r')
    iou_dr, dice_dr = file.read().split('TOTAL,')[1].split(',')
    print(iou_dr, 'and ', dice_dr)

    iou_rim = float(iou_rim)
    iou_dr = float(iou_dr)
    dice_dr = float(dice_dr)
    dice_rim = float(dice_rim)

    file.close()
    all_dice = (dice_rim+dice_dr)/2
    all_iou = ((iou_rim+iou_dr)/2)
    MEAN_DICE = (dice_rim, dice_dr, all_dice)
    MEAN_IOU = (iou_rim,iou_dr, all_iou)

    barchart(MEAN_DICE, MEAN_IOU),


def caculate_IOU_DICE_SCORE():

    mesure_segmentation(path_mask_cnn='/home/josue/Área de Trabalho/Images/r1_mask_cnn/',
                        path_mask_esp='/home/josue/Área de Trabalho/Images/r1_mask_esp/',
                        extensao_cnn='.png',
                        extensao_eps='-exp5.bmp',
                        arquivo=os.getcwd()+'/files_csv/RIM-ONEv1.csv')

    mesure_segmentation(path_mask_cnn='/home/josue/Área de Trabalho/Images/dri_mask_cnn/',
                        path_mask_esp='/home/josue/Área de Trabalho/Images/dri_mask_esp/',
                        extensao_cnn='.png',
                        extensao_eps='_ODsegSoftmap.png',
                        arquivo=os.getcwd()+'/files_csv/DRISHTI_GS.csv')

if __name__ == '__main__':
    caculate_IOU_DICE_SCORE()
    #plot_graphics()

