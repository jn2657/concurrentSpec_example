import sys
import os.path

HERE0 = os.path.dirname(__file__) or os.curdir
os.chdir(HERE0)
HERE = os.curdir
sys.path.insert(0, HERE)

from setuptools import setup, find_packages

# -----------------------------------------------------------------
# CONFIGURATIONS:
# -----------------------------------------------------------------
python_version = float("%s.%s" % sys.version_info[:2])
CONCURRENTSPEC = os.path.join(HERE, "src")
README = os.path.join(HERE, "README.md")
long_description = "".join(open(README).readlines())

# -----------------------------------------------------------------
# UTILITIES:
# -----------------------------------------------------------------
def find_packages_by_root_package(where):
    """
    Better than excluding everything that is not needed,
    collect only what is needed.
    """
    root_package = os.path.basename(where)
    packages = [ "%s.%s" % (root_package, sub_package)
                 for sub_package in find_packages(where)]
    packages.insert(0, root_package)
    return packages

setup(
    name = 'cSpec',
    version = '1.0.0.alpha',
    description = 'A behavior-driven development tool using Python',
    long_description=long_description,
    author = 'Kun-Che Li, Bing-Yun Wang, Che-Hung Tsai',
    author_email = 'milkkuan@gmail.com',
    url = 'https://github.com/benny870704/concurrentSpec_research',
    packages=find_packages_by_root_package(CONCURRENTSPEC),
    entry_points = {
        "console_scripts": [
            "cspec = src.main:main"
        ]
    }
)