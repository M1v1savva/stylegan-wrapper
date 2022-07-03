import sys
import argparse

def create_dataset(input, output):
    print(input)
    print(output)

def train(path):
    print(path)

def fid(path1, path2):
    print(path1)
    print(path2)

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
    train.add_argument('path', help='path to config file')
    
    fid = subparser.add_parser('fid', help='calculate FID')
    fid.add_argument('path1', help='path to the first image directory')
    fid.add_argument('path2', help='path to the second image directory')
    
    args = parser.parse_args()
    func = globals()[args.command]
    del args.command
    func(**vars(args))

if __name__ == '__main__':
    exec_cmd(sys.argv)