import os
import importlib
import model

current_path = os.path.dirname(os.path.abspath(__file__))
modulefilename = 'modules.py'
modulefilepath = os.path.abspath(os.path.join(current_path, os.path.pardir, modulefilename))


with open(modulefilepath, 'r') as f:
    while True:
        modules = []
        line = f.readline()
        if not line:
            break
        if line.strip().startswith('#'):
            continue
        cuts = line.split()
        if cuts[0] == 'import':
            mods = cuts[1]
        elif cuts[0] == 'from':
            mods = cuts[1]
            assert cuts[2] == 'import'
            cls = cuts[3]
        if line.rfind(' as ') > 0:
            asname = cuts[-1]

        name = mods[mods.rfind('.')+1:]
        package = mods[mods.rfind('.')]

        imps = importlib.import_module(name, package)
        if cls:
            clasz = getattr(imps, cls)
            modules.append(clasz)
        else:
            attrs = dir(imps)
            for attr in attrs:
                if  issubclass(getattr(imps,attr), model.Model):
                    modules.append()
