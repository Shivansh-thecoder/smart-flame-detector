import serial
import joblib
import time

# Load trained model
print("Loading ML model...")
model = joblib.load("flame_model.pkl")
print("✅ Model loaded successfully.")

# Connect to Arduino
print("Connecting to Arduino...")
arduino = serial.Serial('COM5', 9600)
time.sleep(2)
print("✅ Connected to Arduino on COM5.")

print("\n🔥 Live Flame Detection Started... (Press Ctrl + C to stop)\n")

try:
    while True:
        line = arduino.readline().decode().strip()
        if line.startswith("FLAME:"):
            # Parse the numeric sensor value
            val = int(line.split(":")[1])

            # Predict using trained model
            pred = model.predict([[val]])[0]
            status = "🔥 Fire Detected!" if pred == 1 else "✅ No Fire"

            # Print prediction
            print(f"Sensor: {val} → Prediction: {status}")

            # Send buzzer control command to Arduino
            if pred == 1:
                arduino.write(b'1')  # Turn buzzer ON
            else:
                arduino.write(b'0')  # Turn buzzer OFF

except KeyboardInterrupt:
    print("\n🛑 Detection stopped by user.")
    arduino.close()
    print("🔌 Arduino connection closed.")
