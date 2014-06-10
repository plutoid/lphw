#!/bin/bash

#Mon Jun  9 21:00:17 PDT 2014

echo -n "Commit Message: ";read CI_MSG
git add ./*
git commit -m "$CI_MSG"
git push origin master
