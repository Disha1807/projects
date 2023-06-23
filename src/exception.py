import sys
import logging

def error_message_details(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info() # error details in which file which line it has the exception

    file_name = exc_tb.tb_frame.f_code.co_filename #custon exception handling 

    error_msg ='Error occurred in python script name [{0}] line number [{1}] Error message [{2}]'.format(
        file_name,exc_tb.tb_lineno,str(error)
    )

    return error_msg


class CustomException(Exception):
    def __init__(self, error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message
    
