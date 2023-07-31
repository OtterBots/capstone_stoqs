# Known Issues

## FAIL: test_parameterplot_scatter (stoqs.tests.unit_tests.SummaryDataTestCase)

This fail log has the following error messages associated with it:

```
ERROR 2023-07-31 21:18:17,343 plotting.py _make_image():654 Could not plot the data
 Traceback (most recent call last):
   File "/srv/stoqs/utils/Viz/plotting.py", line 651, in _make_image
     fig.savefig(sectionPngFileFullPath, dpi=120, transparent=True)
   File "/usr/local/lib/python3.10/dist-packages/matplotlib/figure.py", line 3343, in savefig
     self.canvas.print_figure(fname, **kwargs)
   File "/usr/local/lib/python3.10/dist-packages/matplotlib/backend_bases.py", line 2366, in print_figure
     result = print_method(
   File "/usr/local/lib/python3.10/dist-packages/matplotlib/backend_bases.py", line 2232, in <lambda>
     print_method = functools.wraps(meth)(lambda *args, **kwargs: meth(
   File "/usr/local/lib/python3.10/dist-packages/matplotlib/backends/backend_agg.py", line 509, in print_png
     self._print_pil(filename_or_obj, "png", pil_kwargs, metadata)
   File "/usr/local/lib/python3.10/dist-packages/matplotlib/backends/backend_agg.py", line 458, in _print_pil
     mpl.image.imsave(
   File "/usr/local/lib/python3.10/dist-packages/matplotlib/image.py", line 1689, in imsave
     image.save(fname, **pil_kwargs)
   File "/usr/local/lib/python3.10/dist-packages/PIL/Image.py", line 2429, in save
     fp = builtins.open(filename, "w+b")
\FileNotFoundError: [Errno 2] No such file or directory: '/srv/stoqs/media/sections/4_None_dorado_TQ20UILE31.png'

ERROR 2023-07-31 21:18:19,834 plotting.py _make_image():654 Could not plot the data
Traceback (most recent call last):
   File "/srv/stoqs/utils/Viz/plotting.py", line 651, in _make_image
     fig.savefig(sectionPngFileFullPath, dpi=120, transparent=True)
   File "/usr/local/lib/python3.10/dist-packages/matplotlib/figure.py", line 3343, in savefig
     self.canvas.print_figure(fname, **kwargs)
   File "/usr/local/lib/python3.10/dist-packages/matplotlib/backend_bases.py", line 2366, in print_figure
     result = print_method(
   File "/usr/local/lib/python3.10/dist-packages/matplotlib/backend_bases.py", line 2232, in <lambda>
     print_method = functools.wraps(meth)(lambda *args, **kwargs: meth(
   File "/usr/local/lib/python3.10/dist-packages/matplotlib/backends/backend_agg.py", line 509, in print_png
     self._print_pil(filename_or_obj, "png", pil_kwargs, metadata)
   File "/usr/local/lib/python3.10/dist-packages/matplotlib/backends/backend_agg.py", line 458, in _print_pil
     mpl.image.imsave(
   File "/usr/local/lib/python3.10/dist-packages/matplotlib/image.py", line 1689, in imsave
     image.save(fname, **pil_kwargs)
   File "/usr/local/lib/python3.10/dist-packages/PIL/Image.py", line 2429, in save
     fp = builtins.open(filename, "w+b")
FileNotFoundError: [Errno 2] No such file or directory: '/srv/stoqs/media/sections/1_None_dorado_CK4KDP54IS.png'

ERROR 2023-07-31 21:18:27,586 plotting.py _make_image():654 Could not plot the data
Traceback (most recent call last):
   File "/srv/stoqs/utils/Viz/plotting.py", line 651, in _make_image
     fig.savefig(sectionPngFileFullPath, dpi=120, transparent=True)
   File "/usr/local/lib/python3.10/dist-packages/matplotlib/figure.py", line 3343, in savefig
     self.canvas.print_figure(fname, **kwargs)
   File "/usr/local/lib/python3.10/dist-packages/matplotlib/backend_bases.py", line 2366, in print_figure
     result = print_method(
   File "/usr/local/lib/python3.10/dist-packages/matplotlib/backend_bases.py", line 2232, in <lambda>
     print_method = functools.wraps(meth)(lambda *args, **kwargs: meth(
   File "/usr/local/lib/python3.10/dist-packages/matplotlib/backends/backend_agg.py", line 509, in print_png
     self._print_pil(filename_or_obj, "png", pil_kwargs, metadata)
   File "/usr/local/lib/python3.10/dist-packages/matplotlib/backends/backend_agg.py", line 458, in _print_pil
     mpl.image.imsave(
   File "/usr/local/lib/python3.10/dist-packages/matplotlib/image.py", line 1689, in imsave
     image.save(fname, **pil_kwargs)
   File "/usr/local/lib/python3.10/dist-packages/PIL/Image.py", line 2429, in save
     fp = builtins.open(filename, "w+b")
FileNotFoundError: [Errno 2] No such file or directory: '/srv/stoqs/media/sections/19_None_M1_Mooring_70H57BIVY0.png'
```

When .env the PRODUCTION=false then that means that the following code does not execute in the compose/local/stoqs/stoqs-start.sh:

```
if [ "$PRODUCTION" == "true" ]; then
   echo "Checking for presence of ${MEDIA_ROOT}/sections..."
   if [[ ! -e ${MEDIA_ROOT}/sections ]]; then
       echo "Creating directories for image generation and serving by nginx..."
       mkdir -p ${MEDIA_ROOT}/sections ${MEDIA_ROOT}/parameterparameter
       chmod 733 ${MEDIA_ROOT}/sections ${MEDIA_ROOT}/parameterparameter
   fi
fi
```

This means the sections folder is not created.  Although, there is also the issue of the images not being generated.

The exact cause to why the images are not being generated has not been solved.

## unit_tests.py: SummaryDataTestCase: test_sampledparameter_select Hangs.

It is unknown why this one particular test just hangs.  It was originally thought it might have been related to x3dom being down, but that may not be the case.

## Four tests that hang when x3dom is down or not responsive.

unit_tests.py: BaseAndMeasurementViewsTestCase: test_measuredparameter

unit_tests.py: SummaryDataTestCase: test_parameterparameterplot1

unit_tests.py: SummaryDataTestCase: test_parameterparameterplot2

unit_tests.py: SummaryDataTestCase: test_parameterparameterplot3

