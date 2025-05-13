import os

import pytest

from hub.utils.state import StatefulList


@pytest.fixture
def TestingStatefulList():
    try:
        os.remove(StatefulList("test").state.path)
    except FileNotFoundError:
        pass
    finally:
        l = StatefulList("test")
        yield l
        os.remove(StatefulList("test").state.path)


def test_StatefulList_init_no_items(TestingStatefulList):
    l = TestingStatefulList

    assert len(list(l)) == 0


def test_StatefulList_init_with_items():
    try:
        os.remove(StatefulList("test").state.path)
    except FileNotFoundError:
        pass
    finally:
        l = StatefulList("test", 1, 2, 3)
        return l

    assert len(list(l)) == 3


def test_StatefulList_add_item(TestingStatefulList):
    l = TestingStatefulList
    
    l.add(1)
    l.add(2)

    assert len(list(l)) == 2


def test_StatefulList_remove_item(TestingStatefulList):
    l = TestingStatefulList

    l.add(1)
    l.remove()

    assert len(list(l)) == 0


def test_StatefulList_undo(TestingStatefulList):
    l = TestingStatefulList

    l.add(1)
    l.add(2)
    l.undo()

    assert len(list(l)) == 1