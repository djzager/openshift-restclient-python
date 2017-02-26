# Copyright 2016 The Kubernetes Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
To install the library, run the following

python setup.py install

prerequisite: setuptools
http://pypi.python.org/pypi/setuptools
"""

from setuptools import find_packages, setup
from openshift import __version__

# Do not edit these constants. They will be updated automatically
# by scripts/update-client.sh.
CLIENT_VERSION = __version__
PACKAGE_NAME = "openshift"
DEVELOPMENT_STATUS = "3 - Alpha"


def extract_requirements(filename):
    """
    Extracts requirements from a pip formatted requirements file.
    """
    with open(filename, 'r') as requirements_file:
        return [x.split()[0] for x in requirements_file.readlines()]


setup(
    name=PACKAGE_NAME,
    version=CLIENT_VERSION,
    description="OpenShift python client",
    author_email="",
    author="OpenShift",
    license="Apache License Version 2.0",
    url="https://github.com/ftl-toolbox/python-openshift",
    keywords=["Swagger", "OpenAPI", "Kubernetes", "OpenShift"],
    install_requires=extract_requirements('requirements.txt'),
    test_requires=extract_requirements('test-requirements.txt'),
    packages=find_packages(include='openshift.*'),
    include_package_data=True,
    long_description='Python client for OpenShift http://openshift.io/',
    classifiers=[
        "Development Status :: %s" % DEVELOPMENT_STATUS,
        "Topic :: Utilities",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
    ],
    entry_points={
        'console_scripts': ['openshift-ansible-gen = openshift.ansiblegen.cli:commandline']
    },
)