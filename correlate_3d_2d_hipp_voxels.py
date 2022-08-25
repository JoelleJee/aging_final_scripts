import os
import sys
import argparse
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def corr_num_voxels(struc, cest, roi, out):
    struc = pd.read_csv(struc)
    cest = pd.read_csv(cest)

    for rl in ["Left", "Right"]:
        struc_count = struc[rl + ' ' + roi + ' NZcount']
        cest_count = cest[rl + ' ' + roi + ' NZcount']

        # replace NAN as 0s
        struc_count = np.nan_to_num(struc_count)
        cest_count = np.nan_to_num(cest_count)

        # plot struc vs cest
        plt.scatter(struc_count, cest_count)

        for i in range(0, len(struc['Subject'])):
            plt.annotate(i, (struc_count[i], cest_count[i]))

        plt.xlabel('Whole Brain Atlas')
        plt.ylabel('CEST Atlas')
        plt.title(rl + ' ' + roi + ' Number of Voxels in Whole Brain vs CEST Atlas')
        plt.savefig(os.path.join(out,
                                 'Wholte_Brain_vs_CEST_Atlas_' + rl + '_' + roi + '_voxels.png'))
        plt.cla()

    return


def main():

    # Set up the argparser
    parser = argparse.ArgumentParser()
    required = parser.add_argument_group('required arguments')

    # Add the argument for the input directory
    required.add_argument(
        "-s", "--struc",
        help="Path to csv file with ROI values for whole brain",
        metavar="",
        required=True)

    # Add the argument for the input directory
    required.add_argument(
        "-c", "--cest",
        help="Path to csv file with ROI values for CEST slab",
        metavar="",
        required=True)

    # Add the argument for the input directory
    required.add_argument(
        "-r", "--roi",
        help="ROI label to corelated number of voxels in 3d vs 2d atlases",
        metavar="",
        required=True)

    # Add the argument for the input directory
    required.add_argument(
        "-o", "--outdir",
        help="directory to save the output to",
        metavar="",
        required=True)

    # Parse the arguments
    try:
        args = parser.parse_args()
    except:
        parser.print_help()
        sys.exit(1)

    corr_num_voxels(args.struc, args.cest, args.roi, args.outdir)

    return


if __name__ == '__main__':
    main()

