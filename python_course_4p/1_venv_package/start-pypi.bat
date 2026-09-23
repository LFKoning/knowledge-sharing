:: To publish a package use:
:: uv publish --publish-url http://localhost:8080 --check-url http://localhost:8080/simple  -p "" -u ""

mkdir packages
uv venv --python=3.13 --clear
uv pip install pypiserver
uv run pypi-server run  -a . -P . -p 8080 ./packages