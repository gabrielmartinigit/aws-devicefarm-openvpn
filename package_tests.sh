#!/bin/bash
## Copy tests
cp -r tests workspace/
cd workspace

## Verify tests
py.test --collect-only tests/
read -rsp $'\nMake sure desired capabilities is empty.\n\tVerify your tests were collected, press any key to continue or CTRL+C to abort.\n' -n1 key

## Write installed packages to requirements.txt
pip freeze >requirements.txt

## Build wheel archive
pip wheel --wheel-dir wheelhouse -r requirements.txt

## Remove cached files
find . -name '__pycache__' -type d -exec rm -r {} +
find . -name '*.pyc' -exec rm -f {} +
find . -name '*.pyo' -exec rm -f {} +
find . -name '*~' -exec rm -f {} +

## Zip tests/, wheelhouse/, and requirements.txt into test_bundle.zip
zip -r test_bundle.zip tests/ wheelhouse/ requirements.txt
