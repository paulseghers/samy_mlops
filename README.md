## Running the scripts

Running the scripts should be as easy as installing the requirements:  

    pip install requirements.txt  

Alternatively load the conda environment from the file:  

    conda env create --name mlops --file=environments.yml  

Followed by optionally running the following methods:  

    python src/models/main.py train   

    python src/models.main.py evaluate   


The model is saved in src/models/savedmodels

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
.
├── LICENSE
├── Makefile
├── README.md
├── basic.yaml
├── data
│   ├── external
│   ├── interim
│   ├── make_dataset.py
│   ├── mnist_loader.py
│   ├── processed
│   └── raw
│       ├── corruptmnist
│       │   ├── test.npz
│       │   ├── train_0.npz
│       │   ├── train_1.npz
│       │   ├── train_2.npz
│       │   ├── train_3.npz
│       │   └── train_4.npz
│       └── corruptmnist_v2
│           ├── train_5.npz
│           ├── train_6.npz
│           └── train_7.npz
├── data.dvc
├── datasets
│   └── MNIST
│       └── raw
│           ├── t10k-images-idx3-ubyte
│           ├── t10k-images-idx3-ubyte.gz
│           ├── t10k-labels-idx1-ubyte
│           ├── t10k-labels-idx1-ubyte.gz
│           ├── train-images-idx3-ubyte
│           ├── train-images-idx3-ubyte.gz
│           ├── train-labels-idx1-ubyte
│           └── train-labels-idx1-ubyte.gz
├── docs
│   ├── Makefile
│   ├── commands.rst
│   ├── conf.py
│   ├── getting-started.rst
│   ├── index.rst
│   └── make.bat
├── environments.yml
├── exercise_files
│   ├── config.yaml
│   ├── typing_exercise.py
│   ├── typing_exercise_solution.py
│   ├── vae_mnist_bugs.py
│   ├── vae_mnist_pytorch_profiler.py
│   └── vae_mnist_working.py
├── logs
│   ├── access_log.log
│   ├── config
│   │   └── 20220117125532782-startup.cfg
│   ├── model_log.log
│   ├── model_metrics.log
│   ├── ts_log.17-Jan.log.gz
│   ├── ts_log.log
│   ├── ts_metrics.17-Jan.log.gz
│   └── ts_metrics.log
├── model_store
│   └── deployable_model.pt
├── notebooks
├── predict.dockerfile
├── references
├── reports
│   └── figures
│       └── wandb.png
├── requirements.txt
├── setup.py
├── src
│   ├── __init__.py
│   ├── data
│   │   ├── __init__.py
│   │   ├── corruptmnist
│   │   │   ├── test
│   │   │   │   └── test.npz
│   │   │   └── train
│   │   │       ├── train_0.npz
│   │   │       ├── train_1.npz
│   │   │       ├── train_2.npz
│   │   │       ├── train_3.npz
│   │   │       ├── train_4.npz
│   │   │       └── train_merged.npz
│   │   ├── load_bz2_nlpdata.py
│   │   └── make_dataset.py
│   ├── data.dvc
│   ├── features
│   │   ├── __init__.py
│   │   └── build_features.py
│   ├── models
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── data.cpython-38.pyc
│   │   │   ├── lightningmodel.cpython-38.pyc
│   │   │   ├── model.cpython-38.pyc
│   │   │   ├── predict_model.cpython-38.pyc
│   │   │   └── train_model.cpython-38.pyc
│   │   ├── data.py
│   │   ├── lightningmodel.py
│   │   ├── main.py
│   │   ├── model.py
│   │   ├── predict_model.py
│   │   ├── savedmodels
│   │   │   ├── checkpoints
│   │   │   │   └── checkpoint.pth
│   │   │   └── trainedmodel.pt
│   │   ├── train_model.py
│   │   ├── trainer.py
│   │   └── visualize.py
│   ├── tests
│   │   ├── __init__.py
│   │   └── test_data.py
│   └── visualization
│       ├── __init__.py
│       └── visualize.py
├── test_environment.py
├── tox.ini
├── trainer.dockerfile
├── tree.txt
└── wandb
    ├── debug.log -> run-20220118_131734-1h55g57m/logs/debug.log


