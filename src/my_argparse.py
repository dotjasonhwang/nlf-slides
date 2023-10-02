import argparse

def get_args():
    parser = argparse.ArgumentParser(description='Create a lyrics ppt. Reads all files matching data/input/*txt and outputs ppts to data/output/<TITLE>.pptx, where <TITLE>. See more information about the input and output file formatting in the README')
    parser.add_argument('-u', '--uppercase', default=False, action=argparse.BooleanOptionalAction, help="This flag makes the lyrics all uppercase")
    parser.add_argument('-v', '--vertical_alignment', default="top", choices=["top, middle, bottom"], help="This flag makes the lyrics all uppercase")
    return parser.parse_args()
