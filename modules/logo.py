from rich.text import Text
from rich.console import Console
from rich.text import Text
import os


def show_logo():
    """Displays a stylish DP logo with clouds"""
    # Clear the screen
    os.system("cls" if os.name == "nt" else "clear")

    console = Console()

    # Cloud-themed ASCII art with DP logo
    logo_text = """                                                            
                     YTTSTTSSSSSSSSSSSSSSSS         UTTTTSTTSSSSSSTSSSSSSY                          
                     UMSIBBABABBAAAABBABAAAAAAN     LSQABABBABAAAABBABBAAAAAS                       
                     UQXKAAAAH        KIHLBAAAAAF   MXVAAAAAU       QKGNFAAAAAS                     
                     UNTIAAAAH         XOYCAAAAAF   LSQAAAAAU         NTIPDAAAS                     
                     US LAAAAH         XLSBAAAAAF   N XAAAADEDDDFFDDJVEAAAAAAAS                     
                     UMSIAAAAH         XOYEAAAAAF   LSQAAAAAAAAAAAAAAAAAAIKKV                       
                     UNTJAAAAH         XJQDAAAAAF   LSQAAAAAU                                       
                     UPWKAAAACHJIHIHJJJMGMEAAAAAF   MWUAAAAAU                                       
                     UNTJAAAAAAAAAAAAAAAAAAHHHQ     LTSAAAAAU                                       

"""

    # Create gradient text
    gradient_logo = Text(logo_text)
    gradient_logo.stylize("bold #deebf8")

    # Print with padding
    console.print(gradient_logo)

