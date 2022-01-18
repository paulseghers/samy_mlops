## Running the scripts

Running the scripts should be as easy as installing the requirements:  

    pip install requirements.txt  

Alternatively load the conda environment from the file:  

    conda env create --name mlops --file=environments.yml  

Followed by optionally running the following methods, if you wish to retrain the model:  

    python src/models/main.py train   

    python src/models.main.py evaluate   


The model is saved in src/models/savedmodels

To run the docker containers, you can build from the following files:

    docker/trainer.dockerfile

    docker/predict.dockerfile

## LIST

- [x] Working mnist classifier (92% accuracy), train and evaluate methods in main
- [ ] Visualizations
- [x] Comments (predict_model)
- [x] Flake8, black, isort - pep8 compliant
- [x] Up-and-running git repo
- [x] DVC with personal google drive
- [x] DVC with google cloud 
- [x] Docker local training
- [x] Docker gcloud
- [x] Hyperparameter config file (hydra)
- [x] Pytorch lightning
- [x] Wandb  
- [x] Cookie-cutter
- [x] Makefile update 
- [ ] Torchserve local deployment
- [ ] Torchserve remote deployment

Wandb loss chart: ![Wandb loss chart](https://github.com/samytessier/samy_mlops/blob/master/reports/figures/wandb.png?raw=true)


. <br>
├── LICENSE <br>
├── Makefile <br>
├── README.md <br>
├── basic.yaml <br>
├── data <br>
│   ├── external <br>
│   ├── interim <br>
│   ├── make_dataset.py <br>
│   ├── mnist_loader.py <br>
│   ├── processed <br>
│   └── raw <br>
│       ├── corruptmnist <br>
│       │   ├── test.npz <br>
│       │   ├── train_0.npz <br>
│       │   ├── train_1.npz <br>
│       │   ├── train_2.npz <br>
│       │   ├── train_3.npz <br>
│       │   └── train_4.npz <br>
│       └── corruptmnist_v2 <br>
│           ├── train_5.npz <br>
│           ├── train_6.npz <br>
│           └── train_7.npz <br>
├── data.dvc <br>
├── datasets <br>
│   └── MNIST <br>
│       └── raw <br>
│           ├── t10k-images-idx3-ubyte <br>
│           ├── t10k-images-idx3-ubyte.gz <br>
│           ├── t10k-labels-idx1-ubyte <br>
│           ├── t10k-labels-idx1-ubyte.gz <br>
│           ├── train-images-idx3-ubyte <br>
│           ├── train-images-idx3-ubyte.gz <br>
│           ├── train-labels-idx1-ubyte <br>
│           └── train-labels-idx1-ubyte.gz <br>
├── docs <br>
│   ├── Makefile <br>
│   ├── commands.rst <br>
│   ├── conf.py <br>
│   ├── getting-started.rst <br>
│   ├── index.rst <br>
│   └── make.bat <br>
├── environments.yml <br>
├── exercise_files <br>
│   ├── config.yaml <br>
│   ├── typing_exercise.py <br>
│   ├── typing_exercise_solution.py <br>
│   ├── vae_mnist_bugs.py <br>
│   ├── vae_mnist_pytorch_profiler.py <br>
│   └── vae_mnist_working.py <br>
├── logs <br>
│   ├── access_log.log <br>
│   ├── config <br>
│   │   └── 20220117125532782-startup.cfg <br>
│   ├── model_log.log <br>
│   ├── model_metrics.log <br>
│   ├── ts_log.17-Jan.log.gz <br>
│   ├── ts_log.log <br>
│   ├── ts_metrics.17-Jan.log.gz <br>
│   └── ts_metrics.log <br>
├── model_store <br>
│   └── deployable_model.pt <br>
├── notebooks <br>
├── predict.dockerfile <br>
├── references <br>
├── reports <br>
│   └── figures <br>
│       └── wandb.png <br>
├── requirements.txt <br>
├── setup.py <br>
├── src <br>
│   ├── __init__.py <br>
│   ├── data <br>
│   │   ├── __init__.py <br>
│   │   ├── corruptmnist <br>
│   │   │   ├── test <br>
│   │   │   │   └── test.npz <br>
│   │   │   └── train <br>
│   │   │       ├── train_0.npz <br>
│   │   │       ├── train_1.npz <br>
│   │   │       ├── train_2.npz <br>
│   │   │       ├── train_3.npz <br>
│   │   │       ├── train_4.npz <br>
│   │   │       └── train_merged.npz <br>
│   │   ├── load_bz2_nlpdata.py <br>
│   │   └── make_dataset.py <br>
│   ├── data.dvc <br>
│   ├── features <br>
│   │   ├── __init__.py <br>
│   │   └── build_features.py <br>
│   ├── models <br>
│   │   ├── __init__.py <br>
│   │   ├── __pycache__ <br>
│   │   │   ├── data.cpython-38.pyc <br>
│   │   │   ├── lightningmodel.cpython-38.pyc <br>
│   │   │   ├── model.cpython-38.pyc <br>
│   │   │   ├── predict_model.cpython-38.pyc <br>
│   │   │   └── train_model.cpython-38.pyc <br>
│   │   ├── data.py <br>
│   │   ├── lightningmodel.py <br>
│   │   ├── main.py <br>
│   │   ├── model.py <br>
│   │   ├── predict_model.py <br>
│   │   ├── savedmodels <br>
│   │   │   ├── checkpoints <br>
│   │   │   │   └── checkpoint.pth <br>
│   │   │   └── trainedmodel.pt <br>
│   │   ├── train_model.py <br>
│   │   ├── trainer.py <br>
│   │   └── visualize.py <br>
│   ├── tests <br>
│   │   ├── __init__.py <br>
│   │   └── test_data.py <br>
│   └── visualization <br>
│       ├── __init__.py <br>
│       └── visualize.py <br>
├── test_environment.py <br>
├── tox.ini <br>
├── trainer.dockerfile <br>
├── tree.txt <br>
└── wandb <br>
    ├── debug.log -> run-20220118_131734-1h55g57m/logs/debug.log <br>
    
