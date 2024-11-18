import setuptools

__version__ = "0.0.1"

with open("README.md", "r", encoding="utf8") as f:
    long_description = f.read()


REPO_NAME = "CNN Classifier Project"
AUTHOR_NAME = "Md Saif Ali"
SRC_REPO = "DL-Project"
AUTHOR_Email = "shaikhsaifali346@gmail.com"



setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_Email,
    description="Classification Project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)   