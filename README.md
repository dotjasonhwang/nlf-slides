# Overview

Streamlines and automates some of the ppt lyric making process.
Tributory alias: NLFSlides

The available processing versions are listed below:

## Textfile Instructions
### V1
[V1 Text file example](/data/input/v1_example.txt)

1. Any name is fine, must end in .txt
2. `#`: comments in the file that the script will not read
3. 1st block: title
4. 2nd block: author
5. 3rd + blocks: The contents of each slide should be split up with an empty line in between
	i. `!`: blank slide

### V2
[V2 Text file example](/data/input/v2_example.txt)

1. Any name is fine, must end in .txt
2. `#` = comments in the file that the script will not read
3. 1st block: title
4. 2nd block: author
5. 3rd block: song map of symbols
	i. `!` = blank slide
6. 4th + blocks are each section
	i. The section starts with `/{SectionName}`. For example, `/V1` or `/C`
	ii. The contents of each slide should be split up with an empty line in between
* Error will throw if a symbol in song map is not found in below blocks
* Error will throw if symbol not in song map is found in below blocks

### Setup
1. Create virtualenv
2. Activate virtualenv
3. `pip install -r requirements.txt`

### Script
1. Put all text files in data/input with format {TITLE}.txt
2. `source venv/bin/activate`
3. `bin/create_ppt`
4. Use the -u/--uppercase argument to make the entire output ppt uppercase 
5. Output will be at data/output

### TODO
- README templating
- Generic templating (dotfiles, format hooks, typehinting)
- tests :)
	- 1 integration test should be that v1 and v2 example files should result in same ppt object

### Misc Notes
- Pyinstaller?
	- Ran into this issue: https://github.com/pyinstaller/pyinstaller/issues/4893
- Set up pipwheel
	- https://stackoverflow.com/questions/26059111/build-a-wheel-egg-and-all-dependencies-for-a-python-project
- Template
	- template background warning https://www.google.com/search?q=warning+duplicate+name+xml+ppt&sxsrf=AJOqlzW83r54TTTUMHnN4Yg9dxtRMCCUYQ%3A1674190859617&source=hp&ei=CyDKY9eRIoqlqtsP6v2TaA&iflsig=AK50M_UAAAAAY8ouG0EVG2eu8mIbUTpOylPTIZ8q_5K3&ved=0ahUKEwiXw-H7rtX8AhWKkmoFHer-BA0Q4dUDCAo&uact=5&oq=warning+duplicate+name+xml+ppt&gs_lcp=Cgdnd3Mtd2l6EAMyBQghEKABUABYAGCnGWgBcAB4AIABfIgBfJIBAzAuMZgBAKABAqABAQ&sclient=gws-wiz
- Textbox is whole screen because of some issues. See if it is possible to make it not the whole screen. Maybe the script can output textboxes and in google sheet there is functionality to mass edit all slides' textboxes. Can't remember exactly but cause is something about some "runtime" loading step that google sheets does not do?
- For archival history sake:
```
TEMPLATE_FILENAME = "Template.pptx" # Unused
def get_template_blank_layout(self):
    template_ppt = Presentation(input_file_path(TEMPLATE_FILENAME))
    blank_layout = template_ppt.slide_layouts[0]
    return blank_layout
```
