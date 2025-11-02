# 🔥 Smart Flame Detector (Arduino + Machine Learning)

A **Smart IoT system** that detects the presence of fire using a **Flame Sensor**, **Arduino Uno**, and a **Machine Learning model** running in real-time on Python.  
If fire is detected, the **buzzer alerts**, and the system displays a live alert on-screen.

---

## 🌟 Features

✅ Real-time flame monitoring  
✅ ML-based classification (Fire / Safe)  
✅ Buzzer alert for immediate detection  
✅ Easy to calibrate and retrain  
✅ Works with real sensors or simulated data  

---

## 🧠 How It Works

1. The Arduino reads analog values from a **Flame Sensor**.
2. The readings are sent to Python through **Serial communication**.
3. A **trained Random Forest model** classifies readings:
   - 🔥 **Fire Detected** → Buzzer ON  
   - ✅ **Safe** → Buzzer OFF  
4. The system continuously updates readings and predictions in real-time.

---

## ⚙️ Hardware Components

| Component | Function |
|------------|-----------|
| Arduino UNO | Microcontroller |
| Flame Sensor | Detects IR light emitted by flames |
| Buzzer | Alerts when fire is detected |
| Breadboard + Jumper Wires | Circuit setup |
| USB Cable | Serial connection to PC |

---

### 🖥️ Requirements
- Python 3.10+
- PlatformIO (VS Code)
- Arduino Uno board drivers


