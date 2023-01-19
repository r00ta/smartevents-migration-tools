# Migrations for Smartevents

Smartevents main repository [here](https://github.com/5733d9e2be6485d52ffa08870cabdee0/sandbox).

Make sure you have `python3` installed (at least `3.6`), `pip` and `virtualenv` as well.

Create a virtualenv

```bash
virtualenv venv
```

Activate the virtualenv

```bash
source venv/bin/activate
```

Install the required packages

```bash
pip install -r requirements.txt
```

## List of migrations

1. [MGDOBR-1415](https://issues.redhat.com/browse/MGDOBR-1415): Once you get the new TLS certificates, you have to patch all the existing secrets (for v1). Login into the target cluster and then run the [script](migrations/MGDOBR-1415.py) `python migrations/MGDOBR-1415.py`.
