import os
import importlib
import model
import modules
import types

current_path = os.path.dirname(os.path.abspath(__file__))
module_dir_name = 'modules'
module_dir_path = os.path.abspath(os.path.join(current_path, os.path.pardir, module_dir_name))

def list_module(mod,farmod=''):
    mod_path_list = mod.__path__
    mod_name = mod.__name__
    if len(mod_path_list) == 1:
        mod_path = mod_path_list[0]
        submods = os.listdir(mod_path)
        for file in submods:
            file_path = os.path.join(mod_path, file)
            if os.path.isdir(file_path):
                files = os.listdir(file_path)
                if "__init__.py" in files:
                    submodule = importlib.import_module('.'.join(farmod_name,file), mod_name)
                    list_module(submods,mod)
            elif os.path.isfile(file_path):
                obj = getattr(mod,file)
                attrs = dir(obj)
                for attr in attrs:
                    unit = getattr(obj,attr)
                    if type(unit) is types.

                if issubclass(obj, model.Model)

def load_from_file(filepath):
    class_inst = None
    expected_class = 'MyClass'

    mod_name,file_ext = os.path.splitext(os.path.split(filepath)[-1])

    if file_ext.lower() == '.py':
        py_mod = importlib.im
            #imp.load_source(mod_name, filepath)

    elif file_ext.lower() == '.pyc':
        py_mod = imp.load_compiled(mod_name, filepath)

    if hasattr(py_mod, expected_class):
        class_inst = getattr(py_mod, expected_class)()

    return class_inst

if __name__ == '__main__':
    list_module(modules)
    exit(0)














with open(modulefilepath, 'r') as f:
    modules = []
    while True:

        line = f.readline()
        if not line:
            break
        if line.strip().startswith('#'):
            continue
        if not line.strip():
            continue
        annotation_pos = line.find('#')
        if annotation_pos > 0:
            para_str = line[annotation_pos+1:]
            line = line[:annotation_pos]
        cuts = line.split()
        if cuts[0] == 'import':
            mods = cuts[1]
        elif cuts[0] == 'from':
            mods = cuts[1]
            assert cuts[2] == 'import'
            cls = cuts[3]
        if line.rfind(' as ') > 0:
            asname = cuts[-1]

        dot_pos = mods.rfind('.')
        name = mods[dot_pos+1:]
        package = None if dot_pos < 0 else mods[:dot_pos]

        imps = importlib.import_module(mods, package)
        if cls:
            clasz = getattr(imps, cls)
            modules.append(clasz)
        else:
            attrs = dir(imps)
            for attr in attrs:
                clasz = getattr(imps, attr)
                if issubclass(clasz, model.Model):
                    modules.append(clasz)
        if para_str:
            paras = para_str[para_str.find('('):para_str.find(')')].split(',')
            inst = clasz()