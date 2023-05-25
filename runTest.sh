#!/usr/bin/zsh

workdir=$(dirname $0)
source ~/.zshrc
cd "$workdir"
conda activate hearthstone
timeout 60s python -m unittest discover -s tests -p "*_tests.py"
conda deactivate
