import subprocess

applescript_facetime='''
do shell script "open facetime://+8618939933901"
tell application "System Events"
	repeat while not (button "呼叫" of window 1 of application process "FaceTime" exists)
		delay 1
	end repeat
	click button "呼叫" of window 1 of application process "FaceTime"
end tell
'''


applescript_call='''
do shell script "open location tel://+8618939933901"
tell application "System Events" 
key code 36
end tell
'''


args = [item for x in [("-e",l.strip()) for l in applescript_facetime.split('\n') if l.strip() != ''] for item in x]
subprocess.Popen(["osascript"] + args, stdout=subprocess.PIPE)


