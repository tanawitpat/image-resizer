# Image Resizer

## Project Maintainer

- Tanawit Pattanaveerangkoon <<tanawit.pat@gmail.com>>

## Installation

### 1. Using Python with virtual environment

```bash
# 1. Clone the project
git clone https://github.com/tanawitpat/image-resizer.git
cd image-resizer

# 2. Create and activate a virtual environment
virtualenv env
source env/bin/activate

# 3. Install dependencies
make install

# 4. Define TARGET_WIDTH and TARGET_HEIGHT (example: 600px)
export TARGET_WIDTH=600
export TARGET_HEIGHT=600

# 5. Run the service
make run
```

### 2. Using Docker

```bash
# 1. Clone the project
git clone https://github.com/tanawitpat/image-resizer.git
cd image-resizer

# 2. Define TARGET_WIDTH and TARGET_HEIGHT in .env

# 3. Run the service
make run_compose
```

Images in the input directory will be resized and saved to the output directory.

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
