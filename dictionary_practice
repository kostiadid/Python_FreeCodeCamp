test_settings = {
    'test': 'value',
    'test1': 'value1'
}

def add_setting(settings, pair):
    key, value = pair[0].lower(), pair[1].lower()

    if key in (k.lower() for k in settings.keys()):
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."

    settings[key] = value

    return f"Setting '{key}' added with value '{value}' successfully!"

add_setting(test_settings, ('THEME', 'dark'))
add_setting(test_settings, ('volume', 'high'))

def update_setting(settings, pair):
    key, value = pair[0].lower(), pair[1].lower()
    if not key in (k.lower() for k in settings.keys()):
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."
    settings[key] = value
    return f"Setting '{key}' updated to '{value}' successfully!"
    

update_setting(test_settings, ('theme', 'dark'))

def delete_setting(settings, key):
    key = key.lower()
    if not key in (k.lower() for k in settings.keys()):
        return f"Setting not found!"
    settings.pop(key)
    return f"Setting '{key}' deleted successfully!"
delete_setting({'theme': 'light'}, 'theme')

def view_settings(settings):
    if not settings:
        return "No settings available.\n"
    
    section = ["Current User Settings:"]
    for key, value in settings.items():
        section.append(f"{key.capitalize()}: {value}")
    return "\n".join(section) + "\n"

view_settings(test_settings)



