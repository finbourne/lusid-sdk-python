# Viewing the SDK documentation online

The SDK documentation is [available to view online](https://lusid-sdk-python.readthedocs.io/en/latest/_autosummary/sdk.lusid.html).

# Building the SDK documentation locally as HTML

You can clone this repo and use Sphinx to build the SDK documentation and view it locally as HTML:
   
1. Change to this `docs` directory:

   `cd docs`

2. Assuming a Python 3.x environment, install dependencies:

   `pip install -r requirements.txt`

3. Build the documentation:

   `make html`

4. Run a web server:

   `python -m http.server`

5. View the doc set locally in a browser at:

   http://localhost:8000/_build/html/
