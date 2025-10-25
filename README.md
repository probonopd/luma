# Estardyn 1.3" OLED SH1116 Example

This project demonstrates the use of the Estardyn 1.3" OLED Module with SH1116 controller using the luma.oled library and emulator.

It allows you do develop for this module without requiring the actual hardware, allowing for fast iterations during development.

<img width="222" height="440" alt="image" src="https://github.com/user-attachments/assets/046b0252-ca9f-4dd1-b51d-6594f859a40f" />

## Requirements

- Python 3.x
- luma.oled
- luma.emulator
- Pillow

## Installation

```bash
# On FreeBSD need to run this first: sudo pkg install py311-game
pip install -r requirements.txt
```

## Running the Example

```bash
python main.py
```

This will open an emulator window displaying text on the OLED screen. Use left/right arrow keys to simulate rotary encoder turns, spacebar for button, 'C' for confirm, 'B' for back, and ESC to exit.
