from distutils.core import setup

setup(
    name='asyncio-pause',
    version='0.4',
    license='LICENSE.txt',
    author='Jeremy Gillick - Inaki Abadia',
    author_email='none@none.com',
    packages=['asyncio-pause', 'asyncio-pause.tests'],
    url='https://github.com/iAbadia/python-asyncio-pause',
    description='A timestamp-based sleep function for Python using asyncio.',
    long_description=open('README.rst').read(),
    platforms='osx, posix, linux, windows',
    keywords='sleep timestamp datetime asyncio',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Environment :: Console'
    ]
)
