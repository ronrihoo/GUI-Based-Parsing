import time

import terminaldriver as terminal
import nanodriver as nano
import browserdriver as browser


# scalar
# 
# Brief: scales the wait time in the wait() method
#
# NOTE: if something goes wrong and if all the required packages are available,
# then try changing scalar to 2 or 3 (or higher, depending on your machine)
scalar = 1

verbose = True

url = 'http://go.flatironschool.com/ebook-no-brainer-tech-hire'

terminal.setLogging(verbose)
nano.setLogging(verbose)
browser.setLogging(verbose)


def note(msg):
	if verbose:
		print(msg)


def wait(sec=0.25, scalar=scalar):
	unit = 'seconds'
	if scalar == 1: unit = 'second'
	note('waiting {} {}'.format(sec*scalar, unit))
	time.sleep(sec*scalar)


def flatironRig_FixUrl():
	note('applying fix to the URL that was parsed from Flatiron\'s webpage')
	# removing backslashes: 'http:\/\/'
	nano.replaceAll("\\", "")


def flatironRig_formBypass():
	flatironRig_FixUrl()
	wait()
	nano.highlight('"', '"')


def copyUrlToClipboard(a, b):
	terminal.openNewSession()
	wait(.5)
	nano.open()
	terminal.paste()
	if not b:
		flatironRig_formBypass()
	else:
		nano.highlight(b, a)
	nano.removeAllNonSelected()
	# temporarily save contents in a file
	nano.saveAndExit('temp369.txt')
	terminal.copyFileContentsToClipboard('temp369.txt')
	terminal.removeFile('temp369.txt')
	terminal.close()


def getUrlFromSourcePage(keyword1, keyword2=''):
	browser.invokeSourcePage()
	wait(.5)
	browser.findTargetKeyword(keyword1)
	browser.copyLine()
	copyUrlToClipboard(keyword1, keyword2)


def getPdfFromFlatiron():
	# open firefox with target url
	terminal.openPrivateTabInFirefox(url)
	wait(5)
	# bypass form
	getUrlFromSourcePage('redirect')
	browser.loadAddressInBrowser()
	wait(.5)
	# load PDF
	getUrlFromSourcePage('.pdf', 'http://')
	browser.loadAddressInBrowser()
