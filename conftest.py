import pytest
# @pytest.fixture(autouse="true")
@pytest.fixture(params=["参数1","参数2"])

def myfixture(reqeuest):
    print("执行myfixture.带参数%s"%request.param)

def pytest_collection_modifyitems(session, config, items):
    print(type(items))
    items.reverse()
    for item in items:
        item.name == item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid == item.nodeid.encode('utf-8').decode('unicode-escape')
        if "add" in item._nodeid:
            item.add_marker(pytest.mark.add)
        if "div" in item._nodeid:
            item.add_marker(pytest.mark.div)
