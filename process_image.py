
import cv2

def get_name(path):
    name = path.split('/')
    return name[len(name)-1].split('.')[0]

def get_name_with_ext(path):
    name = path.split('/')
    return name[len(name)-1]

def binarizar(image):
    """
    :param image: 2d numpu arrray
    :return: image binrizada
    """
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if image[i][j] > 0:
                image[i][j] = 255
    return image


def gray(path):
    """
    :param path: str with path image
    :return: 2d numpy array with image in grayscale
    """
    return cv2.imread(path, 0)


def rgb(path):
    """
    :param path: str with path image
    :return: 3 2d numpy array with image in rgb
    """
    return cv2.imread(path)

def resize(img, x, y):
    return cv2.resize(img,(y,x), interpolation = cv2.INTER_CUBIC)

def save(str_name, np_img):
    cv2.imwrite(str_name, np_img)


def view(name_img, image):
    """
    :param name_img: str image name to view in title window
    :param image: numpy array or string iwth image name
    :return: None
    """
    if type(image) != str:
        img = image
    else:
        img = cv2.imread(image)

    cv2.imshow(name_img, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()