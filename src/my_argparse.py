import argparse

def get_args():
    parser = argparse.ArgumentParser(description='Create a lyrics ppt')
    parser.add_argument('-u', '--uppercase', default=True, action=argparse.BooleanOptionalAction)
    return parser.parse_args()