from setuptools import setup

with open('README.rst') as f:
    long_description = f.read()

setup(
    name='sitemapgenerator',
    version='0.1.0',
    description='Create an XML sitemap by crawling a website.',
    long_description=long_description,
    url='https://github.com/techjacker/sitemapgenerator',
    license='MIT',
    author='Andrew Griffiths',
    author_email='mail@andrewgriffithsonline.com',
    packages=['sitemapgenerator'],
    entry_points={
        'console_scripts': [
            'sitemapgenerator = sitemapgenerator.sitemapgenerator:main'
        ]
    },
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4'
    ],
)
