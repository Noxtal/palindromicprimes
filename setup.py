from distutils.core import setup
setup(
    name='palindromicprimes',
    packages=['palindromicprimes'],
    version='1.0.0',
    license='MIT',
    description='Python library to search through palindromic primes. Based on the A002385 number set. Created for the NahamCon CTF 2020.',
    author='Noxtal',
    author_email='contact.noxtal@gmail.com',
    url='https://github.com/Noxtal/palindromicprimes/',
    download_url='https://github.com/Noxtal/palindromicprimes/archive/1.0.0.tar.gz',
    keywords=['primes', 'palindromes', 'numbers'],
    install_requires=[            # I get to this in a second
        'functools',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
