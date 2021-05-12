import numpy as np
import hdrio
import os

def reexpose_hdr(hdrim, percentile=90, max_mapping=0.8, alpha=None):
    """
    :param img:         HDR image
    :param percentile:
    :param max_mapping:
    :return:
    """
    r_percentile = np.percentile(hdrim, percentile)
    if alpha==None:
        alpha = max_mapping / (r_percentile + 1e-10)
    return alpha * hdrim, alpha

input_folder = '/gel/usr/heweb4/datasets/LavalIndoor/1942x971/'
output_folder = '/gel/usr/heweb4/datasets/LavalIndoor/1942x971_reexposed/'
files = os.listdir(input_folder)
for file in files:
    print(file)
    im = hdrio.imread(os.path.join(input_folder, file))
    im, _ = reexpose_hdr(im)
    hdrio.imwrite(im, os.path.join(output_folder, file))