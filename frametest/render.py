from jinja2 import Template
from jinja2.environment import Environment
from jinja2 import FileSystemLoader

def render(template_name, **kwargs):
    """
    Минимальный пример работы с шаблонизатором
    :param template_name: имя шаблона
    :param kwargs: параметры для передачи в шаблон
    :return:
    """
    env = Environment()
    env.loader = FileSystemLoader('.')
    tmpl = env.get_template(template_name)

    return tmpl.render(**kwargs)

output_test = render('index.html', object_list=[{'name': 'Leo'}, {'name': 'Kate'}])
print(output_test)