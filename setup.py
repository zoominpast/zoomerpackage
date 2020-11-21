from setuptools import setup

def readme():
    with open("README.md") as f:
        return f.read()

setup(
    name="zoomerpackage",
    version='0.0.1',
    long_description=readme(),
    long_description_content_type="text/markdown",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent'
    ],
    url="https://github.com/zoominpast/zoomerpackage",
    author="zoominpast",
    author_email="heatseeker03@outlook.com",
    keywords="core package",
    license="MIT",
    packages=['zoomerpackage'],
    install_reqiures=['datetime'],
    include_package_data=True,
    zip_safe=False)
    