
import data
import process_image as pi
from metrics import IOU, Dice_Score

def mesure_segmentation(path_mask_cnn, path_mask_esp, extensao_cnn, extensao_eps):

    lista_img = data.get_list_images(path_mask_cnn, extensao_cnn)

    for index, i in enumerate(lista_img):

        mask_cnn = pi.gray(i)
        mask_esp = pi.resize(pi.gray(path_mask_esp+pi.get_name(i)+extensao_eps), mask_cnn.shape[0], mask_cnn.shape[1])

        pi.view('CNN', mask_cnn)
        pi.view('Especialista', mask_esp)

        print(' IOU is [', IOU(mask_cnn, mask_esp, 255) ,' ] ')
        print(' Dice Score is [', Dice_Score(mask_cnn, mask_esp, 255), ' ] ')
        if index is 2:
            break



if __name__ == '__main__':
    mesure_segmentation(path_mask_cnn='/home/josue/Área de Trabalho/Images/r1_mask_cnn/',
                        path_mask_esp='/home/josue/Área de Trabalho/Images/r1_mask_esp/',
                        extensao_cnn='.png',
                        extensao_eps='-exp5.bmp')
