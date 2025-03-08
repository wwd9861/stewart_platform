from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'stewart_platform'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='wwd9861',
    maintainer_email='wwd9861@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'stewart_tf_platform = stewart_platform.stewart_tf_platform:main',
            'stewart_tf_platform_joint = stewart_platform.stewart_tf_platform_joint:main',
            'stewart_tf_servo = stewart_platform.stewart_tf_servo:main',
            'stewart_ik = stewart_platform.stewart_ik:main',
        ],
    },
)
