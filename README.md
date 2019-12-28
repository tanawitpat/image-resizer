# Image Resizer

## Project Maintainer

- Tanawit Pattanaveerangkoon <<tanawit.pat@gmail.com>>

## Installation

```bash
# 1. Clone the project
git clone https://github.com/tanawitpat/image-resizer.git

# 2. Create and activate a virtual environment
virtualenv env
source env/bin/activate

# 3. Install dependencies
make install
```

## Usage

```AsciiDoc
.
+-- _input
|   +-- image1.png
|   +-- image2.png
+-- _output
|   +-- image1.png
|   +-- image2.png
+-- app.py
+-- Makefile
+-- README.md
+-- requirements.txt
```

Run `make run` command. Images in the input directory will be resized and saved to the output directory.
