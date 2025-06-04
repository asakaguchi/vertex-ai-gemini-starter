"""
Setup script for vertex-ai-gemini-starter
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="vertex-ai-gemini-starter",
    version="0.1.0",
    author="vertex-ai-gemini-starter contributors",
    description="Vertex AI Gemini API スターターキット",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/asakaguchi/vertex-ai-gemini-starter",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.9",
    install_requires=[
        "google-cloud-aiplatform>=1.38",
        "python-dotenv>=1.0.0",
        "rich>=13.0.0",
    ],
    extras_require={
        "dev": [
            "ipython",
            "pytest",
        ],
    },
    entry_points={
        "console_scripts": [
            "vertex-ai-chat=vertex_ai_gemini.chat:main",
            "vertex-ai-streaming=vertex_ai_gemini.streaming:streaming_chat",
            "vertex-ai-vision=vertex_ai_gemini.vision:main",
            "vertex-ai-models=vertex_ai_gemini.models:main",
        ],
    },
)