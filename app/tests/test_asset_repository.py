import pytest

from app.parsing.repositories.base import AssetNotFound


class TestAssetRepository:
    @pytest.mark.asyncio
    async def test_get_assets_returns_list_of_assets(self, asset_repo):
        # Arrange
        await asset_repo.create({"name": "asset1", "current_price": 100.00})
        await asset_repo.create({"name": "asset2", "current_price": 200.00})
        await asset_repo.create({"name": "asset3", "current_price": 250.00})
        # Act
        assets = await asset_repo.get_assets()
        # Assert
        assert len(assets) == 3
        assert assets[0]["name"] == "asset1"
        assert assets[0]["current_price"] == 100.00
        assert assets[1]["name"] == "asset2"
        assert assets[1]["current_price"] == 200.00
        assert assets[2]["name"] == "asset3"
        assert assets[2]["current_price"] == 250.00

    @pytest.mark.asyncio
    async def test_update_asset_price_with_non_exiting_asset(self, asset_repo):
        # Act
        await asset_repo.update_asset_price(
            {"name": "asset1"}, {"current_price": 120.00}
        )
        assets = await asset_repo.get_assets()
        # Assert
        assert len(assets) == 1
        assert assets[0]["name"] == "asset1"

    @pytest.mark.asyncio
    async def test_update_asset_price(self, asset_repo):
        # Arrange
        await asset_repo.update_asset_price(
            {"name": "asset1"}, {"current_price": 100.00}
        )
        filter = {"name": "asset1"}
        file = {"current_price": 200.00}
        # Act
        await asset_repo.update_asset_price(file, filter)
        # Assert
        assets = await asset_repo.get_assets()
        assert len(assets) == 1
        assert assets[0]["name"] == "asset1"
        assert assets[0]["current_price"] == 200.00

    @pytest.mark.asyncio
    async def test_get_assets_returns_empty_list(self, asset_repo):
        # Act
        assets = await asset_repo.get_assets()
        # Assert
        assert len(assets) == 0

    @pytest.mark.asyncio
    async def test_update_raises_error_when_no_matching_asset_found(self, asset_repo):
        # Act & Assert
        with pytest.raises(AssetNotFound):
            await asset_repo.update({"name": "asset10001"}, {"current_price": 20.0})
