import subprocess
import pyautogui as pag

logging = True


def setLogging(state):
	logging = state


def cli(cmd):
	if logging: print('opening {} browser: {}'.format(cmd[0], cmd[2]))
	subprocess.Popen(cmd)
	#print(displayOutput(cmd))


def displayOutput(cmd):
	if logging: print('waiting for response from subprocess')
	return subprocess.check_output(cmd).decode("utf-8")#.strip()


def paste():
	if logging: print('pasting in terminal')
	pag.hotkey('ctrl', 'shift', 'v')


def openNewSession():
	if logging: print('opening new terminal session')
	pag.hotkey('ctrl', 'alt', 't')


def openPrivateTabInFirefox(url):
	firefoxPath = '/usr/bin/firefox'
	browserType = '--private-window'
	command = ['firefox', browserType, url]
	cli(command)


def copyFileContentsToClipboard(filename):
	if logging: print('copying contents of file, \'{}\', to the clipboard via terminal'.format(filename))
	pag.typewrite('xsel --clipboard ')
	pag.hotkey('shift', ',') # '<'
	pag.typewrite(' {}'.format(filename))
	pag.press('enter')


def removeFile(filename):
	if logging: print('removing file, \'{}\', via terminal'.format(filename))
	pag.typewrite('rm {}'.format(filename))
	pag.press('enter')


def close():
	if logging: print('closing terminal session')
	pag.hotkey('alt', 'f4')
