from setuptools import setup

package_name = 'dooby_ai'

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
    maintainer='ubuntu',
    maintainer_email='ubuntu@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'object_detection = dooby_ai.object_detection:main',
            'depth_estimation = dooby_ai.depth_estimation:main',
            'lane_detection = dooby_ai.lane_detection:main',
            'yolo_detection = dooby_ai.yolo_detection:main'
        ],
    },
)
