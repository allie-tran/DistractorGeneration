
import setuptools

setuptools.setup(
    name="distractor", # Replace with your own username
    version="0.0.1",
    author="Allie Tran",
    author_email="ly.tran2@mail.dcu.ie",
    description="POS tagger for lifelog data",
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(exclude=["eval", "script", "embedding_to_torch.py", "preprocess.py", "inference.py", "train_single.py", "translate.py"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
