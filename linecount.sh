#!/usr/bin/env bash

printf "TOTAL LINE COUNT:\n"
git ls-files | xargs wc -l
printf "\nCode Files Word Count:\n"
git ls-files | grep '.py\|.sh\|.html' | grep -v '.pyc' | xargs wc -l
