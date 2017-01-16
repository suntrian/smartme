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

    submods = dir(mod)
    for submod in submods:
        if submod.startswith("__"):
            continue
        obj = getattr(submod, mod)
        if type(obj) is types.ModuleType:
            list_module(obj)
        elif type(obj) is type:
            if issubclass(obj, model.Model):
                obj.start()

    if len(mod_path_list) == 1:
        mod_path = mod_path_list[0]
        packages = os.listdir(mod_path)
        for file in packages:
            file_path = os.path.join(mod_path, file)
            if os.path.isdir(file_path):
                files = os.listdir(file_path)
                if "__init__.py" in files:
                    try:
                        subpackages = importlib.import_module('.'.join([farmod,file]), mod_name)
                        list_module(subpackages,'.'.join([farmod, mod_name]))
                    except Exception as e:
                        print(e)
            elif os.path.isfile(file_path):
                try:
                    mod, ext = os.path.splitext(file)
                    if ext in ['.py', '.pyc']:
                        module = importlib.import_module(mod, mod_name)
                        attrs = dir(module)
                        for attr in attrs:
                            try:
                                if attr.startswith('__'):
                                    continue
                                unit = getattr(module, attr)
                                if issubclass(unit, model.Model):
                                    unit().start()
                            except Exception as e:
                                print(e)
                except Exception as e:
                    print(e)

if __name__ == '__main__':
    list_module(modules)
    exit(0)
