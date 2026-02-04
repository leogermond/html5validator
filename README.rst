HTML5 Validator 2
=================

    ``html5validator`` is a command line tool that tests files for
    HTML5 validity. This was written with static site generators like
    `Jekyll <http://jekyllrb.com/>`_ and
    `Pelican <http://blog.getpelican.com/>`_ in mind. Dynamic html content
    (for example from JS template engines) can be crawled
    (e.g. with `localcrawl <https://github.com/svenkreiss/localcrawl>`_)
    and then validated.

.. image:: https://github.com/leogermond/html5validator/actions/workflows/tests.yml/badge.svg?branch=main
    :target: https://github.com/leogermond/html5validator/actions/workflows/tests.yml
.. image:: https://badge.fury.io/py/html5validator.svg
    :target: https://pypi.python.org/pypi/html5validator/


Install
-------

This module requires Python 3.12 or 3.13 and Java 8 (``openjdk8`` or ``oraclejdk8``).
Install with ``uv add html5validator2`` and run with

.. code-block:: bash

    html5validator --root _build/

to validate all html files in the ``_build`` directory.
Run ``html5validator --help`` to see the list of command line options::

    usage: html5validator [-h] [--root ROOT] [--match MATCH [MATCH ...]]
                          [--blacklist [BLACKLIST ...]] [--show-warnings]
                          [--no-langdetect] [--no-vnu-stdout] [--no-asciiquotes]
                          [--format {gnu,xml,json,text}]
                          [--ignore [IGNORE ...]] [--ignore-re [IGNORE_RE ...]]
                          [--config CONFIG] [-l] [-ll] [-lll] [--log LOG]
                          [--log-file LOG_FILE] [--version]
                          [files ...]

    [v2.0.1] Command line tool for HTML5 validation. Return code is 0 for valid
    HTML5. Arguments that are unknown to html5validator
    are passed as arguments to `vnu.jar`.

    positional arguments:
      files                 specify files to check

    optional arguments:
      -h, --help            show this help message and exit
      --root ROOT           start directory to search for files to validate
      --match MATCH [MATCH ...]
                            match file pattern in search (default: "*.html" or
                            "*.html *.css" if --also-check-css is used)
      --blacklist [BLACKLIST ...]
                            directory names to skip in search
      --show-warnings       show warnings and count them as errors
      --no-langdetect       disable language detection
      --no-vnu-stdout       do not use --stdout with vnu.jar
      --no-asciiquotes      do not use --asciiquotes with vnu.jar
      --format {gnu,xml,json,text}
                            output format
      --ignore [IGNORE ...]
                            ignore messages containing the given strings
      --ignore-re [IGNORE_RE ...]
                            regular expression of messages to ignore
      --config CONFIG       Path to a config file for options
      -l                    run on larger files: sets Java stack size to 2048k
      -ll                   run on larger files: sets Java stack size to 8192k
      -lll                  run on larger files: sets Java stack size to 32768k
      --log LOG             log level: DEBUG, INFO or WARNING (default: WARNING)
      --log-file LOG_FILE   Name for log file. If no name supplied then no log
                            file will be created
      --version             show program's version number and exit

This module uses the `validator.nu backend <https://github.com/validator/validator.github.io>`_
which is written in Java. Therefore, a Java Runtime Environment must be
available on your system. Since version 0.2, Java 8 is required.


Checking CSS/SVG
----------------

.. code-block:: bash

    html5validator --root _build/ --also-check-css

    # checking only CSS
    html5validator --root _build/ --skip-non-css

Replace ``css`` with ``svg`` for similar behavior with SVG files.


Technical Notes
---------------

* If you are using grunt already, maybe consider using the
  `grunt-html <https://github.com/jzaefferer/grunt-html>`_ plugin for grunt instead.
* Use ``--ignore-re 'Attribute "ng-[a-z-]+" not allowed'`` with angular.js apps.
* Example with multiple ignores: ``html5validator --root tests/multiple_ignores/ --ignore-re 'Attribute "ng-[a-z-]+" not allowed' 'Start tag seen without seeing a doctype first'``


Changelog
---------

Install a particular version, for example ``0.1.14``, with ``pip install html5validator==0.1.14``.

* `main <https://github.com/svenkreiss/html5validator/compare/v2.0.1...main>`_
* `2.0.1 <https://github.com/leogermond/html5validator/compare/v0.4.2...v2.0.1>`_ (2026-02-04)
    * fork
    * updated major to be sure not to confuse with original
    * remove support for older python versions
    * vnu.jar updated to 26.01.03
    * add programmatic interface ``validator.get_errors(files)``
