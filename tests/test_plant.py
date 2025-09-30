from classes.plant import Plant

def test_plant_instantiation():
    # Arrange
    name = "Orchid"
    water_level = 3
    sunlight_hours = 1
    is_blooming = True

    # Act
    plant = Plant(name, water_level, sunlight_hours, is_blooming)

    # Assert
    assert plant.name == name
    assert plant.water_level == water_level
    assert plant.sunlight_hours == sunlight_hours
    assert plant.is_blooming is True

def test_plant_class_initialization_default_is_blooming():
    # Arrange
    name = "Lily"
    water_level = 4
    sunlight_hours = 5

    # Act
    plant = Plant(name, water_level, sunlight_hours)

    # Assert
    assert plant.name == name
    assert plant.water_level == water_level
    assert plant.sunlight_hours == sunlight_hours
    assert plant.is_blooming is False
