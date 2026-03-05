# LTXV

## QUICK START (on macOS or Linux)

```shell
# Prepare your environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

```shell
# Set your API key
echo "LTXV_API_KEY=YOUR_API_KEY" > .env
```

```shell
# For text to video
python main.py -p INPUT_FILE
# For image to video
python main.py -p INPUT_FILE -i IMAGE_URI
```
