## Running all tests (test.sh)
Make sure you at are the capstone_stoqs/stoqs directory.  This is where the local.yml is.

In terminal, do the following steps.  This should create the containers.
1. ```docker-compose -f local.yml run --rm stoqs /bin/bash```
2. The bash shell should run and look similar to: ```root@601e658963ba:/srv#```
3. Enter into shell: ```export DATABASE_URL=postgis://stoqsadm:CHANGEME@stoqs-postgis:5432/stoqs```
4. Then enter: ```export DATABASE_SUPERUSER_URL=postgis://postgres:changeme@stoqs-postgis:5432/stoqs```
5. And then run test.sh with: ```./test.sh CHANGEME load noextraload```

You should see the following starting line:
```
Loading standard data for unit and functional tests...
```
The tests can take 5+ minutes to complete.

Type ```exit``` in shell to exit.

## Results
```
2023-07-21 16:02:43 Unit tests...
2023-07-21 16:02:44 Found 41 test(s).
2023-07-21 16:02:44 Creating test database for alias 'default'...
2023-07-21 16:02:49 System check identified no issues (0 silenced).
2023-07-21 16:03:05 unit_tests.py: BaseAndMeasurementViewsTestCase: test_activity: DONE
2023-07-21 16:03:06 unit_tests.py: BaseAndMeasurementViewsTestCase: test_activityType: DONE
2023-07-21 16:03:08 unit_tests.py: BaseAndMeasurementViewsTestCase: test_activity_parameter: DONE
2023-07-21 16:03:09 unit_tests.py: BaseAndMeasurementViewsTestCase: test_activity_resource: DONE
2023-07-21 16:03:11 unit_tests.py: BaseAndMeasurementViewsTestCase: test_analysis_method: DONE
2023-07-21 16:03:13 unit_tests.py: BaseAndMeasurementViewsTestCase: test_base_campaign: DONE
2023-07-21 16:03:14 unit_tests.py: BaseAndMeasurementViewsTestCase: test_campaign: DONE
2023-07-21 16:03:16 unit_tests.py: BaseAndMeasurementViewsTestCase: test_manage: DONE
2023-07-21 16:03:17 unit_tests.py: BaseAndMeasurementViewsTestCase: test_measuredparameter_with_parametervalues: DONE
2023-07-21 16:03:19 unit_tests.py: BaseAndMeasurementViewsTestCase: test_parameter: DONE
2023-07-21 16:03:20 unit_tests.py: BaseAndMeasurementViewsTestCase: test_parameter_resource: DONE
2023-07-21 16:03:22 unit_tests.py: BaseAndMeasurementViewsTestCase: test_platform: DONE
2023-07-21 16:03:23 unit_tests.py: BaseAndMeasurementViewsTestCase: test_platformType: DONE
2023-07-21 16:03:25 unit_tests.py: BaseAndMeasurementViewsTestCase: test_platform_resource: DONE
2023-07-21 16:03:26 unit_tests.py: BaseAndMeasurementViewsTestCase: test_query_summary: DONE
2023-07-21 16:03:28 unit_tests.py: BaseAndMeasurementViewsTestCase: test_query_ui: DONE
2023-07-21 16:03:30 unit_tests.py: BaseAndMeasurementViewsTestCase: test_resource: DONE
2023-07-21 16:03:31 unit_tests.py: BaseAndMeasurementViewsTestCase: test_resourceType: DONE
2023-07-21 16:03:33 unit_tests.py: BaseAndMeasurementViewsTestCase: test_sample: DONE
2023-07-21 16:03:34 unit_tests.py: BaseAndMeasurementViewsTestCase: test_sample_type: DONE
2023-07-21 16:03:39 unit_tests.py: BugsFoundTestCase: test_activity_has_attributes: DONE
2023-07-21 16:03:39 unit_tests.py: BugsFoundTestCase: test_lopc_data_load: DONE
2023-07-21 16:03:46 unit_tests.py: ParquetTestCase: test_include_activity_names: DONE
2023-07-21 16:03:46 unit_tests.py: ParquetTestCase: test_include_activity_names: DONE
2023-07-21 16:03:48 unit_tests.py: ParquetTestCase: test_multiple_activitynames: DONE
2023-07-21 16:03:49 unit_tests.py: ParquetTestCase: test_parameter: DONE
2023-07-21 16:03:51 unit_tests.py: ParquetTestCase: test_platform: DONE
2023-07-21 16:03:53 unit_tests.py: ParquetTestCase: test_single_activitynames: DONE
2023-07-21 16:03:58 starting... (test_empty)
2023-07-21 16:03:59 unit_tests.py: SummaryDataTestCase: test_empty: DONE
2023-07-21 16:03:59 starting... (test_histograms)
2023-07-21 16:04:01 unit_tests.py: SummaryDataTestCase: test_histograms: DONE
2023-07-21 16:04:01 starting... (test_labeled)
2023-07-21 16:04:03 unit_tests.py: SummaryDataTestCase: test_labeled: DONE
2023-07-21 16:04:03 starting... (test_measuredparameter_select)
2023-07-21 16:04:05 unit_tests.py: SummaryDataTestCase: test_measuredparameter_select: DONE
2023-07-21 16:04:05 starting... (test_parameterplot_scatter)
2023-07-21 16:04:07 unit_tests.py: SummaryDataTestCase: test_parameterplot_scatter: DONE
2023-07-21 16:04:07 starting... (test_parametervalue_min_max1)
2023-07-21 16:04:10 unit_tests.py: SummaryDataTestCase: test_parametervalue_min_max1: DONE
2023-07-21 16:04:10 starting... (test_platform_animations)
2023-07-21 16:04:12 unit_tests.py: SummaryDataTestCase: test_platform_animations: DONE
2023-07-21 16:04:12 starting... (test_sampledparameter_select)
2023-07-21 16:04:12 starting... (test_simpledepthtime_timeseries)
2023-07-21 16:04:15 unit_tests.py: SummaryDataTestCase: test_simpledepthtime_timeseries: DONE
2023-07-21 16:04:15 starting... (test_simpledepthtime_timeseriesprofile1)
2023-07-21 16:04:17 unit_tests.py: SummaryDataTestCase: test_simpledepthtime_timeseriesprofile1: DONE
2023-07-21 16:04:17 starting... (test_simpledepthtime_timeseriesprofile2)
2023-07-21 16:04:19 unit_tests.py: SummaryDataTestCase: test_simpledethtime_timeseriesprofile2: DONE
2023-07-21 16:04:19 starting... (test_standardname_select)
2023-07-21 16:04:21 unit_tests.py: SummaryDataTestCase: test_standardname_select: DONE
2023-07-21 16:04:21 starting... (test_timedepth)
2023-07-21 16:04:23 unit_tests.py: SummaryDataTestCase: test_timedepth: DONE
2023-07-21 16:04:23 starting... (test_timedepth2)
2023-07-21 16:04:25 unit_tests.py: SummaryDataTestCase: test_timedepth2: DONE
2023-07-21 16:04:25 ..................................E......
2023-07-21 16:04:25 ======================================================================
2023-07-21 16:04:25 ERROR: test_sampledparameter_select (stoqs.tests.unit_tests.SummaryDataTestCase)
2023-07-21 16:04:25 ----------------------------------------------------------------------
2023-07-21 16:04:25 Traceback (most recent call last):
2023-07-21 16:04:25   File "/srv/stoqs/tests/unit_tests.py", line 341, in test_sampledparameter_select
2023-07-21 16:04:25     CAL1939_calanoida_id = Parameter.objects.get(name='CAL1939_calanoida').id
2023-07-21 16:04:25   File "/usr/local/lib/python3.10/dist-packages/django/db/models/manager.py", line 87, in manager_method
2023-07-21 16:04:25     return getattr(self.get_queryset(), name)(*args, **kwargs)
2023-07-21 16:04:25   File "/usr/local/lib/python3.10/dist-packages/django/db/models/query.py", line 637, in get
2023-07-21 16:04:25     raise self.model.DoesNotExist(
2023-07-21 16:04:25 stoqs.models.Parameter.DoesNotExist: Parameter matching query does not exist.
2023-07-21 16:04:25 
2023-07-21 16:04:25 ----------------------------------------------------------------------
2023-07-21 16:04:25 Ran 41 tests in 96.352s
2023-07-21 16:04:25 
2023-07-21 16:04:25 FAILED (errors=1)
```


## Troubleshooting

### <strong>Problem #1</strong>:
If running all 45 unit tests and it hangs during running test.sh, then it is possible x3dom.org is down or not working.

<strong>Solution</strong>: If you still want to view the results for the other tests, comment out the four below tests in test.sh:
- test_measuredparameter()
- test_parameterparameterplot1()
- test_parameterparameterplot2()
- test_parameterparameterplot3()

### <strong>Problem #2</strong>:
Error: ```stoqs.models.Parameter.DoesNotExist: Parameter matching query does not exist.```

<strong>Solution</strong>: Check stoqs DB and view the stoqs_parameter table.  Check if the name is in the data.  If it is not, then that is why the error happened.

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
In table stoqs_parameter, the name field did not have an entry for "CAL1939_calanoida".
