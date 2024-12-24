# TLDR

Daily log

##

- MacOS v14.7.1 Sonoma
- CrewAI was designed to work with Python 3.10<=,<3.13
  - `https://github.com/crewaiinc/crewai?tab=readme-ov-file#1-installation`
- `brew update`
- `brew install pyenv`
  - `https://github.com/pyenv/pyenv?tab=readme-ov-file#switch-between-python-versions`
  - NOTE: "automatically select whenever you are in the current directory (or its subdirectories)"
  
  ```sh
  pyenv -v
  pyenv global
  pyenv versions
  pyenv version
  pyenv which python3
  pyenv install 3.11
  pyenv local 3.11
  ```

## Add the following to the .zshrc (or .bashrc 😉)

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
