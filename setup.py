from setuptools import find_packages, setup


with open("README.md", mode="r", encoding="utf-8") as readme_file:
    readme = readme_file.read()



setup(
    name="seateb",
    version="0.0.1",
    description="Southeast Asian Text Embedding Benchmark",
    long_description=readme,
    long_description_content_type="text/markdown",
    keywords="deep learning, text embeddings, benchmark",
    license="Apache",
    author="SEATEB",
    author_email="wuttikornp.pro@gmail.com",
    url="https://github.com/KornWtp/seateb",
    project_urls={
        "Huggingface Organization": "https://huggingface.co/kornwtp",
        "Source Code": "https://github.com/KornWtp/seateb",
    },
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "seateb=seateb.cmd:main",
        ]
    },
    python_requires=">=3.8.0",
    install_requires=[
        "datasets>=2.2.0",
        "jsonlines",
        "numpy",
        "requests>=2.26.0",
        "scikit_learn>=1.0.2",
        "scipy",
        "sentence_transformers>=2.2.0",
        "torch",
        "tqdm",
        "rich",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
)