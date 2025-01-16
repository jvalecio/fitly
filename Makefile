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

simul: $(VENV)
	$(BIN)/$(PY) -m tools.simulator.main_simulator

requirements:$(VENV)
	powershell $(BIN)/pip3.exe freeze > requirements.txt

test:$(VENV)
	$(BIN)/$(PY) -m pytest -rP -v


mdi_tester:$(VENV)
	$(BIN)/$(PY) -m tools.mdi_tester.mdi_simulator_main
# $(BIN)/$(PY) -m mypy src --explicit-package-bases

$(VENV)/Lib/site-packages: $(VENV)
	powershell $(BIN)/pip3.exe freeze > requirements.txt

cli:
	$(BIN)/$(PY) -m tools.cli.cli_main
#cli_ex:
#	$(BIN)/$(PY) -m tools.cli.cli_example

clean:
	powershell Remove-Item -Force -Recurse -Path $(VENV)