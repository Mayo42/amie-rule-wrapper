from setuptools import setup

setup(
        name="amie-rule-wrapper",
        version="0.1.0",
        author="Philipp Ehler",
        author_email="p.ehler@tu-braunschweig.de",
        license="LICENSE",
        description=(
            "A wrapper which wraps AMIE rules into "
            "a more intuitive data structure"
            ),
        long_description=open("README.md").read(),
        install_requires=[
            req.rstrip("\n")
            for req in open("requirements.txt").readlines()
            if not req.startswith("#")
            ]
        )
