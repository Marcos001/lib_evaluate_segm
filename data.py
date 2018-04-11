


def get_list_images(path, extensao):
    # implementar os dois tipos, glob e os.listdir
    from glob import glob
    return glob(path+'*'+extensao)

