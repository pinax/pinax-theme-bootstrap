from setuptools import setup, find_packages


setup(
    name = "pinax-bootstrap-theme",
    version = "0.1",
    author = "James Tauber",
    author_email = "jtauber@jtauber.com",
    description = "a theme for Pinax",
    license = "BSD",
    # url = "http://github.com/pinax/bootstrap-theme",
    packages = find_packages(),
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ],
    include_package_data=True
)
