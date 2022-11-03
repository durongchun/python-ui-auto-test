
# 1.Required dependencies
python 3.8

```
BeautifulReport 0.1.2
ParamUnittest   0.2
PyMySQL         0.9.3
futures         3.1.1
pip             10.0.1	
redis           3.3.11
selenium        3.141.0	
setuptools      39.1.0	
tomorrow        0.2.4	
urllib3         1.25.7	
```

# 2.Project structure
```
python-ui-auto-test
    - api-test (api test package, no content added)
    - ui-test (ui test package)
        - base (related to project initialization configuration)
        - case (test case script)
        - common (common method)
        - data (data driven)
        - locator (element positioning corresponding to the page)
        - page (page class)
        - report
            - html (html report)
            - log (log report)
            - img (test screenshot)
        - resource (resource folder)
            - config (configuration file)
            - driver
        - util (tools)
        - README.md
        - requirements.txt (dependencies list)
        - run_all.py (similar to testng, single threading)
        - run_all_mutithread.py (similar to testng, single thread, multithreading)
    - venv
    - .gitignore
External Libraries
Scratches and Consoles
```
