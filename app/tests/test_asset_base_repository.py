import pytest

from app.parsing.repositories.base import AssetNotFound


class TestBaseRepository:
    @pytest.mark.asyncio
    async def test_create_and_get_asset_successfully(self, base_repo):
        # Arrange
        file = {"name": "test", "value": 1}
        # Act
        await base_repo.create(file)
        res = base_repo.get({"name": "test"})
        # Assert
        result_list = [item async for item in res]
        assert len(result_list) == 1
        assert result_list[0]["name"] == "test"
        assert result_list[0]["value"] == 1

    @pytest.mark.asyncio
    async def test_update_valid(self, base_repo):
        # Arrange
        filter = {"name": "test"}
        file = {"name": "test", "value": 1}
        update = {"value": 2}
        await base_repo.create(file)

        # Act
        await base_repo.update(filter, update)
        res = base_repo.get({"name": "test"})

        # Assert
        result_list = [item async for item in res]
        assert result_list[0]["value"] == 2

    @pytest.mark.asyncio
    async def test_get_with_non_exiting_asset(self, base_repo):
        # Arrange
        file = {"name": "test", "value": 1}
        await base_repo.create(file)

        # Act
        res = base_repo.get({"name": "test1"})

        # Arrange
        result_list = [item async for item in res]
        assert len(result_list) == 0

    @pytest.mark.asyncio
    async def test_update_with_non_exiting_asset(self, base_repo):
        # Arrange
        file = {"name": "test", "value": 1}
        filter = {"name": "test1"}
        update = {"value": 2}
        await base_repo.create(file)

        # Act & Assert
        with pytest.raises(AssetNotFound):
            await base_repo.update(filter, update)

    @pytest.mark.asyncio
    async def test_delete_successfully(self, base_repo):
        # Arrange
        file = {"name": "test", "value": 1}
        await base_repo.create(file)

        # Act
        delete_result = await base_repo.delete({"name": "test"})

        # Assert
        assert delete_result.deleted_count == 1

    @pytest.mark.asyncio
    async def test_delete_with_non_exiting_asset(self, base_repo):
        # Arrange
        file = {"name": "test", "value": 1}
        await base_repo.create(file)

        # Act
        delete_result = await base_repo.delete({"name": "test1"})

        # Assert
        assert delete_result.deleted_count == 0
