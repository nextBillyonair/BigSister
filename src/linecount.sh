#!/usr/bin/env bash

printf "TOTAL WORD COUNT:\n"
git ls-files | xargs wc -l
printf "\nCode Files Word Count:\n"
git ls-files | grep '.py\|.sh\|.md\|.txt\|.html\|LICENSE' | grep -v '.pyc' | xargs wc -l
