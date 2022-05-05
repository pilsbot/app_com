from setuptools import setup

package_name = 'app_com'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Christophe Stilmant',
    maintainer_email='Christophe.Stilmant@gmx.de',
    description='Package to communicate with the smartphone app over bluetooth',
    license='GPL 3.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'node = app_com.app_com:main',
        ],
    },
)
