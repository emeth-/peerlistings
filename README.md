# Setup

- Install python 2.7.x
- Run `pip install -r requirements.txt`
- Run `python manage.py migrate`
- Download peercoin wallet, and use the example ppcoin.conf in this directory (changing username and password)
- Run `python manage.py runsever`
- Run `python blockchain_scanner.py`
- Open browser to `127.0.0.1:8000`