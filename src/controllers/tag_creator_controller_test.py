from .tag_creator_controller import TagCreatorController


def test_create():
    mock_value = "image_path"
    tag_creator_controller = TagCreatorController()

    result = tag_creator_controller.create(mock_value)

    print()
    print(result)

    assert isinstance(result, dict)
    assert "data" in result
    assert "type" in result["data"]
    assert "count" in result["data"]
    assert "path" in result["data"]
    assert result["data"]["type"] == "Tag Image"
    assert result["data"]["count"] == 1
    assert result["data"]["path"] == f'{ mock_value }.png'