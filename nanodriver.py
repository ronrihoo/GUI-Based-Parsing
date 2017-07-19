import pyautogui as pag

nanoLogging = True


def setLogging(state):
	nanoLogging = state


def open():	
	if nanoLogging: print('opening nano in terminal')
	pag.typewrite('nano')
	pag.press('enter')


def findString(str):
	if nanoLogging: print('finding string, \'{}\', in nano'.format(str))
	pag.hotkey('ctrl', 'w')
	pag.press(str)
	pag.press('enter')


def findNext():	
	if nanoLogging: print('finding next in nano')
	pag.hotkey('ctrl', 'w')
	pag.press('enter')


def replaceAll(a, b):
	if nanoLogging: print('replacing all \'{}\' with \'{}\' in nano'.format(a, b))
	pag.hotkey('ctrl', '\\')
	pag.press(a)
	pag.press('enter')
	pag.press(b)
	pag.press('enter')
	pag.press('a')


def markCurrentPosition():
	if nanoLogging: print('marking current cursor position in nano')
	pag.hotkey('ctrl', '6')


def moveCursorUp(x=1):
	if nanoLogging: print('moving cursor up {} times in nano'.format(x))
	pag.press(['up']*x)


def moveCursorLeft(x=1):
	if nanoLogging: print('moving cursor left {} times in nano'.format(x))
	pag.press(['left']*x)


def moveCursorRight(x=1):
	if nanoLogging: print('moving cursor right {} times in nano'.format(x))
	pag.press(['right']*x)


def moveCursorDown(x=1):
	if nanoLogging: print('moving cursor down {} times in nano'.format(x))
	pag.press(['down']*x)


def highlight(a, b):
	if nanoLogging: print('highlighting from \'{}\' to \'{}\' in nano'.format(a, b))
	findString(b)
	# re-adjust cursor for highlighting
	if a != b:
		moveCursorRight(len(b))
	markCurrentPosition()
	if a == b:
		findNext()
	else: 
		findString(a)


def copy():
	if nanoLogging: print('copying in nano')
	pag.hotkey('alt', '6')


def paste():
	if nanoLogging: print('pasting in nano')
	pag.hotkey('ctrl', 'u')


def cut():
	if nanoLogging: print('cutting in nano')
	pag.hotkey('ctrl', 'k')


def delete():
	if nanoLogging: print('deleting text in nano')
	pag.press('del')


def removeAllNonSelected():
	'''
		Assumes that there is only one line in file
	'''
	if nanoLogging: print('removing all nonselected content in nano, where there\'s only one line in file')
	copy()
	# paste it on the next line (due to nano cut/delete limitation)
	moveCursorDown()
	paste()
	# go back and cut the first line (get rid of the unneeded portion)
	moveCursorUp()
	cut()
	# bring line 2 to line 1
	delete()


def saveNewFile(filename):
	if nanoLogging: print('saving \'{}\' file in nano'.format(filename))
	pag.hotkey('ctrl', 'o')
	pag.typewrite(filename)
	pag.press('enter')


def exitAfterSaving():
	if nanoLogging: print('exiting nano')
	pag.hotkey('ctrl', 'x')


def saveAndExit(filename):
	saveNewFile(filename)
	exitAfterSaving()
