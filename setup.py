import setuptools

setuptools.setup(
    name = "pyunduh",
    description = "a simple python downloader package",
    version = "0.0.4",
    author = "Aza Maulana",
    author_email = "azamaulanaaa@gmail.com",
    python_requires = '>=3.7, <=3.11',
    packages = setuptools.find_packages("src"),
    package_dir = {"": "src"},
    install_requires = [
        "bs4>='0.0.1'",
        "js2py>='0.71'",
    ],
    extras_require = {
        "dev": [
            "pytest",
        ],
    },
)
