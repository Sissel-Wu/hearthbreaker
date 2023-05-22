#!/usr/bin/zsh

workdir=$(dirname $0)
source ~/.zshrc
cd "$workdir"
conda activate hearthstone
python -m unittest discover -s tests -p "*_tests.py"
conda deactivate
