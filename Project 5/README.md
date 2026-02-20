# 😊 Real-Time Emotion Detection

A real-time facial emotion recognition system built with **OpenCV** and a **deep learning model (Keras/TensorFlow)**. It detects faces from a webcam feed and classifies them into one of several emotion categories instantly.

---

## 📸 Demo

> Point your webcam at a face — the model detects it and overlays the predicted emotion label in real time.
![istockphoto-1496615445-612x612](https://github.com/user-attachments/assets/8a4a3701-a3b7-4fbe-8ee0-a979e97839a0)

---

## 🧠 How It Works

1. **Face Detection** — OpenCV's Haar Cascade classifier (`haarcascade_frontalface_default.xml`) identifies face regions from each video frame.
2. **Preprocessing** — Detected face ROIs are resized and normalized to match the model's expected input format.
3. **Emotion Classification** — The pre-trained Keras model (`emotion_model.hdf5`) predicts the emotion from the face crop.
4. **Overlay** — The predicted label is drawn on the live video frame in real time.

### Detected Emotions

| Label | Emotion |
|-------|---------|
| 0 | Angry |
| 1 | Disgust |
| 2 | Fear |
| 3 | Happy |
| 4 | Sad |
| 5 | Surprise |
| 6 | Neutral |

---

## 🗂️ Project Structure

```
├── emotion_detection.py               # Main script — webcam capture, detection & prediction
├── emotion_model.hdf5                 # Pre-trained Keras CNN model
├── haarcascade_frontalface_default.xml # OpenCV Haar Cascade for face detection
└── README.md
```

---

## ⚙️ Requirements

- Python 3.7+
- OpenCV
- TensorFlow / Keras
- NumPy

Install dependencies:

```bash
pip install opencv-python tensorflow numpy
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/emotion-detection.git
cd emotion-detection
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the detector

```bash
python emotion_detection.py
```

> Press **`q`** to quit the webcam window.

---

## 🏗️ Model Architecture

The emotion classifier (`emotion_model.hdf5`) is a Convolutional Neural Network (CNN) trained on grayscale face images (typically 48×48 pixels). It was trained on a standard facial expression dataset such as **FER-2013**.

The model pipeline:
- Input: Grayscale face crop → resized to 48×48
- CNN layers with ReLU activations + MaxPooling
- Fully connected layers with Dropout
- Output: Softmax over 7 emotion classes

---

## 📌 Notes

- Ensure your webcam is connected and accessible.
- Performance may vary based on lighting conditions and camera quality.
- The Haar Cascade works best with frontal, well-lit faces.

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🙏 Acknowledgements

- [OpenCV](https://opencv.org/) for the face detection cascade
- [FER-2013 Dataset](https://www.kaggle.com/datasets/msambare/fer2013) for model training data
- [Keras / TensorFlow](https://keras.io/) for the deep learning framework
