import setuptools

setuptools.setup(
    name = "pyunduh",
    description = "a simple python downloader package",
    version = "0.0.2",
    author = "Aza Maulana",
    author_email = "azamaulanaaa@gmail.com",
    python_requires = '>=3.7, <4',
    packages = setuptools.find_packages("src"),
    package_dir = {"": "src"},
)
