from setuptools import setup
from setuptools.extension import Extension
import numpy as np


qpbo_directory = "QPBO-v1.3.src"
files = ["src/pyqpbo.pyx"]

setup(name='pyqpbo',
      packages=['pyqpbo'],
      version="0.1.2",
      author="Andreas Mueller",
      author_email="t3kcit@gmail.com",
      description='QPBO interface and alpha expansion for Python',
      url="http://pystruct.github.io",
      ext_modules=[
          Extension('pyqpbo.pyqpbo', sources=files, language='c++',
                    include_dirs=[qpbo_directory, "src", np.get_include()],
                    library_dirs=[qpbo_directory],
                    extra_compile_args=["-fpermissive"])
      ])
