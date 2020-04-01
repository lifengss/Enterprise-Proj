from model import Model

model = Model()
global tab
tab  = '    '
model_name = str(model.__class__.__name__)
file = './script/'+ model_name +'.py'
file_head = '# -*-coding:utf-8-*-\n\nimport torch\nimport torch.nn as nn\n\nclass '\
                + str(model.__class__.__name__)+'(nn.Module):\n'+tab+'def __init__(self,):\n'+tab+tab\
                + 'super(' + model_name + ', self).__init__()\n'

# for name, m in model.named_modules():
#     print(name,m)

def nn_replace(model):
    global tab
    script = ''
    tmp_script = ''
    if len(model._modules) == 0:
        # name, m = model.named_modules()
        # print('module: nn.{},'.format(str(model)))
        script += 'nn.{},\n'.format(str(model))
        return script, tmp_script
        # model.pop(name)
    else:
        for n,m in model._modules.items():
            name = n
            s,_ = nn_replace(m)
            script += s
            try:
                int(n)
                continue
            except ValueError:
                pass
            # print('name: {}'.format(name))
            script = 'self.' + name + ' = nn.Sequential(' + script + ')\n'
            tmp_script += tab + tab + script
            script = ''
    return script, tmp_script


_, script = nn_replace(model)
print(script)

file_head += script
with open(file,'w') as f:
    f.write(file_head)
    
