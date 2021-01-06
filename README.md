## Set up the Appium Python environment

1. We recommend setting up [Python's virtualenv](https://pypi.python.org/pypi/virtualenv) for developing and packaging tests so that unnecessary dependencies are not including in the bundled zip file.
2. Create your workspace and execute package_tests script:

``` 

    $ virtualenv workspace
    $ source workspace/bin/activate
    $ pip install pytest
    $ pip install Appium-Python-Client
    $ ./package_tests.sh

```

## Running tests on AWS Device Farm

Follow these [instructions](http://docs.aws.amazon.com/devicefarm/latest/developerguide/test-types-android-appium-python.html#test-types-android-appium-python-upload), upload **test_bundle.zip** on Step 9.
