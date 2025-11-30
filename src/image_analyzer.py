import cv2
import numpy as np
import yaml
from typing import Dict, Any
from PIL import Image

class ImageAnalyzer:
    """
    Führt Bildanalysen durch und extrahiert Werte für Validierung.
    """
    def __init__(self, config_path: str):
        with open(config_path, 'r') as file:
            self.config = yaml.safe_load(file)

    def analyze_image(self, image_path: str) -> Dict[str, Any]:
        img = cv2.imread(image_path)
        if img is None:
            raise ValueError(f"Ungültiges Bild: {image_path}")

        results = {}

        # Helligkeit
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        brightness = np.mean(gray)
        results['brightness'] = brightness

        # Schärfe (Laplacian-Varianz)
        lap_var = cv2.Laplacian(gray, cv2.CV_64F).var()
        results['sharpness'] = lap_var

        # Farbverteilung (Dominante Farbe via K-Means)
        img_pil = Image.open(image_path)
        img_small = img_pil.resize((64, 64))
        arr = np.array(img_small).reshape((-1, 3))
        n_colors = 3
        _, labels, centers = cv2.kmeans(arr.astype(np.float32), n_colors, None, (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 0.4), 10, cv2.KMEANS_RANDOM_CENTERS)
        _, counts = np.unique(labels, return_counts=True)
        dominant_color = centers[np.argmax(counts)] / 255
        results['dominant_color'] = dominant_color.tolist()
        results['dominant_color_ratio'] = max(counts) / len(arr)

        # Objekt-Erkennung kann mit Model nachgerüstet werden (Platzhalter)
        results['object_detection'] = [] # Erweiterbar mit TensorFlow/PyTorch

        return results
