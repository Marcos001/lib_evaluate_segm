
def Intersection(imagem_a, imagem_b, value):
    """
    :param imagem_a: predicted output map
    :param imagem_b: correct binary output map
    :return:
    """
    cont = 0
    for i in range(imagem_a.shape[0]):
        for j in range(imagem_b.shape[1]):
            if imagem_a[i][j] == value and imagem_b[i][j] == value:
                cont+=1
    return cont

def Union(imagem_a, imagem_b, value):
    """
    :param imagem_a:
    :param imagem_b:
    :param value:
    :return:
    """
    cont = 0
    for i in range(imagem_a.shape[0]):
        for j in range(imagem_b.shape[1]):
            if imagem_a[i][j] == value or imagem_b[i][j] == value:
                cont+=1
    return cont


def Sum(imagem_a, imagem_b, value):
    cont = 0
    for i in range(imagem_a.shape[0]):
        for j in range(imagem_b.shape[1]):
            if imagem_a[i][j] == value:
                cont+=1
            if imagem_b[i][j] == value:
                cont += 1
    return cont


def IOU(imagem_a, imagem_b, value):
    return ( Intersection( imagem_a, imagem_b, value ) / Union( imagem_a, imagem_b, value ))


def Dice_Score(imagem_a, imagem_b, value):
    return (2 * Intersection(imagem_a, imagem_b, value) / Sum(imagem_a, imagem_b, value))