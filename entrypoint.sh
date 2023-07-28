#!/usr/bin/env bash
flask db init
flask db upgrade
python run.py