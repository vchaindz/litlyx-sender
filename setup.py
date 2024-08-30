from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="litlyx-sender",
    version="0.1.0",
    author="Dennis Zimmer",
    author_email="dennis@dzlabs.ch",
    description="A Python library for sending events to LitLyx",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vchaindz/litlyx-sender",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.6",
    install_requires=[
        "requests>=2.25.1",
    ],
)