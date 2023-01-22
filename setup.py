
from distutils.core import setup


def readme():
    with open("README.md") as f:
        README = f.read()
    return README


setup(
  name = 'Topsis_Diksha_102016116',         # How you named your package folder (MyLib)
  packages = ['Topsis_Diksha_102016116'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description="TOPSIS method for multi-criteria decision making",
  long_description=readme(),
  long_description_content_type="text/markdown",
   # Give a short description about your library
  author = 'Diksha Rani',                   # Type in your name
  author_email = 'rodiksha218@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/Dik17/topsis_diksharani_102016116_1.1.0',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/Dik17/topsis_diksharani_102016116_1.1.0/archive/refs/tags/v_01.tar.gz',    # I explain this later on
  keywords = ['TOPSIS', '102016116', 'KEYWORDS'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
         'pandas',
          'numpy',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
