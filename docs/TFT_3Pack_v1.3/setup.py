from setuptools import setup, find_packages

setup(
    name="TFT_3Pack_v1.3",
    version="1.3.0",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'tft=nous.cli:main',
            'entft=entft.cli:main',
            'tops=tops.cli:main'
        ]
    },
    author="Nawder Loswin",
    description="Triadic Framework Toolkit: nous, entft, tops",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    install_requires=[
        "pyyaml", "cryptography", "numpy"
    ],
    python_requires='>=3.8',
)
