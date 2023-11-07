## Instructions
### Textfile
1. Any name is fine, just needs to be *.txt
2. 1st block is title
3. 2nd block is author
4. Split each slide with an empty line between paragraphs
5. `!` = blank slides
6. `#` = comments in the file that the script will not read

### Setup
1. Create virtualenv
2. Activate virtualenv
3. `pip install -r requirements.txt`

### Script
1. `source venv/bin/activate`
2. `bin/create_ppt`
3. Use the -u/--uppercase argument to make the entire output ppt uppercase
4. Make sure input is in data/input and is a .txt file, name with title of song
5. Output will be at data/output

###
Textfile example:
```
#T
Graves Into Gardens

#A
Elevation Worship Feat Brandon Lake

#V1
I searched the world
But it couldn't fill me
Man's empty praise
And treasures that fade
Are never enough

Then You came along
And put me back together
And every desire
Is now satisfied
Here in Your love

#C
Oh, there's nothing better than You
There's nothing better than You
Lord, there's nothing
Nothing is better than You

#TURN
!
```


### TODO/Misc
- Pyinstaller?
	- Ran into this issue: https://github.com/pyinstaller/pyinstaller/issues/4893
- Set up pipwheel
	- https://stackoverflow.com/questions/26059111/build-a-wheel-egg-and-all-dependencies-for-a-python-project
- Template
	- template background warning https://www.google.com/search?q=warning+duplicate+name+xml+ppt&sxsrf=AJOqlzW83r54TTTUMHnN4Yg9dxtRMCCUYQ%3A1674190859617&source=hp&ei=CyDKY9eRIoqlqtsP6v2TaA&iflsig=AK50M_UAAAAAY8ouG0EVG2eu8mIbUTpOylPTIZ8q_5K3&ved=0ahUKEwiXw-H7rtX8AhWKkmoFHer-BA0Q4dUDCAo&uact=5&oq=warning+duplicate+name+xml+ppt&gs_lcp=Cgdnd3Mtd2l6EAMyBQghEKABUABYAGCnGWgBcAB4AIABfIgBfJIBAzAuMZgBAKABAqABAQ&sclient=gws-wiz
- Textbox is whole screen because of some issues. See if it is possible to make it not the whole screen. Maybe the script can output textboxes and in google sheet there is functionality to mass edit all slides' textboxes. Can't remember exactly but cause is something about some "runtime" loading step that google sheets does not do?
- Enhancement
	- from a split up file -> make ppt
	- validate a split up file (max num lines, max num chars)
	- read a non split file and split & ppt
- tests :) 
- Textfile
	- V2: aside from title & author, all other lyrics should be 1 chunk, script auto splits
	- V3: Script auto splits chunks that will be too long for slide (2 lines/4lines, etc)
