import pkg_resources
import yaml

def print_hello():
    print("hello")
    pass

def get_versions():
    from ._version import get_versions as _get_versions
    return _get_versions()

def get_data():
    file_path=pkg_resources.resource_filename('project_name','data/data.yml')
    with open(file_path) as file:
        data_tests = yaml.load(file, Loader=yaml.FullLoader)
    return data_tests

def list_files_in_data():
    return pkg_resources.resource_listdir('project_name', 'data')

