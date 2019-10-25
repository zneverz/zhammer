# appscript = '''
#     do shell script "open facetime://+8618939933901"
#     tell application "System Events"
#         repeat while not (button "呼叫" of window 1 of application process "FaceTime" exists)
#             delay 1
#         end repeat
#         click button "呼叫" of window 1 of application process "FaceTime"
#     end tell
#     '''
#
# p = appscript.find('facetime://')
#
# print(p)
# print(appscript[27:])
#
#

d = {'Name': 'Zara', 'Age': 7, 'fuck': 'Manni'}

a = d.items()

