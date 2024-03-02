from setuptools import setup, find_packages

setup(
    name='probuster',
    version='1.0.2',
    author='D. Sanjai Kumar',
    author_email='bughunterz0047@gmail.com',
    description=' A Python based Web Application Penetration testing tool for Information Gathering and Content Discovery',
    packages=find_packages(),
    py_modules=['probuster'],
    install_requires=[
        'alive_progress>=3.1.4',
        'art>=6.1',
        'beautifulsoup4>=4.11.1',
        'colorama>=0.4.4',
        'httpx>=0.26.0',
        'Requests>=2.31.0',
        'rich>=13.7.0',
        'urllib3>=1.26.18',
        'streamlit>=1.29.0',
        'aiofiles>=23.2.1',
        'aiohttp>=3.8.6',
        'asyncio>=3.4.3',
        'h11==0.13.0',
        'anyio>=4.2.0',
        'click>=8.1.7'  
],
    entry_points={
        'console_scripts': [
            'probuster = probuster:main'
        ]
    },
)
