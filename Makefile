PY = python3
VENV = venv
BIN=$(VENV)/bin

ifeq ($(OS), Windows_NT)
    BIN=$(VENV)/Scripts
    PY=python
endif

all: run

.PHONY: setup, run, simul, requirements, test, stest, mdi_tester,clean,cli
setup:
	git init
	$(PY) -m venv venv
	$(BIN)/pip3 install -r requirements.txt

run: $(VENV)
	$(BIN)/$(PY) -m core.core $(args)

requirements:$(VENV)
	powershell $(BIN)/pip3.exe freeze > requirements.txt

clean:
	powershell Remove-Item -Force -Recurse -Path $(VENV)