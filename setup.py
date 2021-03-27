import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-custom-logging",
    author="Seonghyeon Cho",
    author_email="seonghyeoncho96@gmail.com",
    description="Django middleware for custom format logging",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sh-cho/django-custom-logging",
    project_urls={
        "Bug Tracker": "https://github.com/sh-cho/django-custom-logging/issues",
        "Source Code": "https://github.com/sh-cho/django-custom-logging",
    },
    classifiers=[
        # see https://pypi.org/classifiers/
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
