# 👍 SimpleInstagram Bot
### If there are any errors with the output, contact westside#2630
### Or you can leave something inside of the "Issues" bar.

import os, time

os.system("pip install selenium==3.141.0")
os.system("clear")

from webbot import Browser

class WebEagle:
      BrowsingAs = ""
      def Browser(proxy: str = None):
                 if proxy == None:
                    WebEagle.BrowsingAs = Browser()
                 else:
                    try:
                        WebEagle.BrowingAs = Browser(proxy = proxy)
                    except:
                        print(' Bad Proxy | {} | WebEagle'.format(proxy))
                        WebEagle.BrowsingAs = Browser() 

      def get(url: str, delay: int = None):
          try: 
              if WebEagle.BrowsingAs == "":
                 exit(print(" Insufficient Browsing Data | WebEagle"))
              else:
                 if "https://" or "http://" in url:
                    WebEagle.BrowsingAs.go_to(url)
                 else:
                    print("Cannot GET Invalid Website | {} | WebEagle".format(url))
          except Exception as E:
               exit(print(E))

class WebInsta:
      _prefix = ""
      _logged = False
     #_---------_#


      _credits  = ""
      _password = ""

      def Bot(command_prefix: str = None):
          WebEagle.Browser()
          WebEagle.get("https://instagram.com")

          if command_prefix == None:
                    exit(print(" [🛑] Command Prefix | Undefined"))
          else: 
                    WebEagle._prefix = command_prefix
              
      def login(username = "", password = ""):
          WebInsta._credits = username
          WebInsta._password = password
          if username and password == None or username == None or password == None:  
              exit(print(" [🛑] Login Info | Undefined"))
          else:
              try:
                  print(" [👍] Logging In | ...")
                  WebEagle.BrowsingAs.type(WebInsta._credits, xpath = "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
                  WebEagle.BrowsingAs.type(WebInsta._password, xpath = "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
                  WebEagle.BrowsingAs.click(css_selector = ".L3NKy")
  
                  print(" [👍] Logged In  | Successfuly")
                  time.sleep(5)
              except:
                  print(" [🛑] Unknown Error | Could not Login")

      def follow_from_list(accounts=[]):
          followed = 0
          failed   = 0
          for account in accounts:
              try:
                  WebEagle.BrowsingAs.go_to("https://instagram.com/{}/".format(account))
                  
                  #-------------#
                  WebEagle.BrowsingAs.click(xpath = "/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div/button")
                  print(" [!] Followed {}".format(account))
                  #-------------#
                  
                  followed += 1
              except:
                  print(" [!] Account Doesn't Exist")
                  failed += 1
          print (" [!] Followed ({}/{})".format(followed, failed))
      
      def send_message(user, message: str):
          print(" [👍] Loading..")
          WebEagle.get("https://www.instagram.com/direct/new")

          #_--------_#
          WebEagle.BrowsingAs.click(xpath = "/html/body/div[1]/section/div/div[2]/div/div/div[2]/div/div[3]/div/button")
          WebEagle.BrowsingAs.type(user, xpath = "/html/body/div[6]/div/div/div[2]/div[1]/div/div[2]/input")
          #_--------_#


          try:
              WebEagle.BrowsingAs.click(xpath = "/html/body/div[6]/div/div/div[2]/div[2]/div[1]/div")
              WebEagle.BrowsingAs.type(message, xpath = "/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
              WebEagle.BrowsingAs.click(xpath = "/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button")

              print(" [👍] {} was DMED successfully".format(user))
          except:
              print(" [🛑] Could Not DM")

          #_--------_#
