import setuptools

requires = [
    "flake8 > 3.0.0",
]

setuptools.setup(
    name="flake8_deved",
    license="MIT",
    version="0.1.0",
    description="DevEd's extension to flake8",
    author="Twilio",
    author_email="deved@twilio.com",
    url="https://code.hq.twilio.com/deved/flake8_deved",
    packages=setuptools.find_packages(),
    install_requires=requires,
    entry_points={
        'flake8.extension': [
            'TWI101 = plugins.field_removal:checker',
        ],
    },
    classifiers=[
        "Framework :: Flake8",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Quality Assurance",
    ],
)
