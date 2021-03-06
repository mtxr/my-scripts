#!/bin/bash

# Coloured tail

shopt -s expand_aliases

alias grey-grep="GREP_COLOR='1;30' grep -E --color=always --line-buffered"
alias red-grep="GREP_COLOR='1;31' grep -E --color=always --line-buffered"
alias green-grep="GREP_COLOR='1;32' grep -E --color=always --line-buffered"
alias yellow-grep="GREP_COLOR='1;33' grep -E --color=always --line-buffered"
alias cyan-grep="GREP_COLOR='1;36' grep -E --color=always --line-buffered"
alias highlight-grep="GREP_COLOR='1;36' grep -E --color=always --line-buffered"

tail -f $@ | cyan-grep "INFO|$" | yellow-grep "DEBUG|$" | red-grep ".*ERR.*|$" | green-grep "\[[A-Z][0-9]+\]|$"
