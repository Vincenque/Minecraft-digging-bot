# Minecraft-digging-bot
I am trying to do minecraft digging bot only with computer vision. I am not accesing data from minecraft directly on purpose. This is work in progress

## Installation
Download newest version of python from https://www.python.org/downloads/

To install all necesary packages and libraries for python, open terminal (cmd) and paste those lines:

```
py -m ensurepip 
py -m pip install --upgrade pip 
py -m pip install pywin32 
py -m pip install keyboard 
py -m pip install pyautogui 
py -m pip install opencv-python 
py -m pip install -U Pillow 
py -m pip install matplotlib 
py -m pip install -U selenium 
py -m pip install webdriver-manager 
py -m pip install pypiwin32 
py -m pip install openpyxl 
py -m pip install --user xlsxwriter 
py -m pip install chromedriver-autoinstaller 
py -m pip install requests 
py -m pip install mss 
py -m pip install pytesseract 
```

Download and install Tesseract-OCR: https://github.com/UB-Mannheim/tesseract/wiki

Specific minecraft font is required: https://www.curseforge.com/minecraft/texture-packs/tech-rpg-font/download/4455712 Download it and put whole zip in "\AppData\Roaming.minecraft\resourcepacks".

Run minecraft with optifine in full sized window (not full screen) with screen resolution 1920x1080. Use downloaded resource pack and set interface size to 3.