from setuptools import setup
import os
import shutil

# Copy files from GISPython directory to geopythoncore (except __init__.py)
src = r'C:\TFS\GEOPython10-GIT\GEOPython10\GISPython'
dest = 'C:\TFS\GEOPython10-GIT\GEOPython10\geopythoncore\geopythoncore'
baseFileList = ['GISPythonModule.py', 'GISPythonTool.py', 'MailHelper.py', 'MyError.py', 'SimpleFileOps.py', 'SimpleFileOpsSafe.py', 'SysGISTools.py', 'SysGISToolsSysParams.py', 'TimerHelper.py', 'ZipHelper.py', 'GDBHelper.py']
for bf in baseFileList:
    srcFile = os.path.join(src, bf)
    if os.path.isfile(srcFile):
        shutil.copy(srcFile, dest)



setup(
	name = 'geopythoncore',
	version = '0.1.3', # version number according to PEP440 https://www.python.org/dev/peps/pep-0440/
	description = 'Additional tools for administering and automating different arcpy geoprocessing operations. Package is intended for use with ArcGIS 10.2.1 and later (has been tested on ArcGIS 10.4)', # short package description
	long_description = 'For readme see GitHub https://bitbucket.org/arturspd/geopythontest', # if needed (entire documentation)
	url = 'https://bitbucket.org/arturspd/geopythontest', # GitHub url
    # url = 'https://localhost:8081/simple', # private url
	author = 'LVM BSR', # author
    author_email = '', # email
    license = 'LICENSE.txt', # license

	# classifiers for PyPi: https://pypi.python.org/pypi?%3Aaction=list_classifiers
	classifiers=[
		# Project development status
		'Development Status :: 4 - Beta',
		# Intended audience and topic
		'Intended Audience :: Developers',
		'Topic :: Scientific/Engineering :: GIS',
		# License https://choosealicense.com/
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
		# Operating system
		'Operating System :: Microsoft :: Windows',

		# Specify the Python versions you support here.
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
	],

	keywords = ['ArcGIS', 'arcpy', 'automation'], # keywords (string or list of strings)
	packages = ["geopythoncore"], # packages to install
    include_package_data = True,
	install_requires = ['paramiko>=2.1.2', 'simplejson>=3.10.0'], # list of packages required in project (these will be installed by pip)

	# give entry points
	# first refactor code like this
	#def main():  # Entry point for scripts
	  ## Parse command line args 
	  ## Do a bunch of stuff
 
	# if __name__ == "__main__":
	#   main()

	entry_points = {'console_scripts': [
		'geopythoncore = __init__:main'
		]
	},
)