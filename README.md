[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
![Issues](https://img.shields.io/github/issues/Galsenaicommunity/waxal-project)
![PR](https://img.shields.io/github/issues-pr/Galsenaicommunity/waxal-project)

# Waxal Project
State of the art study of Keyword Spotting models to leverage the [Waxal](https://k4all.org/project/keyword-spotting-with-african-languages/) dataset.

# Project Structure

We were inspired by the [Cookiecutter](https://drivendata.github.io/cookiecutter-data-science/) guidelines to organize this project as follows: 

```
.
├── Makefile                <- tasks
├── config.yml              <- config file in YAML, can be exported as env vars if needed
├── config-private.yml      <- config file with private config (password, api keys, etc.)
├── data
│   └── raw
│   ├── intermediate
│   ├── processed
│   ├── temp
├── results
│   ├── outputs
│   ├── models
├── documents
│   ├── docs
│   ├── images
│   └── references
├── notebooks               <- notebooks for explorations / prototyping
└── src                     <- all source code, internal org as needed
```
# Usage

Download the project data from [Zenodo](https://zenodo.org/record/4661645#.YoyyePfK4lQ) with the command:
```
wget https://zenodo.org/record/4661645/files/Keyword_spotting_dataset_v0.01_17042021.rar
```

Install a rar tool to extract the compressed archive:
```
sudo apt install unrar
```
> If you are not using Linux, download [Winrar](https://www.win-rar.com/) to extract the archive.

Extract the contents of the downloaded archive (RAR) to the `data/raw` folder:
```
unrar e Keyword_spotting_dataset_v0.01_17042021.rar data/raw
```

## Output
After running the [Data Exploration](notebooks/Data%20Analysis/data_exploration.ipynb) notebook, data for each language's audio will be stored in a specific folder in `data/intermediate` as follows:
```
data/intermediate
├── Diola
├── Mandingue
├── Poular
├── Soninké
├── Sérère
└── Wolof
```

# Acknowledgement
The waxal dataset collection has been funded by [Knowledge4All foundation](https://k4all.org/project/keyword-spotting-with-african-languages/).