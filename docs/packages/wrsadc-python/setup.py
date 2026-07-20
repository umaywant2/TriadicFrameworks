from setuptools import setup, find_packages

setup(
    name="wrsadc-python",
    version="0.1.0",
    description="Python-native WRSADC Core — a lightweight resonance-aware boundary layer for RTT-Inside systems.",
    author="TriadicFrameworks",
    license="MIT",
    url="https://github.com/umaywant2/TriadicFrameworks",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "Topic :: Scientific/Engineering :: Information Analysis"
    ],
    python_requires=">=3.8",
)
