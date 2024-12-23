# TLDR

Daily log

##

- MacOS v14.7.1 Sonoma
- CrewAI was designed to work with Python 3.10<=,<3.13
  - https://github.com/crewaiinc/crewai?tab=readme-ov-file#1-installation
- `brew update`
- `brew install pyenv`
```sh
pyenv -v
pyenv global
pyenv versions
pyenv version
pyenv which python3
pyenv install 3.11
pyenv local 3.11
```

##  Add the following to the .zshrc (or .bashrc 😉)

NOTE: ~/.zprofile (for login shells) and ~/.zshrc (for interactive shells)

```sh -  in the .zshrc
export PYENV_ROOT="$HOME/.pyenv"
[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
```

```sh
exec "$SHELL"
```

```sh
python --version # -> should return 3.11
```

## Installing CrewAI

```sh
 python -m venv .venv
 source .venv/bin/activate
 touch requirements.txt
 echo "crewai==0.86.0" > requirements.txt
 pip install -r requirements.txt
```

## Example 1

```sh
touch examples/1.py
python example/1.py # AuthenticationError: OpenAIException - The api_key client option must be set either by passing api_key to the client or by setting the OPENAI_API_KEY environment variable
touch .env
echo "OPENAI_API_KEY=your_key_here" > .env
```

add the following packages to the requirements.txt...

```txt
agentops==0.3.21
python-dotenv==1.0.1
```

add the following to the examples/1.py...

```py - 
from dotenv import load_dotenv
load_dotenv()
import os
```

add the following to the .env...

```sh
echo "\nAGENTOPS_API_KEY=your_key_here" >> .env
```