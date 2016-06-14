from setuptools import setup

setup(
    name='django-fullclean',
    packages=['django_fullclean'],
    version='0.0.2',
    description='Force django model call full_clean before save.',
    author='Alfred Huang',
    author_email='57082212@qq.com',
    url='https://github.com/fish-ball/django-fullclean',
    download_url='https://github.com/fish-ball/django-fullclean/tarball/0.0.2',
    keywords=['django', 'model', 'validator', 'full_clean'],
    classifiers=[],
    license='MIT License',
    install_requires=['django'],
    platforms='any',
)
