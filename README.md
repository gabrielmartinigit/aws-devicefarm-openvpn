# Connecting VPN with OpenVPN on Device Farm

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

Follow these [instructions](https://docs.aws.amazon.com/devicefarm/latest/developerguide/getting-started.html). After creating your project, follow these instructions to run our sample test:

1. On step 1, **Choose application**, select **Test a web application**.
2. On step 2, **Configure your test**, select Appium Python and upload the **test_bundle.zip**.
3. On step 2, choose **Run your test in a custom environment** and copy and paste our **device-farm/demo-phases.yml** spec file.
