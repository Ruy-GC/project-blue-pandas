#!/bin/bash

# kill tmux sessions
pkill -f tmux

# local repo update
cd /root/project-blue-pandas/
git fetch && git reset origin/main --hard
source python3-virtualenv/bin/activate
pip install -r requirements.txt

# new tmux session for deploy
tmux new -d -s portfolio_deploy 'flask run --host=0.0.0.0'

