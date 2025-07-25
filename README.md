# AIR-Ship: A Real-Time Anti-Interference Framework for Vision-Based Ship Detection in Dense Fog Environments

![License](https://img.shields.io/badge/license-MIT-blue)

## 🚢 Introduction
AIR-Ship is a lightweight and robust object detection framework designed for real-time ship detection in inland waterway environments under low-visibility conditions such as dense fog, backlight, and water surface reflections. The framework integrates:
- **Water Surface Image Dehazing (WSID)**: A novel image preprocessing module that enhances clarity in degraded images.
- **YOLOv10 with DS-SPPF**: An optimized detection backbone that incorporates the **Dilated Shared Spatial Pyramid Pooling Fast (DS-SPPF)** module for multi-scale feature extraction and robust detection.

This repository provides the source code, pre-trained models, and the **Inland Waterway Ship Dataset (IWSD)**, which includes 9,305 images captured under diverse weather and lighting conditions.

---

## 📜 Features
1. **Real-time Detection**:
   - Achieves **548 FPS** on standard hardware configurations.
   - Lightweight design with only **2.8M parameters**.
   
2. **Robustness in Low-Visibility Conditions**:
   - Enhanced detection accuracy through the WSID module.
   - Adaptive multi-scale feature fusion using DS-SPPF.

3. **Comprehensive Evaluation**:
   - Validated on **COCO**, **SeaShip**, and the newly constructed **IWSD** datasets.

---

## 📊 Dataset
### Inland Waterway Ship Dataset (IWSD)
- **Description**: A high-quality dataset consisting of 9,305 images captured from real-world inland waterways (e.g., Yangtze River, Wulong River in China).
- **Categories**: Includes nine common ship types (e.g., cargo ships, fishing boats, ferries, recreational boats).
- **Environmental Diversity**: Images captured under clear, foggy, rainy, and nighttime conditions.
- **Format**: COCO-style annotations.

You can download the IWSD dataset [here](https://github.com/Object-Detection-01/YOLO-DC).

---

## 🛠️ Installation
Follow the steps below to set up the AIR-Ship framework:

1. Clone this repository:
   ```bash
   git clone https://github.com/Object-Detection-01/YOLO-DC.git
   cd YOLO-DC
