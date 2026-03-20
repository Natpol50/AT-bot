# -----------------------------------------------------------------------------
#  Displays.py
#  Copyright (c) 2024 Asha the Fox 🦊
#  All rights reserved.
#
#  This module provides functions to have graphics in the cli during bot startup.
#  It is separed to make the code easier to read for anyone trying to help or maintain the code.
#  It is intended to be used as a library to support the main script (AT_bot.py).
#  
#  Functions:
#      Welcome() - The First thing someone should see when running the script.
#      DS_api() - The ASCII showed when the user is needed to enter a discord bot token.
#      DPL_api() - The ASCII showed when the user is needed to enter a deepl api token.
# -----------------------------------------------------------------------------

__author__ = "Asha Geyon (Natpol50)"
__version__ = 0.1
__all__ = ['Welcome', 'DS_api', 'DPL_api']
__last_revision__ = '2024-09-05'

import os

def Welcome () -> None:
    os.system("title ATbot, welcome ! ") #Welcome page / Copyright ?
    print("""                         .::^^^^:..                     
                   :!J5GB#&&@@@&&&#BPY7~.               
               .!5B&@@@&&&&&&&&&&&&&&@@@&GJ^            
             ~5&@@&&###################&&@@@B?:         
           !B@@&###########################&@@&Y:       
         ^G@@&#######&&&&&&##################&@@&?      
        7&@&########&#YYPB#&&##################&@@G:    
       J@@&###&&&&&&&Y^^^^~JB&##############&&##&&@B:   
      7@@####&BGGPP55!^~::^~755PGB#&&&&##&&&GG&###@@B.  
     :&@&####&PY#BP?~:::~?JJ5#&@@@@@@@@@@@@@#B&###&@@J  
     ?@&#####&BJ#@@@&G?7JJJJ&@&#&&@@@@@@@@@@@@#####&@#. 
     P@&######&5J#@@@#JJJJJJP@@@@@@@@@@@@@@@@&#####&@@~ 
     B@&######&#J~G@@Y?JJJJJ?YPB##&@@@@@@@@&&######&@@! 
     P@&#######&B!!G#JJJJJJJ??J5G#&@@@@@@&&########&@@^ 
     7@&########&#PJJJJJJJ?J5B&@@@@@@@@&&##########&@B  
     .B@&########&&BYJJJJ?5#@@@@@@@@&#BB##&&&&#&&#&@@7  
      ~&@&#########&G?J?JB@@@@@@@@BYJ????5GGB##BB&@@5   
        !&@&########&G??Y#@@@@@@@#Y???????????JJ??YPP.   
         ^B@&#######&G?J#@@@@@@@G????????????????????^   
          .Y&@&#####&5?Y&GP#@@@G?????5GG5????????????7.  
            :Y&@&&###JJJJY&@@@#?????J#  #J??JG#5!?????:  
              :?G&@@GJJ?Y&@@@@Y7?????YP Y???Y5^ .?????^  
                :75B&#B#@@@@@&PJ??Y5Y???????!^~7?????:  
                    :~7Y5GGGGBBP?77??~^~!777777?????7   
                                            .!7???7!:         
            Welcome to Asha's Autotranslation bot ! 
            Please, do not claim property of this code   """)
    input("""
        
                press enter to continue""")

def DS_api() -> None:
    os.system("title New bot, discord bot API key ")
    print("""                                                                                                                                                                                     
                             =@@@@@@@@@@=                             
                             @@@@@@@@@@@@                             
                             @@        @@                             
                   @@@      @@@        @@@      @@@                   
                  @@@@@@@@@@@@=        =@@@@@@@@@@@@@                 
                @@@   @@@@@@              @@@@@@   @@@=               
                -@                                   *@               
                %@@.                              :@@@%               
                  @+      @@@@@@@@@@@@@@@@@@      +@                  
                 @@:     @@@@@@@@@@@@@@@@@@@@     :@@                 
          =@@@@@@@      @@                  @@      @@@@@@@=          
          @@@@@@@      @@                    @@      @@@@@@@          
          @@          @@     @@@      @@@     @@          @@          
          @@          @@   .@@@@@:  :@@@@@:   %@:         @@          
          @@         @@    -@   @%  +@   @+    @@         @@          
          @@         @@     @@@@@+  :@@@@@     @@         @@          
          @@@@@@@    @@    *  @.       @  *    @@    @@@@@@@          
          =@@@@@@@   @@@@  @  +@@@@@@@@+  @  @@@@   @@@@@@@=          
                 @@: =@@@@@@ @@@@@@@@@@@@ @@@@@@= :@@                 
                  @+     @@@@@          @@@@@     +@                  
                #@@.                              :@@@%               
                -@                                   *@               
                @@@   @@@@@@              @@@@@@   @@@=               
                  @@@@@@@@@@@@=        =@@@@@@@@@@@@@                 
                   @@@      @@@        @@@      @@@                   
                             @@        @@                             
                             @@@@@@@@@@@@                             
                             =@@@@@@@@@@=                                                         
\n""")

    print('  As you chose New bot, you\'ll need a discord bot API key (a bot token). \n If you do not know how to get one, here\'s a tutorial : https://rapidapi.com/volodimir.kudriachenko/api/DiscordBot/details')


def DPL_api () -> None:
    os.system("title New bot, Deepl API key ")
    print("""                                                                                                                                     
                                    @@@@@@@@                                    
                                 @@@@@@@@@@@@@@                                 
                              @@@@@@        @@@@@@                              
                          @@@@@@@              @@@@@@@                          
                       @@@@@@@                    @@@@@@@                       
                    @@@@@@@                          @@@@@@@                    
                 @@@@@@@                                @@@@@@@                 
                @@@@                                       @@@@@                
               @@               @@@@@                         @@@               
               @@              @@@@@@@                         @@               
               @@             @@    @@@                        @@               
               @@             @@    @@@@@                      @@               
               @@              @@@@@@@  @@@@                   @@               
               @@               @@@@ @@@@  @@@@@@@@@           @@               
               @@                       @@@@  @@@@@@@          @@               
               @@                           @@@     @@         @@               
               @@                           @@@@   @@@         @@               
               @@                        @@@  @@@@@@@          @@               
               @@               @@@@  @@@   @@ @@@@@           @@               
               @@              @@@@@@@   @@@                   @@               
               @@             @@    @@@@@                      @@               
               @@             @@    @@@                        @@               
               @@              @@@@@@@                        @@@               
                @@@@            @@@@@                      @@@@@                
                 @@@@@@@                                @@@@@@@                 
                    @@@@@@@                          @@@@@@@                    
                       @@@@@@@                    @@@@@@                        
                          @@@@@@@               @@@@@                           
                             @@@@@@@           @@@                              
                                 @@@@@@        @@                               
                                    @@@@@@     @@                               
                                       @@@@@@  @@                               
                                          @@@@@@@                               
                                             @@@@                                                                                           
\n""")
    
    print('  Now, you\'ll need a Deepl API (Free or Paid, both works fine for a reasonable amount of messages per month)\n If you do not know how to find yours, here\'s a tutorial : https://support.deepl.com/hc/en-us/articles/360020695820-Authentication-Key')



if __name__ == "__main__":
    print("This is a library module and is not intended to be run directly, please use AT_bot.py .")