#!/bin/bash

cd "$(git rev-parse --show-toplevel)" || exit 1
cd .github/skills/repository-template
if ! [ -d "assets" ]; then
  git clone https://github.com/stefaniuk/repository-template.git assets
else
  cd assets
  git pull origin custom
fi
git checkout custom
