from dram_model import Fab_DRAM
from hdd_model import Fab_HDD
from ssd_model import Fab_SSD
from logic_model import Fab_Logic

# from pyodide.http import pyfetch
# async def request(url):
#     kwargs = {"method": "GET", "mode": "cors"}
#     response = await pyfetch(url, **kwargs)
#     return response
# async def foo():
#     res = await request("http://markmaz.com/co2calc/ACT/dram/dram_hynix.json")
#     print(res)


def model(state):
    # TODO(mmaz) currently ducktyped :( BlockOption def not in scope
    print(state["cpu_node"]["options"][0].act_desc)
    return (
        Fab_DRAM().get_cpg() + Fab_HDD().get_cpg()
    )  # + Fab_SSD().get_cpg() + Fab_Logic().get_cpg()
