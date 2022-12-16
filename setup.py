
from setuptools import setup, find_packages

from pathlib import Path

VERSION = '0.0.1'
DESCRIPTION = 'A data normalization package'

this_directory = Path(__file__).parent
LONG_DESCRIPTION = (this_directory / "DESCRIPTION.md").read_text()

# Setting up
setup(
    name="normcaler",
    version=VERSION,
    author="Shouke Wei",
    author_email="shouke.wei@deepsim.co>",
    license='MIT License',
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    url = ``,
    project_url = ``,
    Documentation = ``,
    packages=find_packages(),
    install_requires=['scikit-learn'],
    keywords=['python', 'normalization', 'decimal', 'scaler'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Data Scientists",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)