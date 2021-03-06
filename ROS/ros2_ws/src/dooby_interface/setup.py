from setuptools import setup

package_name = 'dooby_interface'

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
    maintainer='root',
    maintainer_email='root@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'dooby_interface = dooby_interface.dooby_interface:main',
            'dooby_imu = dooby_interface.dooby_imu:main',
            'dooby_gps = dooby_interface.dooby_gps:main',
            'dooby_cam = dooby_interface.dooby_cam:main',
            'dooby_sonar = dooby_interface.dooby_sonar:main',
            'clock = dooby_interface.clock:main'

        ],
    },
)
