import argparse

def get_args(processor_versions):
    default_processor_version = processor_versions[-1]

    parser = argparse.ArgumentParser(
        description="""Create a lyrics ppt. Reads all files matching data/input/*txt and 
        outputs ppts to data/output/<TITLE>.pptx, where <TITLE>. See more information 
        about the input and output file formatting in the README""")
    parser.add_argument(
        '-v', '--version', default=default_processor_version, choices=processor_versions,
        type=int,
        help=f"""The processing version. Defaults to the latest version, which is {default_processor_version}""")
    parser.add_argument(
        '-u', '--uppercase', default=True, action=argparse.BooleanOptionalAction,
        help="Use this flag to make the lyrics uppercase. Otherwise, uses the capitalization in the raw file")
    parser.add_argument(
        '-a', '--vertical_alignment', default="top", choices=["top", "middle", "bottom"],
        help="The vertical alignment of the text")
    return parser.parse_args()
