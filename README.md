## Running the scripts

Running the scripts should be as easy as installing the requirements:
    pip install requirements.txt
Alternatively load the conda environment from the file:
    conda env create --name mlops --file=environments.yml
Followed by optionally running the following methods:
    python src/models/main.py train
    python src/models.main.py evaluate
    python src/models.main.py visualize

The model is saved in src/models/savedmodels and the visualizations in the reports/figures folder

##TODO LIST

- [x] Working mnist classifier (92% accuracy), train and evaluate methods in main
- [ ] Visualizations
- [x] Comments (predict_model)
- [x] Flake8, black, isort - pep8 compliant
- [x] Up-and-running git repo
- [x] DVC with personal google drive
- [ ] DVC with google cloud 
- [x] Docker local training
- [ ] Docker gcloud
- [ ] Hyperparameter config file (hydra)
- [x] Pytorch lightning
- [ ] Wandb logs 
- [x] Cookie-cutter
- [x] makefile update 
