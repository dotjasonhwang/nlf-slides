from pptx import Presentation
from pathlib import Path
from my_argparse import get_args
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN

INPUT_FILENAME = "split_lyrics.txt"
BLANK_SLIDE_NOTATION = "#"

def data_folder_path():
    return Path(__file__).parent.parent.joinpath("data")


def input_file_path(input_filename):
    return f"{data_folder_path()}/input/{input_filename}"


def output_file_path():
    return f"{data_folder_path()}/output"


def layout(ppt):
    return ppt.slide_layouts[0]


def read_file_into_blocks(make_uppercase):
    with open(input_file_path(INPUT_FILENAME), "r") as file:
        text = file.read()
        if make_uppercase:
            text = text.upper()
        return text.split("\n\n")
    raise Exception


def create_title_slide(ppt, title, authors):
    title_slide = ppt.slides.add_slide(layout(ppt))
    create_textbox(ppt, title_slide, f"{title}\n{authors}")


def create_blank_slide(ppt):
    ppt.slides.add_slide(layout(ppt))


def create_lyric_slide(ppt, lyric_block):
    lyric_slide = ppt.slides.add_slide(layout(ppt))
    create_textbox(ppt, lyric_slide, lyric_block)


def create_textbox(ppt, slide, contents):
    txBox = slide.shapes.add_textbox(
        Inches(3), Inches(3), ppt.slide_width, ppt.slide_height)

    tf = txBox.text_frame
    p = tf.paragraphs[0]
    p.text = contents
    p.alignment = PP_ALIGN.CENTER
    p.font.name = "ARIAL"
    p.font.size = Pt(32)


def create_ppt(title, authors, lyric_blocks):
    ppt = Presentation()
    create_title_slide(ppt, title, authors)
    for lyric_block in lyric_blocks:
        if lyric_block == BLANK_SLIDE_NOTATION:
            create_blank_slide(ppt)
        else:
            create_lyric_slide(ppt, lyric_block)
    return ppt


def get_title_and_authors(blocks):
    return blocks[0], blocks[1]


def get_lyric_blocks(blocks):
    return blocks[2:]


def main():
    args = get_args()
    make_uppercase = args.uppercase
    blocks = read_file_into_blocks(make_uppercase)
    title, authors = get_title_and_authors(blocks)
    lyric_blocks = get_lyric_blocks(blocks)

    ppt = create_ppt(title, authors, lyric_blocks)
    ppt.save(f"{output_file_path()}/{title}.pptx")

if __name__ == "__main__":
    main()
