# unemployment-report

## Setup


Create and activate a virtual environment:

```sh
conda create -n unemployment-env python=3.8

conda activate unemployment-env
```

## Usage

'Run an example script:

```sh
python app/my_script.py
```


Run the unemployment report:

```sh
python app/unemployment.py


ALPHAVANTAGE_API_KEY="abc123" python app/unemployment.py

```



## Configuration


[Obtain an API Key](https://www.alphavantage.co/support/#api-key) from AlphaVantage.

Then create a local ".env" file and provide the key like this:

```sh
# this is the ".env" file...

ALPHAVANTAGE_API_KEY="_________"
```

Install package dependencies:

```sh
pip install -r requirements.txt
```

