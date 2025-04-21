# 🎨 **ASCII Art Generator - Turn Images into Awesome Text Art !**

*Welcome to the ASCII Art Generator, a cool tool that transforms images into pixel-perfect ASCII art using text characters ! Upload an image, and watch it turn into a stunning text-based masterpiece. Ready to get creative? Let’s get started !* ✨

## 🌟 How to Use the ASCII Art Generator

Follow these simple steps to create your own ASCII art:

1. **Clone the Repository**\
   Grab the code from GitHub:

   ```bash
   git clone https://github.com/yourusername/ASCII-Art-Generator.git
   cd ASCII-Art-Generator
   ```

2. **Set Up Your Environment**

   - Ensure you have Python 3.6+ installed.

3. **Install Dependencies**\
   Run this to get the required packages:

   ```bash
   pip install ascii_magic Pillow
   ```

4. **Prepare Your Image**

   - Place your image (e.g., `cod.png`) in the project folder.
   - Supported formats: PNG, JPG, etc. (via Pillow).

5. **Run the Script**\
   Execute the script with:

   ```bash
   python art.py
   ```

   - This converts `cod.png` into ASCII art and displays it in the terminal using `#` characters with 100 columns.
   - Check your terminal for the output!

**Pro Tip**: Use a clear, high-contrast image for the best results!

## 🛠️ Troubleshooting

Running into issues? Here’s how to fix common problems:

### 1. **Script Fails to Run**

- **Signs**: Error like “ModuleNotFoundError” or “No module named”.
- **Fix**:
  - Install dependencies: `pip install ascii_magic Pillow`.
  - Check Python version: Run `python --version` (needs 3.6+).
  - Ensure `art.py` and the image file are in the same folder.

### 2. **No Output or Garbled Text**

- **Signs**: Terminal shows nothing or weird characters.
- **Fix**:
  - Verify the image file name (e.g., `cod.png`) matches the script.
  - Adjust `columns` value in `art.py` (e.g., try 80 or 120).
  - Ensure your terminal supports ASCII rendering.

### 3. **Image Not Found**

- **Signs**: Error like “FileNotFoundError”.
- **Fix**:
  - Confirm `cod.png` exists in the folder.
  - Update the file path in `art.py` if needed (e.g., `from_image("path/to/cod.png")`).

### 4. **Installation Issues**

- **Signs**: `pip install` fails.
- **Fix**:
  - Update pip: `pip install --upgrade pip`.
  - Check internet connection for package downloads.

**Still Stuck?** Report issues on GitHub with the error message!

## 📋 Requirements

To run the ASCII Art Generator, you’ll need:

- **Python 3.6+**: The core language.
- **Dependencies**:
  - `ascii_magic`: For converting images to ASCII art (install via `pip install ascii_magic`).
  - `Pillow`: For image processing (install via `pip install Pillow`).
- **Image File**: Any image (e.g., `cod.png`) to convert.

## 💻 Virtual Environment Tips

Keep your setup clean with a virtual environment:

- **Create a Virtual Env**:

  ```bash
  python -m venv venv
  ```

- **Activate It**:

  - Windows: `venv\Scripts\activate`
  - Mac/Linux: `source venv/bin/activate`

- **Install Dependencies Inside**:

  ```bash
  pip install ascii_magic Pillow
  ```

- **Deactivate When Done**:

  ```bash
  deactivate
  ```

This isolates the project’s packages!

## ✨ What’s Awesome About ASCII Art Generator

- **Pixel Magic**: Turns any image into text art with `#` characters.
- **Customizable**: Adjust column width (e.g., 100) for different looks.
- **Simple & Fun**: Easy to use with stunning results in seconds.
- **Creative Freedom**: Works with any image you throw at it ! and works best at B/W images.

## 👨‍💻 Made By

Crafted with passion by B P ARYAAN \[ Aryaan-Dev \]. Built with love for art and coding enthusiasts !

## 🤝 Join the Fun

Love this tool? Enhance it ! Fork the repo, add features, or fix bugs. Share your ideas in the GitHub issues section.

---

**Built with ❤️ for creators and coders.** Start generating ASCII art today! 🎉
