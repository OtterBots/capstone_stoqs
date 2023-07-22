## Running all tests (test.sh)

1. Open the terminal and go to the capstone_stoqs/stoqs directory where the local.yml is located.  Run the following command to create the containers:
    ```
    docker-compose -f local.yml run --rm stoqs /bin/bash
    ```

2. After running the command, a bash shell will appear, and it will look similar to the following prompt:
    ```
    root@601e658963ba:/srv#
    ```

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
    
    - You should see the following starting line:
        - `Loading standard data for unit and functional tests...`
        - The tests can take 5+ minutes to complete.

Type `exit` in shell to exit.

## Results
```
Unit tests...
Found 41 test(s).
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
.Eunit_tests.py: SummaryDataTestCase: test_measuredparameter_select: DONE
.unit_tests.py: SummaryDataTestCase: test_parameterplot_scatter: DONE
.unit_tests.py: SummaryDataTestCase: test_parametervalue_min_max1: DONE
.unit_tests.py: SummaryDataTestCase: test_platform_animations: DONE
.Eunit_tests.py: SummaryDataTestCase: test_simpledepthtime_timeseries: DONE
.unit_tests.py: SummaryDataTestCase: test_simpledepthtime_timeseriesprofile1: DONE
.unit_tests.py: SummaryDataTestCase: test_simpledethtime_timeseriesprofile2: DONE
.unit_tests.py: SummaryDataTestCase: test_standardname_select: DONE
.unit_tests.py: SummaryDataTestCase: test_timedepth: DONE
.unit_tests.py: SummaryDataTestCase: test_timedepth2: DONE
.
======================================================================
ERROR: test_labeled (stoqs.tests.unit_tests.SummaryDataTestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/srv/stoqs/tests/unit_tests.py", line 528, in test_labeled
    diatom_id = Resource.objects.get(name='label', value='diatom').id
  File "/usr/local/lib/python3.10/dist-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/usr/local/lib/python3.10/dist-packages/django/db/models/query.py", line 637, in get
    raise self.model.DoesNotExist(
stoqs.models.Resource.DoesNotExist: Resource matching query does not exist.

======================================================================
ERROR: test_sampledparameter_select (stoqs.tests.unit_tests.SummaryDataTestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/srv/stoqs/tests/unit_tests.py", line 336, in test_sampledparameter_select
    CAL1939_calanoida_id = Parameter.objects.get(name='CAL1939_calanoida').id
  File "/usr/local/lib/python3.10/dist-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/usr/local/lib/python3.10/dist-packages/django/db/models/query.py", line 637, in get
    raise self.model.DoesNotExist(
stoqs.models.Parameter.DoesNotExist: Parameter matching query does not exist.

----------------------------------------------------------------------
Ran 41 tests in 295.935s

FAILED (errors=2)
```

!!! Note 
    The above log was with 4 tests commented out (see Troubleshooting Problem #1) since x3dom has been causing hanging issues.

## Troubleshooting

### **Problem #1**:
If running all 45 unit tests and it hangs during running test.sh, then it is possible x3dom.org is down or not working.

**Solution**: If you still want to view the results for the other tests, comment out the four below tests in test.sh:
- test_measuredparameter()
- test_parameterparameterplot1()
- test_parameterparameterplot2()
- test_parameterparameterplot3()

### **Problem #2**:
Error: ```stoqs.models.Parameter.DoesNotExist: Parameter matching query does not exist.```

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
