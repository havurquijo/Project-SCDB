from setuptools import setup, find_packages
# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()
setup(
  name = 'SCDB_ML_app',         # How you named your package folder (MyLib)
  # other arguments omitted
  long_description=long_description,
  long_description_content_type='text/markdown',
  packages=find_packages(),   # 
  include_package_data=True,
  version = '1.3.1',      # Start with a small number and increase it with every change you make
  license='AGPL 3.0',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'A MACHINE LEARNING ANALYZER DEPLOYED INTO A WEBPAGE',   # Give a short description about your library
  author = 'HERMES A V URQUIJO',                   # Type in your name
  author_email = 'hvurquijo@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/havurquijo/Project-SCDB',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/havurquijo/Project-SCDB/archive/refs/tags/v1.0.0-alpha.tar.gz',    # I explain this later on
  keywords = [
      'MACHINE', 
      'LEARNING', 
      'SCDB',
      'SUPREME',
      'COURT',
      'WEBPAGE'
      ],   # Keywords that define your package best
  install_requires=[            # Required to install
            'flask',
            'pathlib',
            'pandas',
            'numpy',
            'scikit-learn',
            'requests',
            'statsmodels',
            'plotly'
            ],
  package_data={
        'scdb_ml_app': [
            'models/*',
            'static/*',
            'static/js/*',
            'static/icon/*',
            'static/styles/*',
            'templates/*'
            ],
    },
  classifiers=[
    'Development Status :: 3 - Alpha',      # Choose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: GNU Affero General Public License v3',   # Pick a license
    'Programming Language :: Python :: 3.12'     # Specify which Python versions you want to support
]
)