import setuptools

requires = [
    "flake8 > 3.0.0",
]

flake8_entry_point = # ...

setuptools.setup(
    name="flake8_deved",
    license="MIT",
    version="0.1.0",
    description="DevEd's extension to flake8",
    author="Twilio",
    author_email="deved@twilio.com",
    url="https://code.hq.twilio.com/deved/flake8_deved",
    packages=[
        "flake8_deved",
    ],
    install_requires=requires,
    entry_points={
        flake8_entry_point: [
            'X = flake8_deved:ExamplePlugin',
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
