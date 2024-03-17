class Parser:
    COMMENT_NOTATION = "#"

    def _read_file_into_blocks_and_strip_trailing_whitespace(self, input_file):
        file_contents = ""
        with open(input_file, "r") as file:
            for line in file:
                if not line.startswith(Parser.COMMENT_NOTATION):
                    file_contents += line
        # Split file_contents into blocks and strip trailing whitespace from each block
        return [block.rstrip() for block in file_contents.split("\n\n")]

    def _get_title_and_authors(self, blocks):
        return blocks[0], blocks[1]

    def _get_lyric_blocks(self, blocks):
        return blocks[2:]

    def _parse_song_map(self, song_map_line):
        return song_map_line.split(" ")
    
    def parse(self, full_file_path, filename):
        raise NotImplementedError


class V1Parser(Parser):
    BLANK_SLIDE_NOTATION = "!"

    def parse(self, full_file_path, filename):
        print(f"Reading {filename}...")
        blocks = self._read_file_into_blocks_and_strip_trailing_whitespace(full_file_path)
        title, authors = self._get_title_and_authors(blocks)
        lyric_blocks = self._get_lyric_blocks(blocks)
        return title, authors, lyric_blocks
    
    def block_is_blank_slide(self, lyric_block):
        return lyric_block.startswith(V1Parser.BLANK_SLIDE_NOTATION)


class V2Parser(Parser):
    SECTION_PREFIX = '/'

    def parse(self, full_file_path, filename):
        print(f"Reading {filename}...")
        blocks = self._read_file_into_blocks_and_strip_trailing_whitespace(full_file_path)
        title, authors = self._get_title_and_authors(blocks)
        song_map = self._parse_song_map(blocks[2])
        section_and_lyric_blocks = blocks[3:]
        return title, authors, song_map, section_and_lyric_blocks
    
    def block_is_section_label(self, block):
        return block.startswith(V2Parser.SECTION_PREFIX)
    
    def retrieve_section(self, block):
        return block[1:]
