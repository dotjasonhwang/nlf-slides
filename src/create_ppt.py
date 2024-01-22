from src.my_argparse import get_args
from src.data.io_handler import IOHandler
from src.processor.processor import V1Processor, V2Processor

import os

def main():
    versions = {1: V1Processor(), 2: V2Processor()}
    args = get_args(list(versions.keys()))
    processor = versions[args.version]
    io_handler = IOHandler()

    print(f"""Starting NLFSlides...\n
    Using processor version: {args.version}
    Reading txt files from: {io_handler.input_folder_path()}
    Savings pptx files to: {io_handler.output_file_path()}\n""")

    for filename in os.listdir(io_handler.input_folder_path()):
        if filename.endswith("txt"):
            full_file_path = io_handler.input_folder_path() + os.fsdecode(filename)
            processor.process_lyrics_text_file(full_file_path, filename, args)

if __name__ == "__main__":
    main()
