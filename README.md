# Examples for kts framework
This repo is made to let people new to `kts` learn its syntax and best practices. 
Detailed instructions for each example are below.
## Titanic
The example uses a commonly known Titanic dataset and shows basic features of the framework.
To download it to current folder run `$ kts example titanic`. 
The notebooks are implied to be run in the following order:
* FeatureEngineering.ipynb -- create a feature constructor, preview it and use standard library
* ModelingStart.ipynb -- make a feature set out of feature constructors, create a trackable model and validate it, examine feature importances
* ModelingFull.ipynb -- conduct more experiments, check local leaderboard
* Stacking.ipynb -- blend and stack three best single models
