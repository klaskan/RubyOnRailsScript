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

def git_log(mappe, navnProsjekt):
	os.system("git log")
	backTrack = raw_input("onsker du aa gaa tilbake til en tidligere versjon y/n ")
	if backTrack == "y":
		tidligereGit = raw_input("Git-IDen: ")
		os.system("git checkout %s" % tidligereGit)		 	
	else:
		True
	#her kan du sette tilbake til tidligere versjoner med aa skrive "git reset 1cfef3e9" de random tallene og bokstavene er de 8 forste tall/bokstaver i commit-id

def commit_add_push(mappe, navnProsjekt, kommentar_git):
	os.system("git status")
	os.system("git add .")
	os.system("git commit -am'%s'" % kommentar_git)
	os.system("git push -u origin master")


one = "1. Lag nytt Ruby on rails Prosjekt"
two = "2. Legg til 'git' i nytt prosjektet."
tree = "3. Generer en controller" 
four = "4. Se git log/ gaa tilbake til tidligere versjon"
five = "5. commit og push"
m = ""
n = ""

while True:
	
	print "Hva vil du? Skriv inn tallet."
	print one
	print two
	print tree 
	print four
	print five
	newpro = raw_input("Tall: ")

	if newpro == "1":
		m = raw_input("Hvor skal jeg lagre prosjektet? eks /Users/Klaskan/Documents/RailsPro ")
		n = raw_input("Navn Prosjekt: ")
		start_prosjekt_rails(m,n)
		True

	elif newpro == "2":
		if len(m) == 0 or len(n) == 0:  
			m = raw_input("Hvor skal jeg lagre prosjektet? eks /Users/Klaskan/Documents/RailsPro ")
			n = raw_input("Navn Prosjekt: ")
			a = raw_input("kommentar paa commit: ")
			webbrowser.open("https://github.com/")
			b = raw_input("Link github: ")
			add_to_git(m, n, a, b)
			True
		else:
			a = raw_input("kommentar paa commit: ")
			webbrowser.open("https://github.com/")
			b = raw_input("Link github: ")
			add_to_git(m, n, a, b)
			True

	elif newpro == "3":
		if len(m) == 0 or len(n) == 0:
			m = raw_input("Hvor skal jeg lagre prosjektet? eks /Users/Klaskan/Documents/RailsPro ")
			n = raw_input("Navn Prosjekt: ")
			ac = raw_input("action: ")
			op = raw_input("options (dette kan vare flerer sider, bare husk mellomrom mellom dem: ")
			rails_generate_controller(m, n, ac, op ) 
			True
		else:	
			ac = raw_input("action: ")
			op = raw_input("options (dette kan vare flerer sider, bare husk mellomrom mellom dem: ")
			rails_generate_controller(m, n, ac, op ) 
			True
	
	elif newpro == "4":
		if len(m) == 0 or len(n) == 0:  
			m = raw_input("Hvor skal jeg lagre prosjektet? eks /Users/Klaskan/Documents/RailsPro ")
			n = raw_input("Navn Prosjekt: ")
			git_log(m, n)
		else:
			git_log(m, n)

	elif newpro == "5":
		
		if len(m) == 0 or len(n) == 0 or len(a) == 0:  
			m = raw_input("Hvor skal jeg lagre prosjektet? eks /Users/Klaskan/Documents/RailsPro ")
			n = raw_input("Navn Prosjekt: ")
			a = raw_input("kommentar paa commit: ")
			commit_add_push(m, n, a)
		else:
			commit_add_push(m, n, a)

	else:
		print "Det du skrev inn er ikke stottet"
		True



