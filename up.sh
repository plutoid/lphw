#!/bin/bash

echo -n "Commit Message: ";read CI_MSG

git add ./*
git commit -m "$CI_MSG"
git push origin master
