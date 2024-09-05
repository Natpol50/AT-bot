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
    print("""                              .:~!7?JYY7.                    .?JJJ?7!^:.                            
                         :~7J5PGGP5J7~::..::^^~~~~!!!~~~^^::.:^~!7?Y5PPPY?!^.                       
                     .~?YPGGG5J7~~~!7?JY5PPPPGGGGGPYYYYYYYYYYYYJJ?7!!!7?YPGGPY7^.                   
                   :7YGGGPYJ???Y5PGGGGGGGGGGPPPPPG5777??????????JJJYYYYJ???J5PGG5?^                 
                  ~5GGP5YY5PPGGGGGPPPPPPPPPPPPPPPPPPBPJ?????????????????JJYYJYY5GGP~                
                 ~5GPPPPPGGGPPPPPPPPPPPPPPPPPPPPPPB@@@BPPPPPPPPPPPPY?????????JJYPGGP~               
                ~5GPPPPGPPPPPPPPPPPPPPPPPPPPPPPPPPB@@&5YYYYYYYYYPGG5???????????7?YPGP~              
               ^5GPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPB@@@GYJ??????7YGG5????????YB#GJ7JPG5^             
              .YGPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPB@@@@@@G55PY?JPBG5????????5&@@&J7?PGY.            
              ?GPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPB@@@&BGY??P5Y&@@#577??????JP#&#J??JPG?            
             !PGPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPB@@&YYB#BP##&@@@@&BPG##P????JYJ????JGG!           
            :5GPPPPPPPPPPPPPPPPPPPPGGGGGGPPPPPPPPPB@@&J5@@@@@@@&&&@@@@@@@B????????????5G5:          
            ?PPPPPPPPPPPPPPPPPPPGGGP5555PGGGPPPPPPG&@&5J&@@@&#B####B&@@@@P77???????????PG?          
           ^5GPPPPPPPPPPPPPPPPPGP?~:.  .:~?PGPPPPG5?55P#@@@&GB@@@@@#G#@@@@G5Y??????????YGP^         
           ?GPPPPPPPPPPPPPPPPPGJ:          :JGPPPG57P@@@@@@BPB@@@@@#PG@@@@@@#???????????PG?         
          ^5GPPPPPPPPPPPPPPPPGY             .YGPPG577?Y#@@@&GPGB#BGPP#@@@@BPY???????????5GP:        
          !PGPPPPPPPPPPPPPPPPG7              7GPPG57~  ~#@@@&#GGGGGB&@@@@P77????????????JPG!        
         .JGPPPPPPPPPPPPPPPPPGJ              YGPPG5?7!:?&@@@@@@@@@@@@@@@@B???????????????PGY        
         ^5GPPPPPPPPPPPPPPPPPPG?.          .JGPPPG5???7Y#&#GB#@@@@@&#GB&&G???????????????YGP:       
         !PPPPPPPPPPPPPPPPPPPPPG57:.    .^75GPPPPG5????7???77?5@@@B??7???7???JY5PY???????JPG~       
         ?GPPPPPPPPPPPPPPPPPPPPPGGP5YJJY5PGGPPPPPPP555555Y55YYY55Y?7????JY55PGGPPY????????PG7       
        .YGPPPPPPPPPPPPPPPPPPPPPGPGGGGGGGGPPPPPPPPPGGGGGGGPPPPP555YJY5PPPGPGPPPPPGP???????5G?       
        .YGPPPPPPPPPPGPB@@@@@@@GPGPPPPPPPPPPPP&@@@@@@@@@@@@@@&&#BPPPGGGGPPB@@@@@GPP??????5PGJ       
         ?PGGPPPPPPPGPG@@@@@@@@&PPPPGGGPPPPPPP&@@@@@@@@@@@@@@@@@@@#PPPP5PP#@@@@@BPP???J5PGGG7       
          ~YPGGPPPPPPP&@@@@&@@@@#PPP55PPGGGGPP&@@@@&BBB######&@@@@@&PPPJPP#@@@@@GPPJYPGGGG5~        
            ~JPGGGPP5#@@@@&G&@@@@BPG7 .:^~!YGP&@@@@&PP5?77!75GB@@@@@&PPPPP#@@@@@GPPGGGGPJ~          
              :!JPGPB@@@@&GPB@@@@@GPP^     7GP&@@@@&PG7     ^PP#@@@@@GPPPP#@@@@@GPGGPJ!:            
                :5PG@@@@@BPGP#@@@@&PP5.    ?GP&@@@@&PG7 ....!GP#@@@@@GPGPP#@@@@@GPP~.               
               .JPP&@@@@#PPYPG&@@@@#5GJ    7GP&@@@@&PP5Y5Y55P5G&@@@@&GG5PP#@@@@@GG5.                
               7PP#@@@@&GG5?PPG&@@@@BPG!   7GP&@@@@&BBBBBBBB#&@@@@@&BGY~PPB@@@@@GP5.                
              ^PPB@@@@&GPPPPPPPB@@@@@GPP^  7GP&@@@@@@@@@@@@@@@@@@@#BGJ.:PPB@@@@@GP5.                
             :YPG@@@@@@&&&&&&&&&@@@@@&PG5. ?GP&@@@@@@@@@@@@@@&&&#BPJ~  :PP#@@@@@GG5.                
            .JPP&@@@@@@@@@@@@@@@@@@@@@#5GJ 7GP&@@@@&GGGGGGGGPP5Y?!:    :PP#@@@@@GG5.                
            !PP#@@@@@#############@@@@@BPG!7GP&@@@@&PG?::::::..        :PP#@@@@@GG5.                
           ^5PB@@@@@#P5????????JPG&@@@@@GPP5PP&@@@@&PG!                :PP#@@@@@GG5.                
          :YPG@@@@@&GP~         ?GG&@@@@&PPGPP&@@@@&PG7                :PP#@@@@@GG5.                
          ?GG&@&&&&BP7          .5GB&&&&&#PGGG&&&&&&GG7                :PG#&&&&&BG5.                
          ^JY55555YJ!.           :J5PPPPPP5YJ5PPPPPP5J:                 !Y5PPPPP5Y~                 
             ....                  ........  ........                     .......                  \n""")

    print('  As you chose New bot, you\'ll need a discord bot API key (a bot token). \n If you do not know how to get one, here\'s a tutorial : https://rapidapi.com/volodimir.kudriachenko/api/DiscordBot/details')


