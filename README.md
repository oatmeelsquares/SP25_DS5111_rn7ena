# DS 5111: Software and Automation Skills

Coursework for DS 5111: Software and Automation Skills in partial fulfillment of the UVA School of Data Science Master's in Data Science.

## Module 3: Automating initializing a VM

To initialize a new vm, please follow these steps:

**Access latest packages**

run `sudo apt update`

**Setup ssh key**

run `ssh-keygen -t ed25519 -C "youremail@domain.com"` and set a password if you want

Go to your settings in GitHub, and click `SSH and GPG Keys` in the toolbar

Click `New SSH key` and give it a title to match your machine

Paste your public key into the text box (to find your public key, type `cat id_ed25519.pub`* into your machine)

If you added your key successfully, you should see a message with your GitHub username after typing `ssh -T -i ed25519 git@github.com` in your `home/.ssh` directory:

```
ubuntu@ip-172-31-95-58:~/.ssh$ ssh -T -i id_ed25519 git@github.com
Hi oatmeelsquares! You've successfully authenticated, but GitHub does not provide shell access.
```

**Note*: If you renamed your private key to something other than `id_ed25519`, use that name instead.

**Clone this repo**

In the directory you want to clone the repo in, enter the command:
```
git clone git@github.com:oatmeelsquares/SP25_DS5111_rn7ena.git
```
Now, if you type `ls` you should see `SP_DS5111_rn7ena` in your chosen directory. 

**Other setup**

In `SP25_DS5111_rn7ena` as your working directory, run `scripts/init.sh` to install desired packages. This includes the headless crhome browser and tools for a python virtual environment.

To setup your virtual environemnt, run `make update` from the repository directory. This will cause a python virtual environment to be created with all of the packages listed in `requirements.txt` (currently only `pandas` and `lxml`.

Run `make ygainers.csv` to test that the chrome headless browser is working. You should see `ygainers.html` and `ygainers.csv` appear in your working directory after running this command. `ygainers.csv` should look the same as `example_data/ygainers.csv`, although the numbers will change every day.

At this point, you can run `tree --gitignore .` from the root of the repo and your output should look like this:

```
.
├── LICENSE
├── README.md
├── google-chrome-stable_current_amd64.deb
├── makefile
├── requirements.txt
├── setup
│   └── init.sh
├── ygainers.csv
└── ygainers.html
```
