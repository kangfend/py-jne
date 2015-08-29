from setuptools import setup

setup(
    name='py-jne',
    packages=['jne'],
    version='0.1.3',
    description='PyJNE is a tool to simplify the user in using the JNE API such as tracking stuff, check tariffs and others.',
    license='MIT',
    author='Sutrisno Efendi',
    author_email='kangfend@gmail.com',
    url='https://github.com/kangfend/py-jne',
    download_url='https://github.com/kangfend/py-jne/tarball/0.1.3',
    keywords=['JNE', 'Tracking', 'Courier', 'Indonesia'],
    install_requires=['requests==2.6.0'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
