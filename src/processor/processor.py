from src.data.io_handler import IOHandler
from src.parser.parser import V1Parser, V2Parser
from src.pptx.pptx_util import PPTXUtil

class V1Processor:
    def __init__(self) -> None:
        self.io_handler = IOHandler()
        self.parser = V1Parser()

    def create_ppt(self, title, authors, lyric_blocks, config):
        print(f"Making slides for [{title}] by [{authors}]...")
        ppt = PPTXUtil()
        blank_layout = ppt.create_blank_layout()
        ppt.add_title_slide(blank_layout, title, authors, config)
        for lyric_block in lyric_blocks:
            if self.parser.block_is_blank_slide(lyric_block):
                ppt.add_blank_slide(blank_layout)
            else:
                ppt.add_lyric_slide(blank_layout, lyric_block, config)
        return ppt

    def process_lyrics_text_file(self, full_file_path, filename, config):
        title, authors, lyric_blocks = self.parser.parse(full_file_path, filename)

        ppt = self.create_ppt(title, authors, lyric_blocks, config)
        
        ppt.save(self.io_handler, title)


class V2Processor:
    def __init__(self) -> None:
        self.io_handler = IOHandler()
        self.parser = V2Parser()

    def process_sections(self, song_map, section_and_lyric_blocks):        
        index = 0
        current_section = None
        lyric_blocks_by_section = {}

        lyric_blocks_by_section["!"] = [""] # The empty slide is a special section that is defined via the code, not via the textfile

        while(index < len(section_and_lyric_blocks)):
            block = section_and_lyric_blocks[index]
            if self.parser.block_is_section_label(block): # new starts
                section = self.parser.retrieve_section(block)
                if section not in song_map:
                    raise Exception(f"{section} is not in the song map. The song map is: {song_map}")
                elif section in lyric_blocks_by_section:
                    raise Exception(f"{section} is defined more than once. Please define each section only once")
                else:
                    current_section = section
                    lyric_blocks_by_section[current_section] = []
            else:
                lyric_blocks_by_section[current_section].append(block)
            index += 1

        unique_sections = set(song_map)
        sections_in_song_map_not_defined = unique_sections.difference(set(lyric_blocks_by_section))
        if sections_in_song_map_not_defined:
            raise Exception(f"{sections_in_song_map_not_defined}: were list in the song map but not defined")
        return lyric_blocks_by_section

    def create_ppt(self, title, authors, song_map, lyric_blocks_by_section, config):
        print(f"Making slides for [{title}] by [{authors}]...")
        ppt = PPTXUtil()
        blank_layout = ppt.create_blank_layout()
        ppt.add_title_slide(blank_layout, title, authors, config)
        for section in song_map:
            for lyric_block in lyric_blocks_by_section[section]:
                ppt.add_lyric_slide(blank_layout, lyric_block, config)
        return ppt

    def process_lyrics_text_file(self, full_file_path, filename, config):
        title, authors, song_map, section_and_lyric_blocks = self.parser.parse(full_file_path, filename)
        lyric_blocks_by_section = self.process_sections(song_map, section_and_lyric_blocks, config)
        
        ppt = self.create_ppt(title, authors, song_map, lyric_blocks_by_section, config)
        
        ppt.save(self.io_handler, title)
