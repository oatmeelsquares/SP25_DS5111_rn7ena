# DS 5111: Software and Automation Skills

Coursework for DS 5111: Software and Automation Skills in partial fulfillment of the UVA School of Data Science Master's in Data Science.

## Lab 2: Automating initializing a VM

To initialize a new Ubuntu vm, please follow these steps:

### Access latest packages

run 
```
sudo apt update; sudo apt upgrade
```

### Setup auto-shutdown

If you're like me and always leave your AWS EC2 instance open, save some costs by setting up auto-shutdown based on inactivity:

1. Navigate to `/etc/systemd/`
3. Use `sudo` and an editor of your choice to edit the file `logind.conf`
4. Uncomment the lines that look like this:
    ```
    IdleAction=hibernate
    IdleActionSec=120min
    ```
5. Replace `hibernate` with `poweroff`
6. Replace `120min` with `30min` or however long you want the machine to wait before powering off due to inactivity

### Setup ssh key

run 
```
ssh-keygen -t ed25519 -C "youremail@domain.com"
```
and set a password if you want

Go to your settings in GitHub, and click `SSH and GPG Keys` in the toolbar

Click `New SSH key` and give it a title to match your machine

Paste your public key into the text box. To find your public key, type 
```
cat ~/.ssh/id_ed25519.pub
```
into your machine's console

Click "Add SSH Key" to save the key

If you added your key successfully, then after typing 
```
ssh -T -i ed25519 git@github.com
```
you should see this message with your GitHub username: `Hi my_username! You've successfully authenticated, but GitHub does not provide shell access.`

**Note**: If you renamed your private key to something other than `id_ed25519`, use that name instead.

### Clone this repo

Enter the command:
```
cd; git clone git@github.com:oatmeelsquares/SP25_DS5111_rn7ena.git
```
Now, if you type `ls` you should see `SP25_DS5111_rn7ena` in your home directory. 

### Other setup

In `SP25_DS5111_rn7ena` as your working directory, run 
```
scripts/init.sh
```
 to install desired packages. This includes the headless chrome browser and tools for a python virtual environment.

To setup your virtual environment, run 
```
make update
```
 from the repository directory. This will cause a python virtual environment to be created with all of the packages listed in `requirements.txt`.

Run 
```
make gainer choice=yahoo
```
 to test that the chrome headless browser is working. `ygainersYYYYMMDD_HHMMSS.csv` should appear in the `data` directory. It should look the same as `example_data/sample_ygainers.csv`, although the numbers will be different.

At this point, you can run 
```
tree --gitignore .
```
 from the root of the repo and your output should look like this:

```
.
├── ERD.md
├── Final_Report.md
├── LICENSE
├── README.md
├── bin
│   ├── gainers
│   │   ├── abstractclasses.py
│   │   ├── base.py
│   │   ├── factory.py
│   │   ├── logger.py
│   │   ├── wsj.py
│   │   └── yahoo.py
│   └── normalize_csv.py.old
├── data
│   └── example_data
│       ├── sample_wsjgainers.csv
│       └── sample_ygainers.csv
├── figures
│   ├── ERD.png
│   ├── best_time_bar.png
│   ├── change_ratio_scatter.png
│   └── top_freq_bar.png
├── makefile
├── projects
│   └── gainers
│       ├── README.md
│       ├── analyses
│       ├── dbt_project.yml
│       ├── macros
│       ├── models
│       │   ├── best_time_bar.sql
│       │   ├── change_ratio_scatter.sql
│       │   ├── example
│       │   │   ├── ende.sql
│       │   │   ├── enfr.sql
│       │   │   ├── french.sql
│       │   │   ├── my_first_dbt_model.sql
│       │   │   ├── my_second_dbt_model.sql
│       │   │   └── schema.yml
│       │   ├── gainers.sql
│       │   ├── schema.yml
│       │   ├── symbol_stats.sql
│       │   ├── time_stats.sql
│       │   └── top_freq_hist.sql
│       ├── seeds
│       │   └── numbers.csv
│       ├── snapshots
│       └── tests
├── pylintrc
├── requirements.txt
├── scripts
│   ├── ERD.mermaidjs
│   ├── crontab_clone
│   ├── get_gainer.py
│   ├── init.sh
│   ├── process_data.py
│   └── profiles.yml
└── tests
    ├── fixtures.py
    ├── test_factory.py
    ├── test_normalize_csv.py.old
    └── version_tests.py
```

### Automatic data collection

Hooray! Now you're all ready to start collecting data. You can run 
```
make cron
```
 to setup your machine to collect gainers data from all sources (Yahoo and Wall Street Journal) three times every weekday (at 9:31am, 12:30pm and 4:01pm).

To check that your crontab was setup successfully, type 
```
crontab -l
```
You should see something like this at the bottom of the output:

```
31 09 * * 1-5 cd ~/SP25_DS5111_rn7ena/; make gainer choice=all
30 12 * * 1-5 cd ~/SP25_DS5111_rn7ena/; make gainer choice=all
01 16 * * 1-5 cd ~/SP25_DS5111_rn7ena/; make gainer choice=all
```

Once you have your data collected, you can upload it into snowflake or another system to build SQL tables and do data visualization and analysis!

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

## Lab 6: OOP Your Code

In lab 6, I refactored my code to conform to the factory design pattern. I updated the tree diagram above to reflect the new files.

## Lab 7: Collecting Data

In lab 7, I added a cron job with the following code:

```
31 09 * * 1-5 cd ~/SP25_DS5111_rn7ena/; make gainer choice=all
30 12 * * 1-5 cd ~/SP25_DS5111_rn7ena/; make gainer choice=all
01 16 * * 1-5 cd ~/SP25_DS5111_rn7ena/; make gainer choice=all
```

The purpose of this code was to automatically collect gainers data three times per day, every day for at least one week. I now have many timestamped files with gainers data from my two different sources, though I have added them to the gitignore.

## Lab 8: Database Design

In this lab, I created ERD.md and ERD.mermaidjs to describe the structure of my snowflake database that I will use to create my dashboard. See [ERD.md](./ERD.md) for more details.

## Labs 9-10: Snowflake

In these labs, I created my snowflake profile and a dbt project in this repo. I updated the tree above to match. I uploaded all of the collected data as seed to my snowflake instance.

## Final product

I wrote new dbt models for all intermediate and final tables discussed in [ERD.md](./ERD.md). The final write-up is available in [Final_Report.md](./Final_Report.md).