* `0.4.2 <https://github.com/svenkreiss/html5validator/compare/v0.4.0...v0.4.2>`_ (2022-05-29)
    * test with Python 3.10
    * vnu.jar updated to 20.6.30
    * compatibility restored with certain versions of Python (`os.errno` issue)
* `0.4.0 <https://github.com/svenkreiss/html5validator/compare/v0.3.3...v0.4.0>`_ (2021-05-03)
    * update vnu jar to 21.4.9
    * use `--stdout` and `--asciiquotes` by default for vnu.jar
    * make `--format=json` parsable
    * better log file and config file tests
    * move tests to GitHub Actions and setup auto-deploy to PyPI from GitHub releases
* `0.3.3 <https://github.com/svenkreiss/html5validator/compare/v0.3.2...v0.3.3>`_ (2019-12-07)
    * `PR#59 <https://github.com/svenkreiss/html5validator/pull/59>`_
* `0.3.2 <https://github.com/svenkreiss/html5validator/compare/v0.3.1...v0.3.2>`_ (2019-11-22)
    * update vnu jar to 18.11.5
    * better output check `PR#57 <https://github.com/svenkreiss/html5validator/pull/57>`_ by `@Cyb3r-Jak3 <https://github.com/Cyb3r-Jak3>`_
* `0.3.1 <https://github.com/svenkreiss/html5validator/compare/v0.3.0...v0.3.1>`_ (2018-06-01)
    * update vnu jar to 18.3.0
    * pass remaining command line options to ``vnu.jar``
    * allow to match multiple file patterns, e.g. ``--match *.html *.css``
* `0.3.0 <https://github.com/svenkreiss/html5validator/compare/v0.2.8...v0.3.0>`_ (2018-01-21)
    * update vnu jar to 17.11.1
    * support explicit list of files: ``html5validator file1.html file2.html``
    * new command line options: ``--no-langdetect``, ``--format``
    * new tests for ``--show-warnings`` flag
    * refactored internal API
    * bugfix: check existence of Java
    * bugfix: split Java and vnu.jar command line options
* `0.2.8 <https://github.com/svenkreiss/html5validator/compare/v0.2.7...v0.2.8>`_ (2017-09-08)
    * update vnu jar to 17.9.0
    * suppress a warning from the JDK about picked up environment variables
* `0.2.7 <https://github.com/svenkreiss/html5validator/compare/v0.2.5...v0.2.7>`_ (2017-04-09)
    * update vnu jar to 17.3.0
    * lint Python code
* `0.2.5 <https://github.com/svenkreiss/html5validator/compare/v0.2.4...v0.2.5>`_ (2016-07-30)
    * clamp CLI return value at 255: `PR26 <https://github.com/svenkreiss/html5validator/pull/26>`_
* `0.2.4 <https://github.com/svenkreiss/html5validator/compare/v0.2.3...v0.2.4>`_ (2016-07-14)
    * a fix for Cygwin thanks to this `PR20 <https://github.com/svenkreiss/html5validator/pull/20>`_
* `0.2.3 <https://github.com/svenkreiss/html5validator/compare/v0.2.2...v0.2.3>`_ (2016-07-05)
    * ``vnu.jar`` updated to 16.6.29 thanks to this `PR <https://github.com/svenkreiss/html5validator/pull/19>`_
* `0.2.2 <https://github.com/svenkreiss/html5validator/compare/v0.2.1...v0.2.2>`_ (2016-04-30)
    * ``vnu.jar`` updated to 16.3.3
* `0.2.1 <https://github.com/svenkreiss/html5validator/compare/v0.1.14...v0.2.1>`_ (2016-01-25)
    * ``--ignore``, ``--ignore-re``: ignore messages containing an exact pattern or
      matching a regular expression (migration from version 0.1.14: replace ``--ignore`` with ``--ignore-re``)
    * curly quotes and straight quotes can now be used interchangeably
    * change Java stack size handling (introduced the new command line options ``-l``, ``-ll`` and ``-lll``)
    * update vnu.jar to 16.1.1 (which now requires Java 8)
* `0.1.14 <https://github.com/svenkreiss/html5validator/compare/v0.1.12...v0.1.14>`_ (2015-10-09)
    * change text encoding handling
    * adding command line arguments ``--log`` and ``--version``
* `0.1.12 <https://github.com/svenkreiss/html5validator/compare/v0.1.9...v0.1.12>`_ (2015-05-07)
    * document how to specify multiple regular expressions to be ignored
    * add ``--ignore`` as command line argument. Takes a regular expression
      for warnings and errors that should be ignored.
* `0.1.9 <https://github.com/svenkreiss/html5validator/compare/v0.1.8...v0.1.9>`_ (2015-03-02)
