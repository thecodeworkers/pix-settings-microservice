from .business_settings import start_business_setting_service
from .general_settings import start_general_setting_service
from .sessions import start_session_service

def start_all_servicers():
    start_business_setting_service()
    start_general_setting_service()
    start_session_service()

def start_all_emiters():
    """
    Emition of Emiters
    """
    pass