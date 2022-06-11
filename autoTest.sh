#!/bin/bash

echo "Projekt wird nun automatisiert getestet..."
echo "1/3: MyPy"

mypy .

echo "2/3: Flake8"

flake8 .

echo "3/3: PyTest"

pytest --cov=smartFME_Reciever --cov-report xml:cov.xml

echo "Alle Tests wurden ausgeführt!"
