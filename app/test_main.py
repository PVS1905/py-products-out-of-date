from unittest.mock import patch, MagicMock, Mock
import datetime
import pytest
from app.main import outdated_products


@pytest.mark.parametrize(
    "products, mocked_today, expected_result",
    [
        (
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 10),
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2022, 2, 5),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 2, 1),
                    "price": 160
                }
            ],
            datetime.date(2022, 2, 2),
            ["duck"]
        ),
        (
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 2)
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2022, 2, 1)
                }
            ],
            datetime.date(2022, 2, 2),
            ["chicken"]
        ),
        (
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2025, 9, 27)
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2023, 9, 25)
                }
            ],
            datetime.date(2022, 2, 2),
            []
        )
    ]
)
def test_outdated_products_with_past_dates(
        products: Mock,
        mocked_today: Mock,
        expected_result: Mock
) -> None:
    mocked_today = MagicMock(return_value=datetime.date(2022, 2, 2))
    with patch("datetime.date") as mock_date:
        mock_date.today = mocked_today
        result = outdated_products(products)
        assert result == expected_result
