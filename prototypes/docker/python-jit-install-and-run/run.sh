PIP_URL=$1
ARGS=${@:2}

pip install $PIP_URL
eval $ARGS
