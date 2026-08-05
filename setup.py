from setuptools import setup, find_packages



setup(

    name="het",

    version="4.0",

    packages=find_packages(),

    py_modules=[

        "het_cli"

    ],


    install_requires=[

        "psutil",

        "jinja2",

        "reportlab"

    ],


    entry_points={

        "console_scripts":[

            "het=het_cli:main_cli"

        ]

    }

)