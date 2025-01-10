# DEBUG

## Install Ollama
- Don't install usign Jupyter Lab terminal (error, not explained). Use terminal of the server instead.
- Ollama est installé dans ```usr/local/lib/ollama```
- Help : https://github.com/ollama/ollama/blob/main/docs/linux.md#manual-install

## Ollama use
* When using certain models in ollama : might be because of outdated versions of ollama installed (do not support recent models)
```
ResponseError: llama runner process has terminated: signal: aborted 
```
HELP
* https://github.com/ollama/ollama/issues/8375
* It was on old ollama instance how was running and causing troubles.
