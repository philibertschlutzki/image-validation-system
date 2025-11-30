"""Setup-Skript für lokale Installation des Pakets."""

from setuptools import setup, find_packages

setup(
    name="image-validation-system",
    version="1.0.0",
    description="Konfigurierbare Bildinterpretation mit Validierung",
    author="philibertschlutzki",
    packages=find_packages(),
    install_requires=[
        "opencv-python-headless>=4.8.1",
        "Pillow>=10.1.0",
        "numpy>=1.26.2",
        "PyYAML>=6.0.1",
        "pytest>=7.4.3",
        "pytest-cov>=4.1.0",
    ],
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
