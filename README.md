# DS 5111: Software and Automation Skills

Coursework for DS 5111: Software and Automation Skills in partial fulfillment of the UVA School of Data Science Master's in Data Science.

## Lab 2: Automating initializing a VM

To initialize a new vm, please follow these steps:

### Access latest packages

run `sudo apt update`

### Setup ssh key

run `ssh-keygen -t ed25519 -C "youremail@domain.com"` and set a password if you want

Go to your settings in GitHub, and click `SSH and GPG Keys` in the toolbar

Click `New SSH key` and give it a title to match your machine

Paste your public key into the text box (to find your public key, type `cat id_ed25519.pub`* into your machine)

If you added your key successfully, you should see a message with your GitHub username after typing `ssh -T -i ed25519 git@github.com` in your `home/.ssh` directory:

```
ubuntu@my-computer:~/.ssh$ ssh -T -i id_ed25519 git@github.com
Hi oatmeelsquares! You've successfully authenticated, but GitHub does not provide shell access.
```

**Note*: If you renamed your private key to something other than `id_ed25519`, use that name instead.

### Clone this repo

In the directory you want to clone the repo in, enter the command:
```
git clone git@github.com:oatmeelsquares/SP25_DS5111_rn7ena.git
```
Now, if you type `ls` you should see `SP_DS5111_rn7ena` in your chosen directory. 

### Other setup

In `SP25_DS5111_rn7ena` as your working directory, run `scripts/init.sh` to install desired packages. This includes the headless chrome browser and tools for a python virtual environment.

To setup your virtual environment, run `make update` from the repository directory. This will cause a python virtual environment to be created with all of the packages listed in `requirements.txt` (currently only `pandas` and `lxml`).

Run `make ygainers.csv` to test that the chrome headless browser is working. You should see `ygainers.html` and `ygainers.csv` appear in your working directory. `ygainers.csv` should look the same as `example_data/ygainers.csv`, although the numbers will change every day.

At this point, you can run `tree --gitignore .` from the root of the repo and your output should look like this:

```
.
├── LICENSE
├── README.md
├── bin
│   └── normalize_csv.py
├── example_data
│   └── sample_ygainers.csv
├── makefile
├── pylintrc
├── requirements.txt
├── scripts
│   └── init.sh
├── tests
│   └── test_normalize_csv.py
├── wsjgainers.csv
├── wsjgainers.html
├── ygainers.csv
└── ygainers.html
```

## Lab 3: Writing csv normalizer

In this lab, I added the file `bin/normalize_csv.py`, a module that loads csv files and converts them into a standard format for processing gainers data.

Functions:
    - `read_gainers()` Given a path to a .csv file, returns a pandas DataFrame in standard format

If run directly with the path to a .csv file as an argument, this module will produce a normalized .csv with `_norm` appended to the filename.

## Lab 4: Testing and Linting

In this lab, I:
- added `pylint` and `pytest` to `requirements.txt
- wrote some preliminary tests for `normalize_csv.py` in `tests/test_normalize_csv.py`
- ensured that both .py files passed the linter with a good score*
- updated .gitignore to exclude the gainer files

*Note: I lost points on `normalize_csv.py` because I needed to refactor it, but I will save that for the Design Patterns lab. I also lost points on the imports for `test_normalize_csv.py`, but I feel like disabling those warnings will have too much possible unknown impact on future lints, so I chose to leave them.

## Lab 5: GitHub Actions

In this lab, I added `.github/workflows/validations.yml` and made a pull request. The action ran, but failed because it did not have access to the .csv files, so I removed them from the .gitignore, then the workflow ran successfully:

[![Feature Validation](https://github.com/oatmeelsquares/SP25_DS5111_rn7ena/actions/workflows/validations.yml/badge.svg)](https://github.com/oatmeelsquares/SP25_DS5111_rn7ena/actions/workflows/validations.yml)


