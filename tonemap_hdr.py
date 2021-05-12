import numpy as np
import hdrio
import os
import argparse

def tonemap_hdr(img):
    return np.clip(np.power(img,1/2.2), 0.0, 1.0)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='tonemap hdr images with gamma of 1/2.2 and clipping(0,1)')
    parser.add_argument('inputfolder', default="/gel/usr/heweb4/datasets/LavalIndoor/hdrInputs_reexposed", help="Folder containing the panoramas to process")
    parser.add_argument('outputfolder', default="/gel/usr/heweb4/datasets/LavalIndoor/ldrInputs_reexposed", help="Folder where to put the processed exr")
    args = parser.parse_args()

    files = os.listdir(args.inputfolder)
    for file in files:
        print(file)
        im = hdrio.imread(os.path.join(args.inputfolder, file))
        im = tonemap_hdr(im)
        hdrio.imwrite(im, os.path.join(args.outputfolder, file[:-4]+'.png'))