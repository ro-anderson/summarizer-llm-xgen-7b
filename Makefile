.PHONY: install-libs install

install-libs:
	pip install torch
	pip install transformers
	pip install gradio
	pip install tiktoken
	pip install accelerate
	pip install -i https://test.pypi.org/simple/ bitsandbytes

create-env:
	python -m venv venv
	. venv/bin/activate && make install-libs

