try:
    from PyQt4.QtCore import QSettings
except ImportError:
    from PyQt5.QtCore import QSettings
    
    
def init_config():
    settings = QSettings('settings_16413', QSettings.IniFormat)
    
def save_config(key='', value=''):
    settings = QSettings('settings_16413')
    if value == '':
        value = None
    settings.setValue(key, str(value))
    
def load_config(key='', default_value=''):
    settings = QSettings('settings_16413')
    value = settings.value(key)
    if (value is None) or (value == 'None'):
        return default_value
    else:
        return str(value)

    