def DPL_api () -> None:
    os.system("title New bot, Deepl API key ")
    print("""
                                             ..::::::..                                             
                                          ..::::::::::::..                                          
                                      ..::::::::::::::::::::..                                      
                                  ..::::::::::::::::::::::::::::..                                  
                               ..::::::::::::::::::::::::::::::::::..                               
                           ..::::::::::::::::::::::::::::::::::::::::::..                           
                        .::::::::::::::::::::::::::::::::::::::::::::::::::.                        
                      .:::::::::::::::::...::::::::::::::::::::::::::::::::::.                      
                      :::::::::::::::.       .::::::::::::::::::::::::::::::::                      
                      :::::::::::::::         .:::::::::::::::::::::::::::::::                      
                      :::::::::::::::          .::::::::::::::::::::::::::::::                      
                      ::::::::::::::::.     ..    ..::::::::::::::::::::::::::                      
                      :::::::::::::::::::::::::..    ..:::::::::::::::::::::::                      
                      :::::::::::::::::::::::::::::..    .      .:::::::::::::                      
                      :::::::::::::::::::::::::::::::::.         .::::::::::::                      
                      ::::::::::::::::::::::::::::::::::.        .::::::::::::                      
                      ::::::::::::::::::::::::::::::.::::.      .:::::::::::::                      
                      ::::::::::::::::::::::::::..    ::::::..::::::::::::::::                      
                      ::::::::::::::::...  ....    ..:::::::::::::::::::::::::                      
                      :::::::::::::::.         ..:::::::::::::::::::::::::::::                      
                      :::::::::::::::         .:::::::::::::::::::::::::::::::                      
                      :::::::::::::::.       .::::::::::::::::::::::::::::::::                      
                      .::::::::::::::::.....:::::::::::::::::::::::::::::::::.                      
                        ..::::::::::::::::::::::::::::::::::::::::::::::::..                        
                            ..::::::::::::::::::::::::::::::::::::::::..                            
                                ..::::::::::::::::::::::::::::::::..                                
                                   ..:::::::::::::::::::::::::::.                                   
                                       ..:::::::::::::::::::::::                                    
                                           ..:::::::::::::::::::                                    
                                              ..::::::::::::::::                                    
                                                  ..::::::::::::                                    
                                                      ..::::::::                                    
                                                         ..:::::                                    
:::::::::::::..                                              ...                       .::::        
::::::::::::::::.                                                                      .::::        
::::.       .:::::.        ....:....             ....:....        ..    ....:...       .::::        
::::.         :::::      .::::::::::::.       .::::::::::::.     .:::..:::::::::::.    .::::        
::::.         .::::.   .::::..    .::::.     .::::.    ..::::.   .::::::... ...::::.   .::::        
::::.          ::::.   ::::.........::::.   .::::.........::::   .:::::        .::::.  .::::        
::::.         .::::.  .::::::::::::::::::   ::::::::::::::::::.  .::::.         ::::.  .::::        
::::.        .::::.   .::::..............   :::::..............  .:::::         ::::.  .::::        
::::.      ..::::.     .:::..      ...      .::::.       ...     .::::::.     .::::.   .::::.       
::::::::::::::::.       .::::::::::::::       .:::::::::::::.    .::::::::::::::::.    .::::::::::::
::::::::::::..            ..::::::::..          ..:::::::..      .::::...::::::..       ::::::::::::
                                                                 .::::                              
                                                                 .::::                              
                                                                 .::::                             """)
    
    print('  Now, you\'ll need a Deepl API (Free or Paid, both works fine for a reasonable amount of messages per month)\n If you do not know how to find yours, here\'s a tutorial : https://support.deepl.com/hc/en-us/articles/360020695820-Authentication-Key')



if __name__ == "__main__":
    print("This is a library module and is not intended to be run directly, please use AT_bot.py .")