from comtypes.client import CreateObject
import os
import jsonpickle
from models.group import Group


project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# генерация данных в excel
xl = CreateObject("Excel.Application")
xl.Visible = 1
wb = xl.Workbooks.Add()
for i in range(1, 11):
    xl.Range["A%s" % i].Value[()] = "Group name %s - excel" % i
wb.SaveAs(os.path.join(project_dir, "data/groups.xlsx"))
xl.Quit()


# генерация данных в json
data = [Group(name="Group name %s - json" % i) for i in range(1, 11)]
file = os.path.join(project_dir, "data/groups.json")

with open(file, 'w') as out:
    jsonpickle.set_encoder_options('json', indent=2)
    out.write(jsonpickle.encode(data))