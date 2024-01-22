"""
collections, collection.abc are imported to fix a known Python 3.10 bug. for `from pptx import Presentation`
Identified by a friend.
https://stackoverflow.com/questions/69468128/fail-attributeerror-module-collections-has-no-attribute-container
"""
import collections
import collections.abc
from pptx import Presentation

from pptx.util import Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.dml.color import RGBColor

class PPTXUtil:
    def __init__(self) -> None:
        self.ppt = Presentation()

    FONT = "ARIAL"
    TITLE_FONT_SIZE = 60
    LYRICS_FONT_SIZE = 40
    ALIGNMENT_MAPPING = {
        "top": MSO_ANCHOR.TOP,
        "middle": MSO_ANCHOR.MIDDLE,
        "bottom": MSO_ANCHOR.BOTTOM,
    }
    def create_blank_layout(self):
        blank_layout = self.ppt.slide_layouts[6]
        fill = blank_layout.background.fill
        fill.solid()
        fill.fore_color.rgb = RGBColor(0, 0, 0)
        return blank_layout

    def add_title_slide(self, blank_layout, title, authors, config):
        title_slide = self.ppt.slides.add_slide(blank_layout)
        self.add_textbox(title_slide, f"{title}\n{authors}", PPTXUtil.TITLE_FONT_SIZE, config)

    def add_blank_slide(self, blank_layout):
        self.ppt.slides.add_slide(blank_layout)

    def add_lyric_slide(self, blank_layout, lyric_block, config):
        lyric_slide = self.ppt.slides.add_slide(blank_layout)
        self.add_textbox(lyric_slide, lyric_block, PPTXUtil.LYRICS_FONT_SIZE, config)

    def add_textbox(self, slide, contents, font_size, config):
        txBox = slide.shapes.add_textbox(
            0, 0, self.ppt.slide_width, self.ppt.slide_height)
        
        tf = txBox.text_frame
        tf.vertical_anchor = PPTXUtil.ALIGNMENT_MAPPING[config.vertical_alignment]

        p = tf.paragraphs[0]
        p.text = contents.upper() if config.uppercase else contents
        p.alignment = PP_ALIGN.CENTER

        font = p.font
        font.name = PPTXUtil.FONT
        font.size = Pt(font_size)
        font.color.rgb = RGBColor(255, 255, 255)
        font.bold = True

    def save(self, io_handler, title):
        print(f"Saving [{title}.pptx]...\n")
        self.ppt.save(f"{io_handler.output_file_path()}/{title}.pptx")