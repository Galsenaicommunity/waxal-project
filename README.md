[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
![Issues](https://img.shields.io/github/issues/Galsenaicommunity/waxal-project)
![PR](https://img.shields.io/github/issues-pr/Galsenaicommunity/waxal-project)

# Waxal Project
State of the art study of Keyword Spotting models to leverage the Waxal dataset

# Project Structure

Based on [Cookiecutter Structure](https://drivendata.github.io/cookiecutter-data-science/)

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

Extract the downloaded archive (RAR) and copy _the contents of the resulting folder_ to the `data/raw` folder:
```
cp data_17042021/* data/raw
```
> You' ll need a rar archive extractor like [Winrar](https://www.win-rar.com/) to extract the archive.

## Output
Data for each language's audio will be stored in a different folder in `data/intermediate`.
```
data/intermediate
├── Diola
├── Mandingue
├── Poular
├── Soninké
├── Sérère
└── Wolof
```