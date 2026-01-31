from setuptools import setup, find_packages

setup(
    name="weathersense",
    version="0.1.0",
    author="Yash Gaur",
    author_email="yashgaur98@gmail.com",
    description="Multi-Modal Weather & Road Surface Detection for Autonomous Driving",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yashgaur/weathersense",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "torch>=2.0.0",
        "torchvision>=0.15.0",
        "numpy>=1.24.0",
        "opencv-python>=4.8.0",
        "pandas>=2.0.0",
        "matplotlib>=3.7.0",
        "scikit-learn>=1.3.0",
        "jupyter>=1.0.0",
    ],
)
