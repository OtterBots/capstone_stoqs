## Running all tests (test.sh)

Containers should already exist for local.yml but not running before following the below instructions.  Also, `.env` file at root, set `DEBUG=0`, set `TEST=0`.  This ensures no interuption from the debugpy.

1. Open the terminal and go to the capstone_stoqs/stoqs directory where the local.yml is located.  Run the following command to create the containers:
    ```
    docker-compose -f local.yml run --rm stoqs /bin/bash
    ```

2. After running the command, a bash shell will appear, and it will look similar to the following prompt:

    `root@601e658963ba:/srv#`

3. In the shell, enter the following command to set the `DATABASE_URL` environment variable:
    ``` bash
    export DATABASE_URL=postgis://stoqsadm:CHANGEME@stoqs-postgis:5432/stoqs
    ```

4. Next, set the `DATABASE_SUPERUSER_URL` environment variable by entering the following command:
    ``` bash
    export DATABASE_SUPERUSER_URL=postgis://postgres:changeme@stoqs-postgis:5432/stoqs
    ```

5. Now, you can run the `test.sh` script with the following command:
    ``` bash
    ./test.sh CHANGEME load noextraload
    ```
    
    The tests can takes over 5 minutes to complete.

6. When finished, stop containers.

7. Type `exit` in shell to exit.

## Results
```
Unit tests...
Found 40 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
unit_tests.py: BaseAndMeasurementViewsTestCase: test_activity: DONE
.unit_tests.py: BaseAndMeasurementViewsTestCase: test_activityType: DONE
.unit_tests.py: BaseAndMeasurementViewsTestCase: test_activity_parameter: DONE
.unit_tests.py: BaseAndMeasurementViewsTestCase: test_activity_resource: DONE
.unit_tests.py: BaseAndMeasurementViewsTestCase: test_analysis_method: DONE
.unit_tests.py: BaseAndMeasurementViewsTestCase: test_base_campaign: DONE
.unit_tests.py: BaseAndMeasurementViewsTestCase: test_campaign: DONE
.unit_tests.py: BaseAndMeasurementViewsTestCase: test_manage: DONE
.unit_tests.py: BaseAndMeasurementViewsTestCase: test_measuredparameter_with_parametervalues: DONE
.unit_tests.py: BaseAndMeasurementViewsTestCase: test_parameter: DONE
.unit_tests.py: BaseAndMeasurementViewsTestCase: test_parameter_resource: DONE
.unit_tests.py: BaseAndMeasurementViewsTestCase: test_platform: DONE
.unit_tests.py: BaseAndMeasurementViewsTestCase: test_platformType: DONE
.unit_tests.py: BaseAndMeasurementViewsTestCase: test_platform_resource: DONE
.unit_tests.py: BaseAndMeasurementViewsTestCase: test_query_summary: DONE
.unit_tests.py: BaseAndMeasurementViewsTestCase: test_query_ui: DONE
.unit_tests.py: BaseAndMeasurementViewsTestCase: test_resource: DONE
.unit_tests.py: BaseAndMeasurementViewsTestCase: test_resourceType: DONE
.unit_tests.py: BaseAndMeasurementViewsTestCase: test_sample: DONE
.unit_tests.py: BaseAndMeasurementViewsTestCase: test_sample_type: DONE
.unit_tests.py: BugsFoundTestCase: test_activity_has_attributes: DONE
.unit_tests.py: BugsFoundTestCase: test_lopc_data_load: DONE
.unit_tests.py: ParquetTestCase: test_include_activity_names: DONE
unit_tests.py: ParquetTestCase: test_include_activity_names: DONE
.unit_tests.py: ParquetTestCase: test_multiple_activitynames: DONE
.unit_tests.py: ParquetTestCase: test_parameter: DONE
.unit_tests.py: ParquetTestCase: test_platform: DONE
.unit_tests.py: ParquetTestCase: test_single_activitynames: DONE
.unit_tests.py: SummaryDataTestCase: test_empty: DONE
.unit_tests.py: SummaryDataTestCase: test_histograms: DONE
.unit_tests.py: SummaryDataTestCase: test_labeled: DONE
.unit_tests.py: SummaryDataTestCase: test_measuredparameter_select: DONE
.unit_tests.py: SummaryDataTestCase: test_parameterplot_scatter: DONE
.unit_tests.py: SummaryDataTestCase: test_parametervalue_min_max1: DONE
.unit_tests.py: SummaryDataTestCase: test_platform_animations: DONE
.unit_tests.py: SummaryDataTestCase: test_simpledepthtime_timeseries: DONE
.unit_tests.py: SummaryDataTestCase: test_simpledepthtime_timeseriesprofile1: DONE
.unit_tests.py: SummaryDataTestCase: test_simpledethtime_timeseriesprofile2: DONE
.unit_tests.py: SummaryDataTestCase: test_standardname_select: DONE
.unit_tests.py: SummaryDataTestCase: test_timedepth: DONE
.unit_tests.py: SummaryDataTestCase: test_timedepth2: DONE
.
----------------------------------------------------------------------
Ran 40 tests in 706.012s

OK
```

!!! Note 
    The above log was with 5 tests commented out (see Troubleshooting Problem #1).
## Other ways to run test.sh
`stoqs-start.sh` runs a database check and if it finds the postgis database not setup it will run `test.sh` (usualy on first dry run). Setting the `TEST` environmental variable in the `.env` file will force `start-stoqs.sh` to run `test.sh` regardless of databasecheck.py return code. 

There is a test database that will not be cleared automatically if running `test.sh` this way. For now it can be manually removed before starting the containers. Or we could add an `rm` line into the script if that is desired behavior 

## Troubleshooting

### **Problem #1**:
If running all 45 unit tests and it hangs during running test.sh, then it is possible x3dom.org is down or not working.  Or possibly a file path issue that has not been located.

**Solution**: If you still want to view the results for the other tests, comment out the four below tests in test.sh:

- test_measuredparameter()
- test_parameterparameterplot1()
- test_parameterparameterplot2()
- test_parameterparameterplot3()
- test_sampledparameter_select()

### **Problem #2**:
```stoqs.models.Parameter.DoesNotExist: Parameter matching query does not exist.```

**Solution**: Check stoqs DB and view the stoqs_parameter table.  Check if the name is in the data.  If it is not, then that is why the error happened.

Example:
```
stoqs            | ======================================================================
stoqs            | ERROR: test_sampledparameter_select (stoqs.tests.unit_tests.SummaryDataTestCase)
stoqs            | ----------------------------------------------------------------------
stoqs            | Traceback (most recent call last):
stoqs            |   File "/srv/stoqs/tests/unit_tests.py", line 341, in test_sampledparameter_select
stoqs            |     CAL1939_calanoida_id = Parameter.objects.get(name='CAL1939_calanoida').id
stoqs            |   File "/usr/local/lib/python3.10/dist-packages/django/db/models/manager.py", line 87, in manager_method
stoqs            |     return getattr(self.get_queryset(), name)(*args, **kwargs)
stoqs            |   File "/usr/local/lib/python3.10/dist-packages/django/db/models/query.py", line 637, in get
stoqs            |     raise self.model.DoesNotExist(
stoqs            | stoqs.models.Parameter.DoesNotExist: Parameter matching query does not exist.
```
{==In table stoqs_parameter, the name field did not have an entry for "CAL1939_calanoida".==}

### **Problem #3**:
```Got an error creating the test database: database "test_stoqs" already exists```

```Type 'yes' if you would like to try deleting the test database 'test_stoqs', or 'no' to cancel:```

**Solution**: Type `yes`.  Then the test will continue.
