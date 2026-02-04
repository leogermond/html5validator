from setuptools import setup

from html5validator import __version__


setup(
    name="html5validator-leogermond",
    version=__version__,
    packages=["html5validator", "html5validator.tests", "vnujar"],
    license="MIT",
    description="Validate HTML5 files.",
    long_description=open("README.rst").read(),
    long_description_content_type="text/x-rst",
    author="Léo Germond",
    author_email="leo.germond@gmail.com",
    url="https://github.com/leogermond/html5validator",
    include_package_data=True,
    zip_safe=False,
    python_reqires=">=3.12",
    install_requires=[
        "PyYAML",
    ],
    extras_require={
        "tests": [
            "hacking",
            "pytest",
        ],
    },
    entry_points={
        "console_scripts": [
            "html5validator = html5validator.cli:main",
        ]
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
)
