
This repo is forked from https://github.com/hwchase17/chat-langchain

# How to use
1. Install dependencies: `pip install -r requirements.txt`
2. Register openai acount and create a OpenAI API Key  at https://platform.openai.com/account/api-keys
3. Add your OpenAI API Key in your enviroment
   - Add "OPENAI_API_KEY=<your-openai-aoi-key>" in '~/.bash_profile' file
   - Run command
```shell
$ source ~/.bash_profile
# Check 
$ echo $OPENAI_API_KEY
sk-....
```

4. Ingest book:
   - Add your book in `./data/` directory
   - Update book name in file `ingest.py` at `loader = UnstructuredPDFLoader("<book_name>")`
   - Run `ingest.sh` 
5. Run the app: `make start` or `python main.py`
```shell
$ make start
...
INFO:     Uvicorn running on http://127.0.0.1:9000 (Press CTRL+C to quit)
INFO:     Waiting for application startup.
INFO:     Application startup complete.
``` 

## ✅ Run application
1. Install dependencies: `pip install -r requirements.txt`
1. Run `ingest.sh` to ingest LangChain docs data into the vectorstore (only needs to be done once).
   1. You can use other [Document Loaders](https://langchain.readthedocs.io/en/latest/modules/document_loaders.html) to load your own data into the vectorstore.
1. Run the app: `make start`
   1. To enable tracing, make sure `langchain-server` is running locally and pass `tracing=True` to `get_chain` in `main.py`. You can find more documentation [here](https://langchain.readthedocs.io/en/latest/tracing.html).
1. Open [localhost:9000](http://localhost:9000) in your browser.