from setuptools import setup, find_packages

setup(
    name="mpl_no_tofu",
    version="0.1",
    url="https://github.com/cgjosephlee/mpl_no_tofu",
    author="Joseph Lee",
    author_email="cgjosephlee@gmail.com",
    description="Install Noto fonts for matplotlib",
    packages=find_packages(),
    package_data={"mpl_no_tofu": ["config.json", "assets/*/METADATA.pb"]},
    install_requires=["protobuf>=3.7, <4", "matplotlib"],
)
