# 使用 . 标识测试成功（PASSED）
# 使用 F 标识测试失败（FAILED）


def test_passing():
    assert (1, 2, 3) == (1, 2, 3)


def test_failing():
    assert (1, 2, 3) == (3, 2, 1)
