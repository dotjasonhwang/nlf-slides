<!--
MIT License

Copyright (c) 2025 Jason Hwang

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/github_username/nlf-slides">
    <img src="readme-assets/nlf-slides.png" alt="Logo" width="256" height="256" style="margin-bottom: 10px">
  </a>
  <h1 align="center">nlf-slides</h1>

  <p align="center">Song lyrics to PPT</p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about">About</a></li>
    <li><a href="#setup">Getting Started</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#built-with">Built With</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

## About

Streamlines and the ppt lyric process. From hours to minutes.

## Getting Started

1. Create virtualenv
2. Activate virtualenv
3. `pip install -r requirements.txt`

## Usage

### Script

1. Put all text files in data/input with format {TITLE}.txt
2. `source venv/bin/activate`
3. `bin/create_ppt`
4. Use the -u/--uppercase argument to make the entire output ppt uppercase
5. Output will be at data/output

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

-   Error will throw if a symbol in song map is not found in below blocks
-   Error will throw if symbol not in song map is found in below blocks

### TODO

-   README templating
-   Generic templating (dotfiles, format hooks, typehinting)
-   gpt tests :)
    -   1 integration test should be that v1 and v2 example files should result in same ppt object
-   Pyinstaller/wheels/nest

### Misc Notes

-   Pyinstaller?
    -   Ran into this issue: https://github.com/pyinstaller/pyinstaller/issues/4893
-   Set up pipwheel
    -   https://stackoverflow.com/questions/26059111/build-a-wheel-egg-and-all-dependencies-for-a-python-project
-   Template
    -   template background warning https://www.google.com/search?q=warning+duplicate+name+xml+ppt&sxsrf=AJOqlzW83r54TTTUMHnN4Yg9dxtRMCCUYQ%3A1674190859617&source=hp&ei=CyDKY9eRIoqlqtsP6v2TaA&iflsig=AK50M_UAAAAAY8ouG0EVG2eu8mIbUTpOylPTIZ8q_5K3&ved=0ahUKEwiXw-H7rtX8AhWKkmoFHer-BA0Q4dUDCAo&uact=5&oq=warning+duplicate+name+xml+ppt&gs_lcp=Cgdnd3Mtd2l6EAMyBQghEKABUABYAGCnGWgBcAB4AIABfIgBfJIBAzAuMZgBAKABAqABAQ&sclient=gws-wiz
-   Textbox is whole screen because of some issues. See if it is possible to make it not the whole screen. Maybe the script can output textboxes and in google sheet there is functionality to mass edit all slides' textboxes. Can't remember exactly but cause is something about some "runtime" loading step that google sheets does not do?
-   For archival history sake:

## Built With

[![Python][python-shield]][python-url]

## Contributing

Thank you for your interest in contributing to this project. Open source projects are a beautiful picture of collaboration and generosity. Please raise items for discussion using the links below, via a pull request, or by email.

[Request Feature][feature-request-url]<br>
[Report Bug][bug-report-url]

## License

[![License][license-shield]][license-url]

## Contact

contact_name<br>
[email_address](mailto:email_address)

## Acknowledgments

-   [othneildrew/Best-README-Template][readme-template-url]
    -   For the README template

<!-- MARKDOWN LINKS -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

<!-- repo -->

[feature-request-url]: https://github.com/github_username/nlf-slides/issues/new?labels=enhancement&template=feature-request---.md
[bug-report-url]: https://github.com/github_username/nlf-slides/issues/new?labels=bug&template=bug-report---.md

<!-- about -->

[product-screenshot]: readme-assets/screenshot.png

<!-- usage -->

[usage-screenshot]: readme-assets/screenshot.png

<!-- built_with -->

[python-shield]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[python-url]: https://python.org/
[react-shield]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[react-url]: https://reactjs.org/
[markdown-shield]: https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white
[markdown-url]: https://www.markdownguide.org/

<!-- license -->

[license-shield]: https://img.shields.io/github/license/github_username/nlf-slides.svg?style=for-the-badge
[license-url]: https://github.com/github_username/nlf-slides/blob/master/LICENSE.txt

<!-- acknowledgements -->

[readme-template-url]: https://github.com/othneildrew/Best-README-Template
