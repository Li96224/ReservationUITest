
import pytest

pytest.main()


if __name__ == '__main__':
    command_line=["-s","--alluredir=report"]
    pytest.main(command_line)
