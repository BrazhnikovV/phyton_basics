import os
import yaml

# Структура проекта
# fs_structure = {'my_project':[
#     {'settings':['__init__.py', 'dev.py', 'prod.py']},
#     {'mainapp':['__init__.py', 'models.py', 'views.py', {'templates':[{
#         'mainapp':['base.html', 'index.html']}]}]
#     },
#     {'authapp':['__init__.py', 'models.py', 'views.py', {'templates':[{
#         'authapp':['base.html', 'index.html']}]}]
#      }
# ]}

# f = open('config.yaml', 'w')
# f.write(yaml.dump(fs_structure))
# f.close()

with open('dz_7/config.yaml') as yaml_file:
    fs_structure = yaml.safe_load(yaml_file)[0]


def create_structure(data):
    for folder, data_tmps in data.items():
        if not os.path.exists(folder):
            os.mkdir(folder)
        # перейти в созданную или существовавшую ранее папку
        os.chdir(folder)

        for data_tmp in data_tmps:
            # проверить, что data_tmp является словарем
            if isinstance(data_tmp, dict):
                create_structure(data_tmp)
            else:
                if not os.path.exists(data_tmp):
                    if '.' in data_tmp:
                        with open(data_tmp, 'w') as f:
                            f.write('')

    else:
        os.chdir('../')

create_structure(fs_structure)
