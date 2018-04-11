
import data
import process_image as pi
from metrics import IOU, Dice_Score

def mesure_segmentation(path_mask_cnn, path_mask_esp, extensao_cnn, extensao_eps, arquivo):

    lista_img = data.get_list_images(path_mask_cnn, extensao_cnn)

    resultado = open(arquivo, 'w')
    resultado.write(' Nome Imagem,IOU,Dice_Score\n')

    sum_dice_score = 0
    sum_IOU = 0

    for index, i in enumerate(lista_img):
        print('index = ', index, len(lista_img))

        mask_cnn = pi.gray(i)
        mask_esp = pi.resize(pi.gray(path_mask_esp+pi.get_name(i)+extensao_eps), mask_cnn.shape[0], mask_cnn.shape[1])

        iou = IOU(mask_cnn, mask_esp, 255)
        dice_score = Dice_Score(mask_cnn, mask_esp, 255)

        sum_dice_score += dice_score
        sum_IOU += iou

        resultado.write(' %s,%.2f,%.2f\n' %(pi.get_name(i), iou, dice_score))

        if index is (len(lista_img)-1):
            resultado.write(' TOTAL,%.2f,%.2f\n' % ( (sum_IOU)/(index+1), (sum_dice_score) / (index+1)))
            break

    resultado.close()


if __name__ == '__main__':
    mesure_segmentation(path_mask_cnn='/home/josue/Área de Trabalho/Images/r1_mask_cnn/',
                        path_mask_esp='/home/josue/Área de Trabalho/Images/r1_mask_esp/',
                        extensao_cnn='.png',
                        extensao_eps='-exp5.bmp',
                        arquivo='/home/josue/PycharmProjects/lib_evaluate_segm/files_csv/RIM-ONEv1.csv')
