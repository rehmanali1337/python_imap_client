import setuptools

required_packages = [
    "aiohttp",
]


setuptools.setup(
    name="mail_client",
    version="0.1.0",
    author="Rehman Ali",
    author_email="rehmanali.9442289@gmail.com",
    description="Python mail client for hotmail and other smtp enabled mails",
    url="",
    packages=setuptools.find_packages(),
    install_requires=required_packages,
)
