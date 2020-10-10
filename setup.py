from distutils.core import setup
setup(
  name = 'lib8relay',
  packages = ['lib8relay'],
  version = '1.0.3',
  license='MIT',
  description = 'Library to control Sequent Microsystems 8-RELAY Card',
  author = 'Sequent Microsystems',
  author_email = 'olcitu@gmail.com',
  url = 'https://sequentmicrosystems.com',
  download_url = 'https://github.com/alexburcea2877/lib8relay/archive/v_1_0_3.tar.gz',
  keywords = ['relay', 'raspberry', 'power'],
  install_requires=[
          'smbus2',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers', 
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',  
    'Programming Language :: Python :: 2.7',      
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
  ],
)
