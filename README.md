# Translator

## Running

```bash
docker run -d -p 8000:8000 ghcr.io/memodack/translator:latest
```

## Development

```bash
python3 -m venv .venv
```

```bash
. .venv/bin/activate
```

```bash
pip3 install -r requirements.txt
```

```bash
PYTHONDONTWRITEBYTECODE=1 fastapi dev main.py
```
