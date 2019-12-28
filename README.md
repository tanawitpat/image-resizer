# Image Resizer

## Project Maintainer

- Tanawit Pattanaveerangkoon <<tanawit.pat@gmail.com>>

## Installation

### 1. Using Python

```bash
# 1. Clone the project
git clone https://github.com/tanawitpat/image-resizer.git
cd image-resizer

# 2. Create and activate a virtual environment
virtualenv env
source env/bin/activate

# 3. Install dependencies
make install

# 4. Run the service
make run
```

### 2. Using Docker

```bash
# 1. Clone the project
git clone https://github.com/tanawitpat/image-resizer.git
cd image-resizer

# 2. Run the service
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

