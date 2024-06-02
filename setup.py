from setuptools import setup, find_packages
setup(
  name = 'SCDB_ML_app',         # How you named your package folder (MyLib)
  packages=find_packages(),   # Chose the same as "name"
  version = '1.0',      # Start with a small number and increase it with every change you make
  license=' AGPL-3.0-only',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'A MACHINE LEARNING ANALIZER DEPLOYED INTO A WEBPAGE',   # Give a short description about your library
  author = 'HERMES A V URQUIJO',                   # Type in your name
  author_email = 'hvurquijo@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/havurquijo/Project-SCDB',   # Provide either the link to your github or to your website
  #download_url = ,    # I explain this later on
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
            'pickle',
            'zipfile',
            'time',
            'os'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools :: Machine Learning :: U.S. Supreme Court',
    'License :: AGPL-3.0-only',   # Again, pick a license
    'Programming Language :: Python :: 3.12',      #Specify which pyhton versions that you want to support
    'Programming Language :: html :: 5',
    'Programming Language :: javascript',
    'Programming Language :: css',
  ],
)