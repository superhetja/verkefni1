from platform import system as system_name # Returns the system/OS name
from os import system as system_call       # Execute a shell command
class Clear:
    '''Clearar skjáinn eftir hverja aðgerð'''
    def __init__(self):
        pass

    def clear_screen(self):
        '''
        Clears the terminal screen.
        '''
        # Clear command as function of OS
        command = "-cls" if system_name().lower()=="windows" else "clear"

        # Action
        system_call(command)