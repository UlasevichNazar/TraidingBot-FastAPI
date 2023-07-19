import pytest

from app.parsing.repositories.parser import AssetRepository
from app.parsing.services import AssetService


class TestService:
    @pytest.mark.asyncio
    async def test_get_assets_list(self, service):
        # Act
        result = await service.get_assets()

        # Assert
        assert isinstance(result, list)

    @pytest.mark.asyncio
    async def test_get_assets_returns_empty_list(self, service):
        # Act
        result = await service.get_assets()

        # Assert
        assert result == []

    @pytest.mark.asyncio
    async def test_update_asset_price(self, service):
        # Arrange
        file = {"01. symbol": "AAPL", "05. price": 100.00}

        # Act
        await service.update_price(file)
        assets = await service.get_assets()
        asset = next(
            (asset for asset in assets if asset["name"] == file["01. symbol"]),
            None,
        )

        # Assert
        assert asset is not None
        assert asset["current_price"] == file["05. price"]

    @pytest.mark.asyncio
    async def test_update_price_raises_error_when_file_missing_fields(self):
        # Arrange
        repository = AssetRepository(
            collection=[{"name": "AAPL", "current_price": 100.00}]
        )
        asset_service = AssetService(repository)
        file = {"01. symbol": "AAPL"}

        # Act & Assert
        with pytest.raises(KeyError):
            await asset_service.update_price(file)

    @pytest.mark.asyncio
    async def test_update_price_raises_error_when_filter_does_not_match_any_assets(
        self,
    ):
        # Arrange
        repository = AssetRepository(
            collection=[{"name": "AAPL", "current_price": 100.00}]
        )
        asset_service = AssetService(repository)
        file = {"01. symbol": "GOOG", "05. price": 200.00}

        # Act & Assert
        with pytest.raises(AttributeError):
            await asset_service.update_price(file)
