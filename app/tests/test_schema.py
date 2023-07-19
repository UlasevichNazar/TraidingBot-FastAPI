from decimal import Decimal

import pytest

from app.parsing.schemas import Schema


class TestSchema:
    def test_asset_valid(self):
        # Act
        asset = Schema(name="BNB", current_price=Decimal("240.64"))

        # Assert
        assert asset.name == "BNB"
        assert asset.current_price == Decimal("240.64")

    def test_asset_valid_name(self):
        # Act
        asset = Schema(name="N" * 60, current_price=Decimal("240.64"))

        # Assert
        assert asset.name == "N" * 60

    def test_asset_name_invalid_max_length(self):
        # Act & Assert
        with pytest.raises(ValueError):
            Schema(name="N" * 61, current_price=Decimal("240.64"))

    def test_asset_name_valid_min_length(self):
        # Act
        asset = Schema(name="N", current_price=Decimal("240.64"))

        # Assert
        assert asset.name == "N"

    def test_asset_name_invalid_min_length(self):
        # Act & Assert
        with pytest.raises(ValueError):
            Schema(name="", current_price=Decimal("240.64"))

    def test_current_price_valid(self):
        # Act
        asset = Schema(name="BNB", current_price=Decimal("100.64"))

        # Assert
        assert asset.current_price == Decimal("100.64")

    def test_asset_with_current_price_less_than_zero(self):
        # Act & Assert
        with pytest.raises(ValueError):
            Schema(name="BNB", current_price=Decimal(-100.00))

    def test_asset_current_price_with_max_value(self):
        # Act
        asset = Schema(name="BNB", current_price=Decimal("999999999999.99"))

        # Assert
        assert asset.current_price == Decimal("999999999999.99")
