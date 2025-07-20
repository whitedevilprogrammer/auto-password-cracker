# 📱 Android Unlock Brute Force (ADB Automation)

This Python script automates the process of sending unlock patterns or PIN codes to an Android device using **ADB (Android Debug Bridge)**. It simulates screen taps to try all possible 6-digit PIN combinations between `100000` and `999999`.

> ⚠️ **Note:** This script is for educational and authorized use only. Unauthorized access to devices is illegal.

---

## 🚀 How It Works

- Connects to an Android device via ADB.
- Iterates through all 6-digit PIN codes.
- For each digit in a PIN, sends a corresponding `input tap` command.
- Waits 1.5 seconds before trying the next combination.

---

## 📋 Requirements

- Python 3.x
- ADB installed and added to system PATH
- USB Debugging enabled on the Android device

---

## 📁 Files

- `auto_password_cracker.py`: Main automation script

---

## 🧠 Tap Coordinates Logic

The `asc` array contains predefined screen coordinates for each number (0-9) as if tapping a numeric keypad:

```python
asc = [
    'input tap 554 2221',  # 0
    'input tap 167 1782',  # 1
    'input tap 576 1804',  # 2
    'input tap 890 1804',  # 3
    'input tap 188 1927',  # 4
    'input tap 554 1927',  # 5
    'input tap 957 1927',  # 6
    'input tap 190 2121',  # 7
    'input tap 567 2121',  # 8
    'input tap 899 2121'   # 9
]
```

Each digit in the PIN is mapped to a tap using this list.

---

## ⚙️ Usage

1. Connect your Android device via USB
2. Enable USB debugging
3. Run the script:

```bash
python auto_password_cracker.py
```

---

## ⏱️ Timing

- 5-second initial delay (`time.sleep(5)`)
- 1.5-second delay between attempts (`time.sleep(1.5)`)

---

## 🔐 Disclaimer

This script should **only be used on your own devices** or for testing purposes with **explicit permission**. Unauthorized use is a violation of privacy laws.

---

## 🙋 Author

**Ellalan Haridoss**  
Full Stack Developer | ADB Automation Enthusiast  
📧 [ellalanharidoss@gmail.com](mailto:ellalanharidoss@gmail.com)
