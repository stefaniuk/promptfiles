#!/bin/bash

cd "$(git rev-parse --show-toplevel)" || exit 1
git subtree pull \
  --prefix=.github/skills/repository-template/example \
  https://github.com/nhs-england-tools/repository-template.git \
  main --squash
