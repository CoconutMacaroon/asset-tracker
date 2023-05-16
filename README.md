# Asset Tracker

![GitHub](https://img.shields.io/github/license/coconutmacaroon/asset-tracker?style=for-the-badge) ![GitHub top language](https://img.shields.io/github/languages/top/coconutmacaroon/asset-tracker?style=for-the-badge)

This is a program that runs a web server that provides a web UI for tracking assets (such as stocks, ETFs, etc.).

Prior to running it, install the requirements:
```sh
$ python3 -m pip install --upgrade flask requests waitress
```
Then, create a copy of `defaultconfig.ini` and name the copy `config.ini` (on Linux, `cp defaultconfig.ini config.ini`). Then, make any changes needed to `config.ini`. _You should not change `defaultconfig.ini`_ - instead change the copy. The copy is also ignored by Git to reduce the risk of accidentally pushing API keys to GitHub.
To run it, launch `server.py`:
```sh
$ python3 server.py
```

## Contributing

PRs are welcome. This project uses the `black` code formatter, so please run `python3 -m black server.py` prior to contributing changes. Note that you may need to do `python3 -m pip install --upgrade black` if you don't already have it installed. Also, please use type hints for _all_ variables and constants. Thanks!