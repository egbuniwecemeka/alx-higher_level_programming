# 0x05-python-exceptions
Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General
Why Python programming is awesome
What’s the difference between errors and exceptions
What are exceptions and how to use them
When do we need to use exceptions
How to correctly handle an exception
What’s the purpose of catching exceptions
How to raise a builtin exception
When do we need to implement a clean-up action after an exception

Requirements
General
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the pycodestyle (version 2.8.*)
All your files must be executable
The length of your files will be tested using wc

## Errors and Exception
There are two distinguishable kinds of error: (a) Syntax (b) Exceptions
(a) Syntax: Also known as parsing error, the most common type of error. The parser repeats the affected line as well as a ^ underneath whee the presumed error was detected. File and line number are printed also to aid debugging.
(b) Exception: A program or func may be syntatically correct and still throw an error. Errors detected in/at execution are known as exceptions. Exceptions come in differnt forms namely ZeroDivisionError, NameError, TypeError. Standard exception names are built-in identifiers (not reserved keywords) 

Handling Exceptions
1.Example hand-exp.py: Ask a input until a valid integer is entered. Also, it can be interrupted using Control-C or any other supported operating system function.

