class SpeechRecognitionError(Exception):
    """
    Custom exception class for speech recognition errors.
    """
    pass

def handle_error(e):
    """
    Function to handle errors.
    
    Parameters:
    - e: Error object
    """
    print("Error:", e)
