from setuptools import setup, find_packages

setup(
    name='probuster',
    version='1.0.1',
    author='D. Sanjai Kumar',
    author_email='bughunterz0047@gmail.com',
    description=' A Python based Web Application Penetration testing tool for Information Gathering.',
    packages=find_packages(),
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
        'asyncio>=3.4.3'
        
        
    ],
    entry_points={
        'console_scripts': [
            'probuster = probuster.probuster:main'
        ]
    },
)
