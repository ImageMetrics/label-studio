python3.8 -m venv env
source env/bin/activate
python -m pip install label-studio
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
if bash ${SCRIPT_DIR}/../deploy/prebuild.sh; then
  docker build -t heartexlabs/label-studio ${SCRIPT_DIR}/..
fi
