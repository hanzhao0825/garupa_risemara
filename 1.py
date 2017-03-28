import os
import time

def log(str):
	print time.asctime( time.localtime(time.time()) ), " : ", str

def force_stop():
	log("stop")
	os.system("adb shell am force-stop jp.co.craftegg.band");
	time.sleep(1)

def rm_sav():
	log("rm_sav")
	os.system("adb shell rm /sdcard/Android/data/jp.co.craftegg.band/files/EhNfQ7brV3f3cCIcW9O4OaZxwC0V6UH1")
	time.sleep(1)

def run():
	log("run")
	os.system("adb shell monkey -p jp.co.craftegg.band -c android.intent.category.LAUNCHER 1")
	time.sleep(1)

def screenshot():
	filename = time.time()
	os.system("adb shell screencap -p /sdcard/" + str(filename) + ".png")
	os.system("adb pull /sdcard/" + str(filename) + ".png ~/Downloads/screen/")
	os.system("adb shell rm /sdcard/" + str(filename) + ".png")


def click(x, y):
	log("click " + str(x) + " " + str(y))
	os.system("adb shell input tap " + str(x) + " " + str(y));
	time.sleep(0.7)

def click_center():
	click(640, 360)

def click_skip():
	click(1200, 60)
	click(660, 60)
	click(720, 480)

def click_yes_1():
	click(720, 480)

def click_center_1():
	click(600, 480)

def click_close():
	click(900, 610)

def click_close_center():
	click(640, 600)

def click_close_center_1():
	click(640, 610)

def click_ok_center():
	click(640, 450)

def click_ok_center_1():
	click(640, 540)

def click_story():
	click(900, 270)

def click_gatcha():
	click(750, 480) # 3
	time.sleep(8) 
	click_center();
	time.sleep(8)
	click_center();


while 1: 
	force_stop()
	rm_sav()
	run()

	time.sleep(15) # title
	click_center()

	click_yes_1() # allow
	time.sleep(7)

	click_skip() # skip
	click_center_1() # name
	click_close()
	click_close()
	click_close()
	click_yes_1() # speed

	time.sleep(10) # song loading
	click_close()
	click_close()
	click_close()
	click_close()

	time.sleep(48) # song
	click_close()
	time.sleep(4)
	click_close_center()
	time.sleep(1)
	click_close_center_1()
	click_close()
	click_close()
	time.sleep(2)
	click_ok_center()
	time.sleep(2)
	click_ok_center_1()
	click_close()
	click_close()
	click_close()
	click(990, 630)

	click_story() # story
	click(990, 630)
	click_ok_center() # no voice
	time.sleep(1)
	click_skip()
	click_ok_center_1()
	click_ok_center_1()
	click_ok_center_1()

	click(60, 60) # map
	click(360, 400)
	time.sleep(4)
	click_close()
	click_close()
	click_center()
	click_skip()
	time.sleep(2);
	click_ok_center()
	click_ok_center_1()
	click(990, 630)

	click_story() # story
	click(990, 630)
	click_ok_center() # no voice
	time.sleep(1)
	click_skip()
	click_ok_center_1()
	click_ok_center_1()
	click_ok_center_1()
	click_ok_center_1()
	click_close()
	click_close()
	click_close()
	click(1200, 600) # live
	click(750, 540) # download

	time.sleep(12) # title
	click_center()

	time.sleep(5)
	click_close()
	time.sleep(1)
	click_close()
	time.sleep(2)
	click_close()
	time.sleep(2)
	click(640, 610)
	time.sleep(1)

	click(1200, 260) # present
	time.sleep(2)
	click(1050, 120)
	time.sleep(3)
	click(640, 600)
	click(60, 60)

	click(690, 630) # gatcha
	time.sleep(2)
	click(900, 600)
	click_gatcha()
	click(240, 615)
	click_gatcha()
	click(240, 615)
	click_gatcha()
	click(240, 615)
	click_gatcha()
	click_close()
	time.sleep(2)

	click(60, 60)
	click(810, 615) # band
	click(1020, 390)
	screenshot()

	click(60, 60)
	click(60, 60)
	click(1200, 60) # menu
	click(600, 390)
	time.sleep(3)

	click(600, 435)
	os.system("adb shell input text 12345678")
	time.sleep(1)
	os.system("adb shell input keyevent 4")
	time.sleep(1)
	click(720, 550)
	time.sleep(3)
	screenshot()




