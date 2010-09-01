from os.path import join

from numpy.distutils.system_info import get_info


def configuration(parent_package='',top_path=None):
    from numpy.distutils.misc_util import Configuration

    config = Configuration('lib', parent_package, top_path)

    config.add_include_dirs(join('..','core','include'))

    ndarray_lib_dir = get_info('ndarray')['library_dirs'][0]
    config.add_extension('_compiled_base',
                         sources=[join('src', '_compiled_base.c')],
                         library_dirs=[ndarray_lib_dir],
                         libraries=['ndarray'],
                         )

    config.add_data_dir('benchmarks')
    config.add_data_dir('tests')

    return config

if __name__=='__main__':
    from numpy.distutils.core import setup
    setup(configuration=configuration)
