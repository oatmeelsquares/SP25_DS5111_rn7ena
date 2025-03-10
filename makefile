default:
	cat makefile

env:
	python3 -m venv env; . env/bin/activate; pip install --upgrade pip

update: env
	. env/bin/activate; pip install -r requirements.txt; sudo timedatectl set-timezone America/New_York

ygainers.html.old:
	sudo google-chrome-stable --headless --disable-gpu --dump-dom --no-sandbox --timeout=5000 'https://finance.yahoo.com/markets/stocks/gainers/?start=0&count=200' > ygainers.html

ygainers.csv.old: ygainers.html.old
	. env/bin/activate; python3 -c "import pandas as pd; raw = pd.read_html('ygainers.html', flavor = 'lxml'); raw[0].to_csv('ygainers.csv')"

wsjgainers.html.old:
	sudo google-chrome-stable --headless --disable-gpu --dump-dom --no-sandbox --timeout=5000 'https://www.wsj.com/market-data/stocks/us/movers' > wsjgainers.html

wsjgainers.csv.old: wsjgainers.html.old
	. env/bin/activate; python3 -c "import pandas as pd; raw = pd.read_html('wsjgainers.html', flavor = 'lxml'); raw[0].to_csv('wsjgainers.csv')"

gainer:
	.  env/bin/activate; python3 get_gainer.py $(choice); rm *gainers.html

clean:
	rm ygainers* wsjgainers*

lint:
	-. env/bin/activate; pylint bin/ tests/

test: lint
	. env/bin/activate; pytest -vv tests/


