import pytest

if __name__ == "__main__":
    mode = input("Введите режим (ui/api/all): ").strip().lower()
    if mode == "ui":
        pytest.main(["-q", "test/test_ui.py"])
    elif mode == "api":
        pytest.main(["-q", "test/test_api.py"])
    else:
        pytest.main(["-q", "test/"])
