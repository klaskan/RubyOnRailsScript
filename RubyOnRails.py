import os
import sys
import webbrowser

def start_prosjekt_rails(mappe, navnProsjekt):
	os.chdir("%s" % mappe)
	#os.chdir("%s" % plasering)
	os.system("rails new %s" % navnProsjekt)

def add_to_git(mappe, navnProsjekt, kommentar_git, link_github):
	os.chdir(("%s/%s") % (mappe, navnProsjekt))
	os.system("git init")
	os.system("git status")
	os.system("git add .")
	os.system("git commit -am'%s'" % kommentar_git)
	os.system("%s" % link_github)
	os.system("git push -u origin master")
	
def rails_generate_controller(mappe, navnProsjekt, action, options):
	os.chdir(("%s/%s") % (mappe, navnProsjekt))
	os.system("rails generate controller %s %s" % (action, options))





newpro = raw_input("Vil du lage et nytt prosjektet? y/n : ")
if newpro == "y":
	m = raw_input("Hvor skal jeg lagre prosjektet? eks /Users/Klaskan/Documents/RailsPro ")
	n = raw_input("Navn Prosjekt: ")
	start_prosjekt_rails(m,n)

	a = raw_input("kommentar paa commit: ")
	webbrowser.open("https://github.com/")
	b = raw_input("Link github: ")
	add_to_git(m, n, a, b)
else:
	print "kk"



gencon = raw_input("Vil du generer en controller? y/n : ")
if gencon == "y":
	ac = raw_input("action: ")
	op = raw_input("options (dette kan være flerer sider, bare husk mellomrom mellom dem: ")
	rails_generate_controller(m, n, ac, op )

else:
	print "kk"