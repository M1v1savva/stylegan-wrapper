import sys
import argparse
from dataset_tool import create_from_images
from train import wrapper_call
import os

import tensorflow as tf 
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)

def create_dataset(input, output):
    create_from_images(output, input, 1)

def train(config_path):
    os.system("cp %s current_config.json" % config_path)
    wrapper_call()

def fid(path1, path2):
    os.system('python -m pytorch_fid %s %s' % (path1, path2))

def exec_cmd(argv):
    prog = argv[0]
    parser = argparse.ArgumentParser(
        description = 'Minimalist wrapper for Conditional StyleGAN', 
        epilog = 'For more information run "python %s <command> -h"' % prog)   
    subparser = parser.add_subparsers(dest='command', help='wrapper functions')
    dataset = subparser.add_parser('create_dataset', help='create the dataset')
    dataset.add_argument('-i', '--input', help='path to input folder')
    dataset.add_argument('-o', '--output', help='path to output folder')
    
    train = subparser.add_parser('train', help='train the model')
    train.add_argument('config_path', help='path to config file')
    
    fid = subparser.add_parser('fid', help='calculate FID')
    fid.add_argument('path1', help='path to the first image directory')
    fid.add_argument('path2', help='path to the second image directory')
    
    args = parser.parse_args()
    func = globals()[args.command]
    del args.command
    func(**vars(args))

if __name__ == '__main__':
    exec_cmd(sys.argv)